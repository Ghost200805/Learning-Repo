// Reverse number

#include <stdio.h>
int main(){
    int a = 1234;
    int b;
    while (a>0){
        b = b*10 + a%10;
        a/=10;
    }
    printf("Reverse number : %d",b);
    return 0;
}