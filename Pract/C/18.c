#include <stdio.h>
#include <string.h>

int main() {
    char carName[] = "Volvo";
    int length = strlen(carName); // Can use strlen function with including string.h header file instead of calculating length by yourself using for loop..
    int i;
    
    for (i = 0; i < length; ++i) {
        printf("%c\n", carName[i]);
    }

    return 0;
}