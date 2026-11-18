#include <iostream>
#include <string>
using namespace std;

int main() {
    string x = "12";
    string y = "20";

    cout << stoi(x) + stoi(y) << "\n"; // stoi mean string to int
    
    cout << stod(x)/stod(y) << "\n"; // string to double

    int a = 5;
    string b = to_string(a); // whatever to string
    cout << b;
    return 0;
}
