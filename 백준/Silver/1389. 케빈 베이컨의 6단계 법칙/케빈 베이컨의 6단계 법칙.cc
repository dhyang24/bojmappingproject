#include<iostream>
#include<vector>
#include<list>
#include<algorithm>
using namespace std;
bool visited[100];
vector<vector<int>> v(100);
int main(void){
    int a,b;
    cin >> a >> b;
    for(int i=0; i<b;i++){
        int q,w;
        cin >> q >> w;
        v[q-1].push_back(w-1);
        v[w-1].push_back(q-1);
    }
    int curmin = 123123123;
    int curp = -1;
    for(int i=0; i<a; i++){
        for(int j=0; j<100;j++){
            visited[j] = false;
        }
        list<int>temp;
        temp.push_back(i);
        temp.push_back(-1);
        visited[i] = true;
        int cur = 0;
        int tempans = 0;
        while (temp.size() != 1){
            int now = temp.front();
            temp.pop_front();
            if(now == -1){
                cur++;
                temp.push_back(-1);
                continue;
            }
            for(int j=0; j<v[now].size(); j++){
                if(!visited[v[now][j]]){
                    visited[v[now][j]] = true;
                    tempans+=cur+1;
                    temp.push_back(v[now][j]);
                }
            }
        }
        if(curmin > tempans){
            curmin = tempans;
            curp = i;
        }
    }
    cout << curp+1 << '\n';
}
