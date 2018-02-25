'''
To be able to run this tool inside ArcGIS Pro:

1. Copy the ArcGIS Pro env to a new folder.
2. In clean ArcGIS Pro env, install with built-in Pro package manager:
* PyQt 5.6
* shapely 1.7
3. Create a new custom script tool (with a parameter to specify path to a shapefile
or a feature class) and point to this source Python module.
4. Run the script tool. It might take some seconds for the tool to start. This is
because the PyQt modules are being imported. The following starts of the tool inside
the same Pro session will go much faster.
5. Adjust the slider to tune the borders. When ready, click the Add to the map button
to add the triangulation and the final polygon(s) to the project's map.

Notes:
* Multipolygons are supported.
* Output datasets are written using the sr of the source points layer.
* This is a sample app and it does not perform well when using large point datasets as
drawing them in Matplotlib takes time.

Credits:
`alpha_shape` function code - credits to Sean Gillies at
https://sgillies.net/2012/10/13/the-fading-shape-of-alpha.html
and
Kevin Dwyer at http://blog.thehumangeo.com/2014/05/12/drawing-boundaries-in-python/

You will need to tune the `alpha_factor` variable to adjust the boundaries
of the concave hull. For points spread around the whole California state, set 1000.
For a county, set 100. For the points of an average city, set 1. This may require
some experimenting.
'''

import os
import sys
import math
import arcpy
import numpy as np
from scipy.spatial import Delaunay

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QSlider, QPushButton, QVBoxLayout

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.collections import LineCollection
from matplotlib.patches import Polygon

from shapely.ops import cascaded_union, polygonize
import shapely.geometry as geometry

plt.style.use('ggplot')
arcpy.env.overwriteOutput = True


