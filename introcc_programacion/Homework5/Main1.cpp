#include <iostream>
#include <cstdio>
using namespace std;

int squaresum(int n){
    if (n>=1){
        return (n*n+squaresum(n-1));
    } else {
        return 0;
    }
}

int main(){


    int n;
    cin >> n;
    n=squaresum(n);
    
    cout<<n<<endl;
    return 0;
}