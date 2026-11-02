// %lf for double datatype (upto 8 characters long) (Long Float)

#include <stdio.h>
int main(){
    int a = 12e3; // e or E any thing works , this mean 12 * 10^3 = 12000
    double b = 32E3; // 32000
    printf("a+b = %lf",a+b);
    return 0;
}
