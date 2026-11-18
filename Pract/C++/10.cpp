#include <iostream>
#include <string>
using namespace std;
 
int main () {
    string firstName = "John";
    string lastName = "Doe";
    string fullName = firstName + " " + lastName; // Way to concat 2 strings
    cout << fullName << "\n";

    cout<< firstName.append(lastName) << "\n"; // we can use append too fir concat

    cout << firstName.length(); // instead of length , we can also use size, its same thing.
    return 0;
}
