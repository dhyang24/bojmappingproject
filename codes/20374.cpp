#include <iostream>
#include <stdio.h>
using namespace std;
int main(void){
    long double a = 0;
    while (true){
        long double thing;
        cin >> thing;
        if (cin.eof()){
            break;
        }
        a+=thing;
    }
    printf("%.2Lf",a);
}