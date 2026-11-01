/*
Memory sizes -
int - 2 or 4 bytes
float - 4 bytes
double - 8 bytes
char - 1 byte
*/

#include <stdio.h>
int main(){
    int a;
    float b;
    char c;
    double d;
    char f[10];
    printf("size of int a %zu\n", sizeof(a));
    printf("size of float b %zu\n", sizeof(b));
    printf("size of char c %zu\n", sizeof(c));
    printf("size of double d %zu\n", sizeof(d));
    printf("size of char f[10] %zu\n", sizeof(f));
}