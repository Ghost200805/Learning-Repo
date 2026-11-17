#include <iostream>
#include <string>
using namespace std;
 
int main () {
    string firstName = "John";
    string lastName = "Doe";
    string fullName = firstName + " " + lastName; // Way to concat 2 strings
    cout << fullName << "\n";

    cout<< firstName.append(lastName); // we can use append too fir concat
    return 0;
}
