#include <iostream>
using namespace std;

// auto simply decides its datatype as per the value inside variable

int main(){
    auto x = 5; // x is now an int
    x = 10;     // OK - still an int
    x = 9.99;   // Still an int, so x is now 9

    cout << x;
}