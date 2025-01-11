// aryan053
// stand proud, you're strong
 
#include <bits/stdc++.h>
 
#define inf 1e18
#define pb push_back
#define popb pop_back
#define fi first
#define se second
#define sll set<long long>
#define vll vector<long long>
#define ll long long int
#define pll pair<long long,long long>
#define vp vector<pair<long long,long long>>
#define umpll unordered_map<long long,long long>
#define mpll map<long long>
#define maxpq priority_queue<long long>
#define minpq priority_queue<long long, vector<long long>, greater<long long>>
#define dq deque<long long>
#define qu queue<long long>
#define st stack<long long>
#define ms multiset<long long>
#define usll unordered_set<long long>
 
#define mod 1000000007
#define clr(a) memset(a, 0, sizeof(a))
#define sz(x) x.size()
#define rep(n) for (ll i = 0; i < n; i++)
#define myfor(i, x, y) for (int i = x; i < y; i++)
#define mydec(i, x, y) for (int i = x; i >= y; i--)
#define all(v) v.begin(), v.end()
#define min3(a, b, c) min(a, min(b, c))
#define max3(a, b, c) max(a, max(b, c))
#define end "\n"
 
#define MOD 998244353
 
using namespace std;

bool check(ll n) {
    if (n % 2 != 0 && n % 3 != 0 && n % 5 != 0) {
        return false;
    }
    return true;
}

void solve() {
    int q;
    cin >> q;

    while (q--) {
        ll n;
        cin >> n;

        int cnt = 0;

        while (n != 1) {
            if (check(n) == false) {
                cnt = -1;
                break;
            }
            if (n%2 == 0) {
                n /= 2;
            } else if (n % 3 == 0) {
                n = (2*n)/3;
            } else if (n % 5 == 0) {
                n = (4*n)/5;
            }
            cnt += 1;
        }

        cout << cnt << end;
    }
}
 
int main(){
    solve();
}