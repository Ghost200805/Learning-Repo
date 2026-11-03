// While and do while

/*
#include <stdio.h>

int main() {
    int i = 0;
    
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
*/

#include <stdio.h>

int main() {
    int i = 10;
    
    do {
        printf("%d\n", i);
        i++;
    }
    while (i < 5);
    return 0;
}