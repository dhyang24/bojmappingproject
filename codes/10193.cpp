#include<iostream>
#include<string>
using namespace std;
int main(void){
    int a;
    cin >> a;
    
    for (int i=0; i<a; i++){
        string q,w;
        cin >> q >> w;
        int ans = 0;
        for(int j=0; j < q.size(); j++){
            ans+=q[j]-w[j];
        }
        cout << "Swapping letters to make "+ q +" look like "+w;
        if (ans > 0){
            cout << " earned "<< ans << " coins.\n";
        } else if (ans < 0){
            cout << " cost " << (-1*ans) << " coins.\n";
        } else{
            cout << " was FREE.\n";
        }
    }
    return 0;
}