#include <bits/stdc++.h>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef long long ll;
typedef vector<long long> vl;
typedef vector<vector<long long>> vvl;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;
typedef vector<vector<pair<int, int>>> vvpii;
typedef pair<long long, long long> pll;
typedef vector<pair<long long, long long>> vpll;
typedef vector<vector<pair<long long, long long>>> vvpll;
typedef vector<bool> vb;
typedef vector<vector<bool>> vvb;
typedef vector<string> vs;
typedef vector<vector<string>> vvs;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, b) for(auto &a : b)
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define deb(x) cout << endl << #x << ": " << x << endl
#define deb2(x, y) cout << endl << #x << ": " << x << ", " << #y << ": " << y << endl
#define deb3(x, y, z) cout << endl << #x << ": " << x << ", " << #y << ": " << y << ", " << #z << ": " << z << endl
#define debP(p) cout << endl << #p << ": " << p.first << ", " << p.second << endl
#define debArr(x) cout << endl << #x << ": "; rep(abc, 0, x.size()) cout << x[abc] << " "
#define el cout << endl
#define sz(x) x.size()

//number &= ~(1UL << n);            -Turn off bit
//number |= (1UL << n);             -Turn on bit
//number ^= (1UL << n);             -Toggle bit
//bool on = (number & (1UL << n)    -whether the n-th (0-indexed) bit is on or off

vi rates;
map<int, int> relevant_valves;
int MINUTES = 26;
vector<vvi> DP;
ll c = 0;
int num_valves = 0;
vvi G;

ifstream infile("in.txt");

int get_bitmask_pos(int valve) {
    return 1 << relevant_valves[valve];
}

bool valve_opened(int valve, int bitmask) {
    return bitmask & (1 << relevant_valves[valve]);
}

int current_left;
int num_possible_opens;
int dp(int valve1, int valve2, int left, int bitmask) {
    if (left == 0) return 0;

    int key = valve1 * num_valves + valve2;
    if (DP[current_left - left][bitmask][key] != -1) return DP[current_left - left][bitmask][key];

    int best = -1;
    trav(nei1, G[valve1]) {
        trav(nei2, G[valve2]) {
            best = max(best, dp(nei1, nei2, left - 1, bitmask));
        }
    }
    // G^2
    
    if (__builtin_popcount(bitmask) + 1 <= num_possible_opens) {
        if (relevant_valves.find(valve2) != relevant_valves.end()) {
            if (!valve_opened(valve2, bitmask)) {
                trav(nei1, G[valve1]) {
                    best = max(best, rates[valve2] * (left - 1) + 
                        dp(nei1, valve2, left - 1, bitmask | get_bitmask_pos(valve2)));
                }
            }
        }
    }
    // G

    if (__builtin_popcount(bitmask) + 1 <= num_possible_opens) {
        if (relevant_valves.find(valve1) != relevant_valves.end()) {
            if (!valve_opened(valve1, bitmask)) {
                trav(nei2, G[valve2]) {
                    best = max(best, rates[valve1] * (left - 1) + 
                        dp(valve1, nei2, left - 1, bitmask | get_bitmask_pos(valve1)));
                }
            }
        }
    }
    // G
    
    if (__builtin_popcount(bitmask) + 2 <= num_possible_opens) {
        if (valve1 != valve2) {
            if (relevant_valves.find(valve1) != relevant_valves.end()) {
                if (relevant_valves.find(valve2) != relevant_valves.end()) {
                    if (!valve_opened(valve1, bitmask)) {
                        if (!valve_opened(valve2, bitmask)) {
                            best = max(best, rates[valve1] * (left - 1) + rates[valve2] * (left - 1) + dp(valve1, valve2, left - 1, bitmask | get_bitmask_pos(valve1) | get_bitmask_pos(valve2)));
                        }
                    }
                }
            }
        }
    }
    // 1

    DP[current_left - left][bitmask][key] = best;
    return best;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    map<string, int> to_index;
    string line;
    int N = 54;
    G.resize(N, vi());
    rates.resize(N);
    while (getline(infile, line)) {
        istringstream iss(line);
        string node = line.substr(6, 2);
        int rate_start = line.find("=") + 1;
        int rate_stop = line.find(";");
        string rate_str = line.substr(rate_start, rate_stop - rate_start);
        int rate = stoi(rate_str);
        int others_start = line.find("valves");
        if (others_start == -1) {
            others_start = line.find("valve");
            others_start += 6;
        }else {
            others_start += 7;
        }
        vs others;
        int i = others_start;
        while (i < line.length()) {
            others.pb(line.substr(i, 2));
            i += 4;
        }

        if (to_index.find(node) == to_index.end()) {
            to_index[node] = to_index.size();
        }

        rates[to_index[node]] = rate;
        trav(other, others) {
            if (to_index.find(other) == to_index.end()) {
                to_index[other] = to_index.size();
            }
            G[to_index[node]].pb(to_index[other]);
        }
        if (rate) {
            relevant_valves[to_index[node]] = relevant_valves.size();
        }
    }

    num_valves = to_index.size();
    DP.resize(2, vvi(1 << 16, vi(num_valves * num_valves, -1)));
    rep(left, 1, MINUTES + 1) {
        current_left = left;
        int minutes_gone = MINUTES - left;
        num_possible_opens = minutes_gone / 2 + 1;
        rep(valve1, 0, num_valves) {
            rep(valve2, 0, num_valves) {
                c += 1;
                if (c % 10 == 0) {
                    float fraction = (double)c / (double)(num_valves * num_valves * MINUTES);
                    cout << round(fraction * 10000) / 100 << "%" << endl;
                }
                rep(bitmask, 0, 1 << 16) {
                    if (__builtin_popcount(bitmask) > num_possible_opens) continue;
                    dp(valve1, valve2, left, bitmask);
                }
            }
        }
        swap(DP[0], DP[1]);
        rep(i, 0, num_valves * num_valves) {
            rep(j, 0, 1 << 16) {
                DP[0][j][i] = -1;
            }
        }
    }
    cout << endl << DP[1][0][to_index["AA"] * num_valves + to_index["AA"]] << endl;
}