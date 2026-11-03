#include <stdio.h>
int main(){
    int a = 1;
    int b = 0;
    printf("%d\n",a && b); // And 
    printf("%d\n",a || b); // Or
    printf("%d\n", !(a && b)); // NAND
    printf("%d",!(a || b)); // NOR
    return 0;
}