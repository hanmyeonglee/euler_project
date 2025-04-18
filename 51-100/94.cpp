#include <iostream>
#include <cmath>

using namespace std;
bool verify(int s, int b) {
    if (s % 2 == 0) return false;
    int half = b / 2;

    long value = (long)s * s - (long)half * half;
    long height = static_cast<int>(sqrt(value));
    
    return height * height == value;
}

int main() {
    long sum = 0;
    for (int i = 2 ; i <= 333333334 ; i++) {
        int b1 = i - 1;
        int b2 = i + 1;
        int per1 = 2 * i + b1;
        int per2 = 2 * i + b2;
        if (per1 <= 1000000000 && verify(i, b1)) sum += per1;
        if (per2 <= 1000000000 && verify(i, b2)) sum += per2;
    }
    cout << sum << endl;
}