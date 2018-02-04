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
    ios_base::sync_with_stdio(false);
   // freopen("convexhull_sample.in","r",stdin);
    //freopen("convexhull_sample.ans","w",stdout);
    while(scanf("%d", &n)!=0){
    for(int i=1; i<=n; i++) cin>>a[i].X>>a[i].Y;
    sort(a+1, a+n+1);
    origin = a[1];
    sort(a+2, a+n+1, cmp);
    a[0]=a[n]; a[n+1]=a[1];
    int j=1;
    for (int i=1; i<=n+1; i++){
        while (j>2 && !ccw(a[j-2], a[j-1], a[i])) j--;
        a[j++]=a[i];
    }
    n=j-2;
    for (int i=1;i<=n;i++) cout<<a[i].X<<" "<<a[i].Y<<endl;
    }
}
