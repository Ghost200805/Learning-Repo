#include <stdio.h>
#include <string.h>
 
int main() {
  char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  printf("%zu\n", strlen(alphabet));   // 26, this function doesnt count \0 at end (added by default by c)
  printf("%zu\n", sizeof(alphabet));   // 27 , its +1 because at last by default c does \0 which increases size by 1
  return 0;
}