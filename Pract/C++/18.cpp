#include <iostream>
using namespace std;
// If else and else if works in same way as in C
int main() {
    int time = 16;

    bool isMorning = time < 12;
    bool isDay = time < 18;

    if (isMorning) {
        cout << "Good morning.";
    } 
    else if (isDay) {
        cout << "Good day.";
    } 
    else {
        cout << "Good evening.";
    }

    return 0;
}
