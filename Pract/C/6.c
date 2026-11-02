#include <stdio.h>

int main() {
    int normalInt = 1000;
    double normalDouble = 3.14; 

    short int small = -100;
    unsigned int count = 25;
    long int big = 1234567890;
    long long int veryBig = 9223372036854775807;
    unsigned long long int huge = 18446744073709551615U;
    long double precise = 3.141592653589793238L;

    printf("Normal int: %d\n", normalInt);
    printf("Normal double: %lf\n", normalDouble);
    printf("Small: %hd\n", small);
    printf("Count: %u\n", count);
    printf("Big: %ld\n", big);
    printf("Very Big: %lld\n", veryBig);
    printf("Huge: %llu\n", huge);
    printf("Precise: %.18Lf\n", precise);
    return 0;
}