#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
struct testthing{
    int x,y,z;
};
int main(void){
    int iter;
    cin >> iter;
    for (int thing=0; thing<iter; thing++){
        int a,b;
        int visited[100][100] = {0,};
        cin >> a >> b;
        string c;
        cin >> c;
        int dir = 0;
        int ans = 0;
        visited[a][b]+=1;
        for (int p = 0; p < c.size();p++){
            if (c[p] == 'F'){
                if (dir == 0){
                    b+=1;
                } else if (dir == 3){
                    a+=1;
                } else if (dir == 1){
                    a-=1;
                } else if (dir == 2){
                    b-=1;
                }
                visited[a][b]+=1;
                if (visited[a][b] == 2){
                    ans++;
                }
            }else if (c[p] == 'L'){
                dir = (dir+1)%4;
            }else if (c[p] == 'R'){
                dir = (dir+3)%4;
            }
        }
        cout << "Case #" << (thing+1) << ": "<<a << " " << b << " "<<ans<<"\n";
    }
}