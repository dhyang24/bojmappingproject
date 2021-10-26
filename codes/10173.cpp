#include <iostream>
#include <string>
using namespace std;
int main(void){
    while (1){
        string a;
        bool stat = false;
        getline(cin,a);
        if (a=="EOI")break;
        string b = "";
        for (int i=0; i<a.size();i++){
            b+=tolower(a[i]);
        }
        for (int i=3; i<b.size(); i++){
            if (b[i-3]=='n' and b[i-2] == 'e' and b[i-1] == 'm' and b[i]=='o'){
                stat = true;
                break;
            }
        }
        if(stat){
            cout << "Found\n";
        }else{
            cout << "Missing\n";
        }
    }
}