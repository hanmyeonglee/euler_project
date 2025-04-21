#include <iostream>

int reverse(int n) {
    int reversed_n = 0;
    while (n > 0) {
        reversed_n = reversed_n * 10 + n % 10;
        n /= 10;
    }

    return reversed_n;
}

bool isReversible(int n) {
    while (n > 0)
    {
        int digit = n % 10;
        if (digit % 2 == 0) return false;
        n /= 10;
    }
    
    return true;
}

int main() {
    int cnt = 0;
    for (size_t n = 1 ; n <= 1000000000 ; n++) {
        if (n % 10 == 0) continue;
        int rn = reverse(n);
        if (isReversible(n + rn)) cnt++;
    }

    std::cout << cnt << std::endl;
}