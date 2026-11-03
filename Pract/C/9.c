#include <stdio.h>
int main(){
    int a = 15;
    if (a>10 && a<20){
        printf("Your age is above 10");
    }
    else if (a>20 && a<30){
        printf("Your age is above 20.");
    }
    else{
        printf("Your age is above 30.");
    }
    return 0;
}