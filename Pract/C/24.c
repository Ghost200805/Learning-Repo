#include <stdio.h>

int main() {
    int myNum;
    char myChar;
    int n = 43;

    printf("Type a number AND a character and press enter: \n");

    scanf("%d %c", &myNum, &myChar); // Getting user input

    printf("Your number is: %d\n", myNum);

    printf("Your character is: %c\n", myChar);
    
    printf("%p",n); // To print memory address

    return 0;
}
