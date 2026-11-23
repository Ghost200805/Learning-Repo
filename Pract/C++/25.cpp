#include <iostream>
using namespace std;

int main() {
    int myNumbers[5] = {10, 20, 30, 40, 50}; // array
  
    for (int num : myNumbers) { // Extracts each element in array , can be used in strings too
        cout << num << "\n";
    }
    return 0;
}
