#include<string>
#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;
int main(void){
    int a,b;
    cin >> a >> b;
    string c;
    cin >> c;
    int ans = 0;
    int cur = 0;
    char now = 'O';
    for(int i=0; i<b; i++){
        if(c[i] == now){
            if(now == 'O'){
                cur = 0;
            }else{
                cur = 1;
            }
        }else{
            cur+=1;
            now = c[i];
        }
        if(cur >= a*2+1 && c[i] == 'I'){
            ans+=1;
        }
    }
    cout << ans << '\n';
}
