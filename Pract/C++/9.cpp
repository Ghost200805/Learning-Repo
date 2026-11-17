#include <iostream>
using namespace std;

int main() {
    int maxScore = 500;
    int userScore = 423;

    // Convert to double, so the division keeps the decimals
    double percentage = static_cast<double>(userScore) / maxScore * 100;

    // Convert to int, to get whole stars (one star for every 20 percent)
    int stars = static_cast<int>(percentage / 20);

    cout << "Score: " << percentage << "%\n";
    cout << "Stars: " << stars;
    return 0;
}
