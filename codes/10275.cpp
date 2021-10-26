#include <iostream>
using namespace std;
int main(void){
    int thing;
    cin >> thing;
    for (int qwer =0;qwer<thing;qwer++){
        unsigned long long int a,b,c;
        cin >> c >> a >> b;
        int ans = 0;
        for (int p=0; p<c; p++){
            if (a&(1)){
                cout << (c-p) << "\n";
                break;
            }
            a = a/2;
        }
    }
    return 0;
}