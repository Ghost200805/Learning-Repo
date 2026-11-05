#include <stdio.h>
#include <ctype.h>

int main() {
    char ch = 'A';

    // 1. Check if it is a letter
    if (isalpha(ch)) {
        printf("%c is an alphabet letter\n", ch);
    }

    // 2. Check if it is a digit
    if (isdigit(ch)) {
        printf("%c is a digit\n", ch);
    }

    // 3. Check if it is alphanumeric (letter or number)
    if (isalnum(ch)) {
        printf("%c is alphanumeric\n", ch);
    }

    // 4. Check if it is uppercase
    if (isupper(ch)) {
        printf("%c is uppercase\n", ch);
    }

    // 5. Check if it is lowercase
    if (islower(ch)) {
        printf("%c is lowercase\n", ch);
    }

    // 6. Check if it is a whitespace character
    if (isspace(ch)) {
        printf("%c is a whitespace character\n", ch);
    }

    printf("%c\n",toupper(ch));
    printf("%c",tolower(ch));

    return 0;
}