#include <iostream>
#include <string>
using namespace std;
int main(void){
    int a;
    cin >> a;
    for(int i=0; i<a; i++){
        string thing;
        cin >> thing;
        int ans = 0;
        for (int j=0;j<thing.size();j++){
            if (thing[j] == 'a' or thing[j] == 'e' or thing[j] == 'i' or thing[j] == 'o' or thing[j] == 'u'){
                ans++;
            }
        }
        cout << "The number of vowels in "<<thing<<" is "<<ans<<".\n";
    }
}