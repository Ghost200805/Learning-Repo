#include <stdio.h>

int main() {
    int myNumbers[2] = {1, 2};
    char letters[] = "Hi"; // 'H', 'i', '\0'

    int *pi = myNumbers;   // int pointer
    char *pc = letters;    // char pointer

    printf("%p\n", pi);
    printf("%p\n", pi + 1); // moves by sizeof(int)
    printf("%p\n", pi + 2);

    printf("%p\n", pc);
    printf("%p\n", pc + 1); // moves by 1 byte
    return 0;
}