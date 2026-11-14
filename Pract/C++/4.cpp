#include <iostream>
using namespace std;

// Data types

int main(){
    int myNum = 5e3;               // Integer (whole number) --- 2 or 4 bytes         Can use E or e to denote 10 to the power whatever number
    float myFloatNum = 5.99;     // Floating point number --- 4 bytes
    double myDoubleNum = 9.98;   // Floating point number --- 8 bytes
    char myLetter = 'D';         // Character --- 1 byte
    bool myBoolean = true;       // Boolean --- 1 byte True mean 1 and false mean 0
    string myText = "Hello";     // String

    cout << "Integer : " << myNum;
    cout << "\nFloat : " << myFloatNum;
    cout << "\nDouble : " << myDoubleNum;
    cout << "\nChar : " << myLetter;
    cout << "\nBool : " << myBoolean;
    cout << "\nString : " << myText;
}

/*
Cout properties - 
It shows at most 6 digits in total (before and after the decimal point), and rounds the rest.
It removes zeros at the end of the decimals. If only zeros are left, the decimal point is removed too.
*/