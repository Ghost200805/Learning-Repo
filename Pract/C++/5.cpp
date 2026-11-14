#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double x = 9;
    double y = 9.5;

    cout << fixed << setprecision(2); // This sets precision fixed to 2 , which means 2 decimal places will be printed always
    // if fixed not used , total of 2 numbers will be printed which mean 9.0 or 9.5
    cout << x << "\n";
    cout << y << "\n";
    return 0;
}
