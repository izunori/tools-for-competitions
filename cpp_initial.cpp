#pragma GCC optimize("O3,inline")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC target("movbe")
#pragma GCC target("aes,pclmul,rdrnd")
#include<iostream>
#include<vector>
#include<string>
#include<tuple>
#include<chrono>
#include<map>
#include<set>
#include<algorithm>
#include<queue>
#include<random>
#include<numeric>
#include<functional>
#include<stack>
#include<cassert>
#include<cmath>
#include<cstring>
#include<unordered_set>
#include<unordered_map>
#include<ranges>
#include<bitset>
#include<bit>

#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define reps(i, s, n) for (int i = s; i < (int)n; i++)
#define rep2(i,j,n) for (int i = 0; i < (int)n; i++) for (int j = 0; j < (int)n; j++)
#define rep3(i,j,k,n) for (int i = 0; i < (int)n; i++) for (int j = 0; j < (int)n; j++) for (int k= 0; k < (int)n; k++)
#define all(v) v.begin(),v.end()

template<typename T>
using vec = std::vector<T>;
template<typename T>
using vec2 = vec<vec<T>>;
using ll = long long;
template<typename T>
using t2 = std::tuple<T, T>;
using i2 = std::pair<int,int>;
template<typename T>
using t3 = std::tuple<T, T, T>;
using i3 = t3<int>;
using clk = std::chrono::system_clock;

// global

std::random_device rnd;
std::mt19937 mt(rnd());
std::uniform_real_distribution<> rand01(0.0, 1.0);

// utils

template<typename T> void print(const T& v){ std::cout << v; }
template<typename... T> void print(const std::tuple<T...>& tp);
template<typename T>
void print(const std::vector<T>& vs){
    std::cout << "[";
    rep(i, vs.size()){
        if(i > 0) print(" ");
        print(vs[i]);
    }
    std::cout << "]";
}
template<typename TupType, size_t... I>
void print(const TupType& tp, std::index_sequence<I...>){
    std::cout << "(";
    (..., (print(I==0? "" : " "), print(std::get<I>(tp))));
    std::cout << ")";
}
template<typename... T>
void print(const std::tuple<T...>& tp){
    print(tp, std::make_index_sequence<sizeof...(T)>());
}
template<class T, class... A> void print(const T& first, const A&... rest) { print(first); print(" "); print(rest...); }
template<class... T>
void dprint(const T&... rest){
    std::cout << "# ";
    print(rest...);
    std::cout << "\n";
}

template<typename T>
vec<T> LI(int n){
    vec<T> res;
    rep(i,n){
        T x; std::cin >> x; res.push_back(x);
    }
    return res;
}

template<typename T>
vec<T> LI2(int n, int m){
    vec2<T> res;
    rep(i,n) res.emplace_back(LI<T>(m));
    return res;
}

// main

int main(){
    return 0;
}
