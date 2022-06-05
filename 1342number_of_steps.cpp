#include <iostream>
using namespace std;

// Compiled on Debian (WSL) using:
// g++ -o 1342number_of_steps 1342number_of_steps.cpp

class Solution {
public:
    int numberOfSteps(int num) {
        int steps = 0;
        while(num != 0) {
            if(num % 2 == 0) {
                steps++;
                num = num / 2;
            }
            else {
                steps++;
                num -= 1;
            }
        }
        return steps;     
    }
};

int main(int argc, char *argv[]) {
    Solution sl;
    cout << sl.numberOfSteps(16) << '\n';
}