#include<vector>
#include<iostream>
using namespace std;
int main(void){
    vector<long long int> v;
    v.push_back(1);
    v.push_back(1);
    v.push_back(1);
    v.push_back(2);
    v.push_back(2);
    for(int i=0; i<100;i++){
        v.push_back(v[v.size()-1]+v[v.size()-5]);
    }
    int a;
    cin >> a;
    for(int i=0; i<a; i++){
        int temp;
        cin >> temp;
        cout << v[temp-1] << '\n';
    }
}
