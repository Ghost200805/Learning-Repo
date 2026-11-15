#include <iostream>
using namespace std;

int main(){
    int x = 10;
    int y = 3;

    cout << (x + y) << "\n"; // 13
    cout << (x - y) << "\n"; // 7
    cout << (x * y) << "\n"; // 30
    cout << (x / y) << "\n"; // 3 (integer division)
    cout << (x % y) << "\n"; // 1

    int z = 5;
    cout << ++z << "\n"; // 6
    cout << --z << "\n"; // 5
    cout << z++ << "\n";// 5
    cout << z-- << "\n"; // 6

    x<<=3; // it mean x multiply by 2 raise to 3, in short in bits three places are shifted towards left side
    cout << x <<"\n";
    x >>= 3; // vice versa , 3 bits shifted to right side, in simple words x/2^3, 80/8 = 10
    cout << x << "\n"; 

    int a = 5;
    a|=3; // Here its bitwise OR operation. In simple maths we can calculate it using result = a - (a%4) + 3
    cout << a << "\n";

    int b = 5;
    a&=5; // Here its bitwise AND operation.
    cout << b << "\n";
}