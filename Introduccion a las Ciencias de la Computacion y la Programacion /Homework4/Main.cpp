#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

// return the time for duplicate money for a interes rate(x)

int main(){
    int i, m;
    double x;
    cin >> x;
    for(i=0;m<2;++i)
    {
        m=pow(1+x,i);
        if (m>=2)
        {
            cout << i << endl;
            break;
        }
    }
    return 0;
}

