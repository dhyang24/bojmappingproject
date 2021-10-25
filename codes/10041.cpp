#include <iostream>
using namespace std;
#define min(a,b) a < b ? a : b
int main(void){
    int a,b,c;
    cin >> a >> b >> c;
    int temp1,temp2;
    cin >> temp1 >> temp2;
    int ans = 0;
    for(int i=1; i<c; i++){
        int temp3,temp4;
        cin >> temp3 >> temp4;
        if ((temp1-temp3)*(temp2-temp4) >= 0){
            ans+=abs(temp1-temp3)+abs(temp2-temp4)-(min(abs(temp1-temp3),abs(temp2-temp4)));
        }else{
            ans+=abs(temp1-temp3)+abs(temp2-temp4);
        }
        temp1 = temp3;
        temp2 = temp4;
    }
    cout << ans << '\n';
}