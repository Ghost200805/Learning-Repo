#include <stdio.h>
#include <string.h>

int main() {
    char fruits[3][10] = {"Apple", "Banana", "Cherry"};

    strcpy(fruits[0], "Mango"); // To change values at specific indexes in an array
    printf("%s\n", fruits[0]);
    return 0;
}