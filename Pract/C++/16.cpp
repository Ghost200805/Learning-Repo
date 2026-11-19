#include <iostream>
using namespace std;

int main() {
    bool isCodingFun = true;
    bool isFishTasty = false;

    cout << boolalpha; // enable printing "true"/"false", without this it will print 1 (True) and 0 (False)

    cout << isCodingFun << "\n";   // Outputs true
    cout << isFishTasty << "\n";  // Outputs false
    return 0;
}
