#include<iostream>
#include<vector>
#include<cmath>
#include<cstdint>
#include<algorithm>
#include<boost/range/irange.hpp>
#define PRINT(text) (std::cout << (text) << std::endl);
#define VPRINT(vec) for(const auto& x:vec){std::cout << x << ' ';};
template<typename T>
void for_each(std::vector<T> &vec, std::function<T(T)> &f){
    std::for_each(vec.cbegin(), vec.cend(), f);
}
template<typename T>
T pow(T p, T n, T m){
    T res = 1;
    while(n){
        if(n&1) res = (res*p)%m;
        p = (p*p)%m;
        n >>= 1;
    }
    return res;
}
template<typename T>
inline auto range(T first, T last=-1, T step = 1){
    if(last == -1){
        return boost::irange(0, first, step);
    } else {
        return boost::irange(first, last, step);
    }
}

int main(){
    std::cin >> N >> X >> Y >> Z;
    return 0;
}
