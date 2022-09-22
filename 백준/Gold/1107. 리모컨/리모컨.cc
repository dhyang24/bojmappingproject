#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int a;
    int b;
    cin >> a >> b;
    int thing[10] = {0,0,0,0,0,0,0,0,0,0};
    for(int i=0; i<b;i++){
        int temp;
        cin >> temp;
        thing[temp] =1;
    }
    int ans = abs(100-a);
    for(int i=0; i<=1000000;i++){
        bool stat = true;
        int cur = i;
        int stats = 1;
        while(cur>=10){
            if(thing[cur%10]){
                stat = false;break;
            }
            cur = cur/10;
            stats++;
        }
        if(thing[cur%10]){
            stat = false;
        }
        if(!stat){
            continue;
        }
        if (ans == -1){
            ans = abs(a-i)+stats;
        }else{
            ans = min(ans,abs(a-i)+stats);
        }
    }
    cout << ans;
}
