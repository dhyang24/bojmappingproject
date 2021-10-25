#include <iostream>
#include <string>
using namespace std;
int main(void){
    while (true){
        string a;
        getline(cin,a);
        if (a == string("#"))break;
        int move = 'A'-a.back();
        string ans = "";
        for(int i=0; i<a.size()-1;i++){
            if (char(a[i]) >= 'a' and char(a[i]) <= 'z'){
                ans.push_back((char(a[i])-'a'+move+26)%26+'a');
            }else if (char(a[i]) >='A' and char(a[i]) <= 'Z'){
                ans.push_back((char(a[i])-'A'+move+26)%26+'A');
            }else{
                ans.push_back(char(a[i]));
            }
        }
        cout << ans << '\n';
    }
}