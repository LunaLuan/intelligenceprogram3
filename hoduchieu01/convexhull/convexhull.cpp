// convex hull
#include<bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
#define X first
#define Y second

ii origin;
void operator -= (ii &A, ii B){ A.X-=B.X; A.Y-=B.Y; }
bool ccw(ii O, ii A, ii B){ A-=O, B-=O; return A.X*B.Y > A.Y*B.X; }
bool cmp(ii A, ii B){ return ccw(origin, A, B); }

int n;
ii a[12309];

signed main(){
  //  freopen("bounding.inp","r",stdin);
  //  freopen("bounding.out","w",stdout);
    int i, t;
    while(scanf("%d",&n)==1){
    for (i=1; i<=n; i++)
    cin>>a[i].X>>a[i].Y;
    sort(a+1, a+n+1); // Sort các điểm theo tung độ, hoành độ
    origin = a[1]; // điểm đầu tiên của bao lồi là điểm có tung độ hoành độ nhỏ nhất
    sort(a+2, a+n+1, cmp);
    a[0]=a[n]; a[n+1]=a[1];
    int j=1;
    for (i=1; i<=n+1; i++){
        while (j>2 && !ccw(a[j-2], a[j-1], a[i])) j--;
        a[j++]=a[i];
    }
    n=j-2;
    cout<<n<<endl;
    for (i=1; i<=n; i++) cout<<a[i].X<<" "<< a[i].Y<<endl;
}
}
