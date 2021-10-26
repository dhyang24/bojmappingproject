#include <iostream>
#include <string>
using namespace std;
int main(void){
    while (1){
        int le;
        string a;
        cin >> le;
        if (le == 0)break;
        cin >> a;
        string ans = "";
        for(int i=a.size()-1; i>-1; i--){
            int temp = 0;
            if (a[i] == '_'){
                temp = 26;
            } else if (a[i] == '.') {
                temp = 27;
            } else{
                temp = a[i]-'A';
            }
            if ((temp+le)%28 == 26){
                ans.push_back('_');
            } else if ((temp+le)%28 == 27){
                ans.push_back('.');
            } else{
                ans.push_back((temp+le)%28+'A');
            }
        }
        cout << ans <<'\n';
    }
}