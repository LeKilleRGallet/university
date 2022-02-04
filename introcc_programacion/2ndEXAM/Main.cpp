#include <iostream>
using namespace std;

int sumDigits(int n){
    int sum = 0;
    while (n > 0){
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int primenumber(int n){
    if (n < 2 ){return 0;}
    for (int i = 2; i < n; i++){
        if ((n != 2) && (n % i == 0)){
            return 0;}
    }
    return 1;
}


int main(){

    int floor, ceil;
    cin >> floor;
    cin >> ceil;
    for (int i = floor; i <= ceil; i++){
        if (primenumber(i) == 1){
            int primeDigits = sumDigits(i);
            if (primenumber(primeDigits) == 1){
                cout << i << endl;
            }


        }
    }

    return 0;
}