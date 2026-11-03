// Boolean Operators return 0 and 1
#include <stdbool.h>
#include <stdio.h>
int main(){
    bool x = true;
    bool y = false;
    int a = 10;
    const int z  = 25; // Const mean that the values inside this variable cannot be changed. If tried, throws error.
    int b = 20;
    printf("%d\n",a>b); // 0 mean True , 1 mean false
    printf("%d\n",b>a);
    printf("%d\n",x);
    printf("%d",y);
    return 0;
}