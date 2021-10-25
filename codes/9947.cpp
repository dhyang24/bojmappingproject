#include <iostream>
#include <string>
using namespace std;
int main(void){
    while(true){
        string a,b;
        cin >> a >>b;
        if (a=="#" and b == "#")break;
        int temp;
        cin >> temp;
        int ans1=0;int ans2=0;
        for (int i=0;i<temp;i++){
            string w,e;
            cin >> w >> e;
            if (w == e){
                ans1++;
            }else{
                ans2++;
            }
        }
        cout << a << ' '<< ans1 << ' '<< b << ' '<<ans2 <<'\n';
    }
}