class Window(QDialog):
    def __init__(self, input_shapefile, parent=None):
        super(Window, self).__init__(parent)

        self.input_shapefile = input_shapefile
        self.source_sr = arcpy.Describe(input_shapefile).spatialReference
        self.out_sr = arcpy.SpatialReference(3857)

        self.init_points()

        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the button to add the result layers to the map
        self.button = QPushButton('Add to the map')
        self.button.clicked.connect(self.add_to_map)

        # set the slider for the alpha value
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setSingleStep(1)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setRange(1, 100)  #(1, 45)
        self.slider.valueChanged.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.slider)

        self.setLayout(layout)

        # plotting initial dataset
        self.init_run = True
        self.all_circum_r = []

        self.alpha_factor = 1  # need to tune for the specific dataset, read module docstring
        self.alpha = 1
        self.plot()

    #----------------------------------------------------------------------
    def init_points(self):
        """initialize spatial properties"""
        # will read arcpy geometries coordinates using meters as units
        feats = [
            p[0]
            for p in arcpy.da.SearchCursor(
                self.input_shapefile,
                'SHAPE@XY',
                spatial_reference=self.out_sr)
        ]
        self.x = [feat[0] for feat in feats]
        self.y = [feat[1] for feat in feats]
        self.points = [geometry.Point(feat) for feat in feats]
        return

    #----------------------------------------------------------------------
    def alpha_shape(self, points, alpha):
        """
        Compute the alpha shape (concave hull) of a set
        of points.
        @param points: Iterable container of points.
        @param alpha: alpha value to influence the
            gooeyness of the border. Smaller numbers
            don't fall inward as much as larger numbers.
            Too large, and you lose everything!
        """
        if len(points) < 4:
            # When you have a triangle, there is no sense
            # in computing an alpha shape.
            return geometry.MultiPoint(list(points)).convex_hull

        def add_edge(edges, edge_points, coords, i, j):
            """
            Add a line between the i-th and j-th points,
            if not in the list already
            """
            if (i, j) in edges or (j, i) in edges:
                # already added
                return
            edges.add((i, j))
            edge_points.append(coords[[i, j]])

        coords = np.array([point.coords[0] for point in points])
        tri = Delaunay(coords)
        edges = set()
        edge_points = []
        # loop over triangles:
        # ia, ib, ic = indices of corner points of the
        # triangle
        for ia, ib, ic in tri.vertices:
            pa = coords[ia]
            pb = coords[ib]
            pc = coords[ic]
            # Lengths of sides of triangle
            a = math.sqrt((pa[0] - pb[0])**2 + (pa[1] - pb[1])**2)
            b = math.sqrt((pb[0] - pc[0])**2 + (pb[1] - pc[1])**2)
            c = math.sqrt((pc[0] - pa[0])**2 + (pc[1] - pa[1])**2)
            # Semiperimeter of triangle
            s = (a + b + c) / 2.0
            # Area of triangle by Heron's formula
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            circum_r = a * b * c / (4.0 * area)

            if self.init_run:
                self.all_circum_r.append(circum_r)

            # Here's the radius filter.
            #print(circum_r, 1.0 / alpha)
            if circum_r < 1.0 / alpha:
                add_edge(edges, edge_points, coords, ia, ib)
                add_edge(edges, edge_points, coords, ib, ic)
                add_edge(edges, edge_points, coords, ic, ia)
        m = geometry.MultiLineString(edge_points)
        triangles = list(polygonize(m))
        return cascaded_union(triangles), edge_points

    #----------------------------------------------------------------------
    def plot_polygon(self, polygon):
        """plot the concave hull polygon"""
        # this value needs to be adjusted depending on the map units used
        margin = (
            max(self.x) - min(self.x)) / 10  # 10% of margin around the data
        if not polygon.bounds:
            # all polygons are collapsed as there are no 3 points that are
            # sufficiently close to each other
            return
        x_min, y_min, x_max, y_max = polygon.bounds
        self.ax.set_xlim([x_min - margin, x_max + margin])
        self.ax.set_ylim([y_min - margin, y_max + margin])

        # multipolygon will be created when edges are too far (islands are created)
        if polygon.geometryType() == 'MultiPolygon':
            for poly in polygon:
                self.ax.add_patch(
                    Polygon(
                        (list([
                            list(i) for i in np.asarray(poly.exterior.coords)
                        ])),
                        alpha=0.2))
        else:
            self.ax.add_patch(
                Polygon(
                    (list([
                        list(i) for i in np.asarray(polygon.exterior.coords)
                    ])),
                    alpha=0.2))
        return

    #----------------------------------------------------------------------
    def plot(self):
        """build the concave hulls and plot all the data"""
        self.ax.cla()  # clear the axes

        if self.init_run:
            self.concave_hull, self.edge_points = self.alpha_shape(
                self.points,
                alpha=self.alpha)  # build the triangles and concave hull
            self.alpha_min = (1 / max(self.all_circum_r))
            self.alpha_max = 1 / min(self.all_circum_r) / self.alpha_factor
            self.init_run = False

        self.alpha = np.interp(self.slider.value(),
                               [self.slider.minimum(),
                                self.slider.maximum()],
                               [self.alpha_min, self.alpha_max])

        self.concave_hull, self.edge_points = self.alpha_shape(
            self.points, alpha=self.alpha)

        # add the triangles lines to the plot
        self.lines = LineCollection(self.edge_points)
        self.ax.add_collection(self.lines)

        self.ax.set_title(
            'Generating alpha shapes (concave hulls) with alpha of {}'.format(
                self.alpha))

        # add the concave hull to the plot
        self.plot_polygon(self.concave_hull)

        # plotting the source points as dots
        self.ax.plot(
            self.x, self.y, marker='o', linestyle='None', color='#f16824')

        self.canvas.draw()  # refresh canvas

    #----------------------------------------------------------------------
    def add_to_map(self):
        """save the concave hull and triangles edges as feature classes
        and add to the currently open map in the project"""
        # export shapely.geometry.Polygon to WKT and read into arcpy.Geometry
        concaves_feats = arcpy.FromWKT(self.concave_hull.to_wkt(),
                                       self.out_sr).projectAs(self.source_sr)

        wkt_lines = [
            geometry.LineString(edge_point).to_wkt()
            for edge_point in self.edge_points
        ]
        delaunay_feats = [
            arcpy.FromWKT(wkt_line, self.out_sr).projectAs(self.source_sr)
            for wkt_line in wkt_lines
        ]

        ondisk_concaves = os.path.join(
            arcpy.env.scratchGDB,
            'concaves_a{}'.format(str(self.alpha).replace('.', '_')))
        ondisk_delaunay = os.path.join(
            arcpy.env.scratchGDB,
            'delaunay_a{}'.format(str(self.alpha).replace('.', '_')))
        arcpy.CopyFeatures_management(concaves_feats, ondisk_concaves)
        arcpy.CopyFeatures_management(delaunay_feats, ondisk_delaunay)

        # the feature class will be added as the top layer to the TOC
        aprx = arcpy.mp.ArcGISProject('current')
        open_map = aprx.listMaps()[0]
        open_map.addDataFromPath(ondisk_concaves)
        open_map.addDataFromPath(ondisk_delaunay)


if __name__ == '__main__':
    input_shapefile = arcpy.GetParameterAsText(0)
    app = QApplication(sys.argv)
    main = Window(input_shapefile=input_shapefile)
    main.show()
    sys.exit(app.exec_())