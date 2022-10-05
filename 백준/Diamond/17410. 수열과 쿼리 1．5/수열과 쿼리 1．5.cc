#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
#pragma GCC optimize("Ofast")
int curdata[100000];
vector<int> datas[100];
int main(void){
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);
    for(int i=0; i<100; i++){
        vector<int>(1000).swap(datas[i]);
    }
    int a;
    cin >> a;
    for(int i=0; i<a; i++){
        int temp;
        cin >> temp;
        datas[i/1000][i%1000] = temp;
        curdata[i] = temp;
    }
    int q,qn,w,e,r;
    for(int i=0; i<100; i++){
        sort(datas[i].begin(),datas[i].end());
    }
    cin >> q;
    for(int i=0; i<q; i++){
        cin >> qn;
        if(qn == 1){
            cin >> w>>e;
            w--;
            bool stat = false;
            for(int i=0; i<1000; i++){
                if (datas[w/1000][i] == curdata[w]){
                    datas[w/1000].erase(datas[w/1000].begin()+i);
                    stat = true;
                    break;
                }
            }
            assert (stat);
            for(int i=0; i<=1000; i++){
                if (i == 999 || datas[w/1000][i] >= e){
                    datas[w/1000].insert(datas[w/1000].begin()+i,e);
                    stat = false;
                    break;
                }
            }
            assert (!stat);
            curdata[w] = e;
        }else{
            cin >> w >> e >> r;
            int ans = 0;
            w--;
            e--;
            if(w/1000 == e/1000){
                for(int i=w; i<=e; i++){
                    ans+=curdata[i]>r;
                }
            }else{
                while(w%1000 != 0){
                    ans+=curdata[w] > r;
                    w++;
                }
                while(e%1000 != 0){
                    ans+=curdata[e] > r;
                    e--;
                }
                ans+=curdata[e]>r;
                e--;
                for(int i=w/1000; i<=e/1000; i++){
                    ans+=datas[i].end()-upper_bound(datas[i].begin(),datas[i].end(),r);
                }
            }
            cout << ans << '\n';
        }
    }
}
