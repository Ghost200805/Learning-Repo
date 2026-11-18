#include <iostream>
#include <string>
using namespace std;

int main() {
    string myString = "Hello";
    cout << myString[myString.length() - 1] << "\n"; // string slicing and printing in reverse

    cout << myString.at(3) << "\n"; // we can use at also for slicing , it does the same thing

    myString.at(0) = 'J'; // changing data at index 0
    cout << myString;

    return 0;
}
