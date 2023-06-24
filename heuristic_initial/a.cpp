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

// utils

template<typename T>
void print(const T& v){
    std::cout << v;
}
template<typename T>
void print(const std::vector<T>& vs){
    std::cout << "[";
    rep(i, vs.size()){
        print(vs[i]); if(i < vs.size()-1) print(",");
    }
    std::cout << "]";
}
template<class T, class... A> void print(const T& first, const A&... rest) { print(first); print(","); print(rest...); }

template<class... T>
void dprint(const T&... rest){
    std::cout << "# ";
    print(rest...);
    std::cout << "\n";
}

template<typename T>
void vprint(std::vector<T>& vs){
    for(const auto& v : vs){
        _print(v);
    }
    std::cout << std::endl;
}

double getElapsed(clk::time_point& start, clk::time_point& end){
    return (std::chrono::duration<double, std::milli>(end-start)).count() / p10_k<3>;
}

int randint(int size){
    int a = mt() % size;
    if(a<0) a += size;
    return a;
}

int randbool(){
    return mt() & 1;
}

int main(){
    dprint("score:", 50, "hoge");
    vec<int> v{1,2,3};
    vec<vec<int>> v2{{1,2},{3,4,5}};
    dprint(v,v2);
    return 0;
}
