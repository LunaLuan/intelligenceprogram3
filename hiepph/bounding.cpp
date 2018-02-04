#include <bits/stdc++.h>
using namespace std;

vector<int> bounding(vector<pair<int, int>> points) {
  // input: pair<x, y>
  // return vector<x1, y1, x2, y2>
  // x1: xmin, y1: ymin, x2: xmax, y2: ymax

  // corner: no points
  if (points.size() == 0) {
    return {};
  }

  // get all x
  vector<int> X;
  for (auto point : points) {
    X.push_back(point[0]);
  }

  // get all y
  vector<int> Y;
  for (auto point : points) {
    Y.push_back(point[1]);
  }

  return {min(X), min(Y), max(X), max(Y)};
}
