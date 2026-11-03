#include <stdio.h>

int main() {
  int myNumbers[] = {3, -1, 7, 0, 9}; // Array
  int length = sizeof(myNumbers) / sizeof(myNumbers[0]); // 20 bytes divide by 4 bytes = 5
  int i;

  for (i = 0; i < length; i++) {
    if (myNumbers[i] < 0) {
      continue;
    }
    if (myNumbers[i] == 0) {
      break; 
    }
    printf("%d\n", myNumbers[i]);
  }  
  
  return 0;
}