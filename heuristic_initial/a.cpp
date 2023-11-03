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

#define rep(i, n) for (int i = 0; i < (int)n; i++)
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
using i2 = t2<int>;
template<typename T>
using t3 = std::tuple<T, T, T>;
using clk = std::chrono::system_clock;

template<int k>
constexpr double p10_k = std::pow(10, k);

// global

constexpr bool local = false;
std::map<std::string, std::string> LOG;

std::random_device rnd;
std::mt19937 mt(rnd());
std::uniform_real_distribution<> rand01(0.0, 1.0);

clk::time_point start_time;

// utils

template<typename T>
void print(const T& v){
    std::cout << v;
}
template<typename... T>
void print(const std::tuple<T...>& tp);
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
void vprint(std::vector<T>& vs){
    for(const auto& v : vs){
        std::cout << v << " ";
    }
    std::cout << std::endl;
}

double getElapsed(clk::time_point& start, clk::time_point& end){
    return (std::chrono::duration<double, std::milli>(end-start)).count() / p10_k<3>;
}

vec<int> range(int n){
    vec<int> v(n);
    std::iota(all(v), 0);
    return v;
}

int randint(int size){
    int a = mt() % size;
    if(a<0) a += size;
    return a;
}

vec<int> sample(int mx, int num){
    vec<int> res;
    while(res.size() < num){
        res.emplace_back(randint(mx));
        std::sort(all(res));
        auto unique_end = std::unique(all(res));
        res.erase(unique_end, res.end());
    }
    return res;
}

int randbool(){
    return mt() & 1;
}

template<typename T>
vec<int> getOrderOf(vec<T>& v){
    auto res = range(v.size());
    std::sort(all(res),
        [&](int x, int y){return v[x] < v[y];}
    );
    return res;
}

// functions

void initialize(){
}
void deconstruct(){
}

// main

int main(){
    initialize();
    deconstruct();
    return 0;
}
