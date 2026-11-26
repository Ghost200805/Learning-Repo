#include <iostream>
using namespace std;
 
enum Level {
    LOW = 1, // can add value (not compulsory)
    MEDIUM,
    HIGH
};

int main() {
    enum Level myVar = MEDIUM;

    switch (myVar) {
        case 1:
            cout << "Low Level : " << myVar;
            break;
        case 2:
            cout << "Medium level";
            break;
        case 3:
            cout << "High level";
            break;
    }
    return 0;
}
