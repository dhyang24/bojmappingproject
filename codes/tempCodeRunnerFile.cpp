#include <iostream>
using namespace std;
int main(void){
    int thing;
    cin >> thing;
    for (int qwer =0;qwer<thing;qwer++){
        unsigned long long int a,b,c;
        cin >> c >> b >> a;
        int ans = 0;
        for (int p=c; p>=0; p--){
            if (a&(1<<p)){ans=(c-p);}
            if (b&(1<<p)){ans=(c-p);}
        }
        cout << (ans)<<"\n";
    }
}