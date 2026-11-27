#include <iostream>
#include <string>
using namespace std;

int main() {
    string food = "Pizza";       // food variable
    string &meal = food;         // reference to food

    meal = "Burger";             // change the reference

    cout << food << "\n";        
    cout << meal << "\n";     
    cout << &food; // To get Memory place   
    return 0;
}
