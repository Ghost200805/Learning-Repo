#include <stdio.h>

int main() {
  // Create variables
  int myNum = 15;              // Integer (whole number)
  float myFloatNum = 5.99;     // Floating point number
  char myLetter = 'D';         // Character
  
  // Print variables
  printf("%d\n", myNum);
  printf("%.2f\n", myFloatNum); // %f normally but %.2f mean- till 2 decimal places...
  printf("%c\n", myLetter);
  return 0;
}