// Swapping without third variable with XOR method
/*
#include <stdio.h>
int main(){
    int a = 5;
    int b = 10;
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    printf("a is %d and b is %d",a,b);
    return 0;
}
*/

//Swapping variable values without XOR
#include <stdio.h>
int main(){
    int a = 5;
    int b = 10;
    a +=b;
    b = a-b;
    a = a - b;
    printf("a is %d and b is %d",a,b);
    return 0;
}

