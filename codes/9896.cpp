#include <iostream>
#include <string>
using namespace std;
int main(void){
    int a;
    cin >> a;
    string b;
    cin >> b;
    string ans;
    ans = b[0];
    for (int i=1; i<a; i++){
        ans.push_back((b[i]-'0')^(b[i-1]-'0')+'0');
    }
    cout << ans;
}