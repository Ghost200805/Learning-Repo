#include <iostream>
using namespace std;

int main() {
    bool isCodingFun = true;
    bool isFishTasty = false;

    cout << boolalpha; // enable printing "true"/"false", without this it will print 1 (True) and 0 (False)

    cout << isCodingFun << "\n";
    cout << isFishTasty << "\n";

    cout << noboolalpha; // This is how to disable printing True and False

    cout << isCodingFun << "\n";
    cout << isFishTasty;
    return 0;
}
