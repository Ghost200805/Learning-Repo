#include <iostream>
using namespace std;

int main() {
    int i = 0;
    while (i < 10) {
        if (i%3==0){
            i++;
            continue;
        }
        cout << i << "\n";
        i++;
        if (i == 4) {
            break;
        }
    } 
    return 0;
}
