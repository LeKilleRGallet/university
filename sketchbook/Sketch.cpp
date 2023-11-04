#include <iostream>
using namespace std;

void increase(void* data, int psize){
    if (psize == sizeof(char))
        {char* pchar;
        pchar = (char*)data;
        ++(*pchar);}
    else if (psize == sizeof(int))
        {int* pint;
        pint== (int*)data;
        ++(*pint);}
    
}


int main(){
    char c = 'a';
    int i = 1;
    increase(&c, sizeof(c));
    increase(&i, sizeof(i));
    cout << c << " " << i << endl;
    return 0;
}