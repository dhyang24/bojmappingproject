#include <iostream>
#include <string>
using namespace std;
#define input(a) (cin >> a)
#define print(a) (cout << a)

int main(void){
    int counter = 0;
    string a,b;
    int it;
    string thing;
    while (true){
        input(a);input(b);
        if (a == "#" and b == "#"){
            break;
        }
        cin >> it;
        print("Case ");
        print(counter+1);
        for(int q=0; q<it+1; q++){
            getline(cin,thing);
            for(int i=0;i<thing.size(); i++){
                if (tolower(thing.at(i)) == a[0] or tolower(thing.at(i)) == b[0]){
                    print("_");
                }else{
                    print(thing[i]);
                }
            }
            print("\n");
        }
        print("\n");
        counter++;
    }
    return 0;
}