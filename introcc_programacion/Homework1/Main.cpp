#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    float Papa;
    float Carlos;
    float Jose;
    float Martha;
    cin>>Papa;
    Carlos = Papa*1/3;
    Jose = Carlos*4/3;
    Martha = Jose*1/2;
    printf("Carlos:	$%0.2f\nJose:	$%0.2f\nMartha:	$%0.2f\n", Carlos, Jose, Martha);
    return 0;
}