//#define FUNCTION(name, b) int #name() {return #b;}
#define FUNCTION(name, sign) int name(int x, int y) { return (x sign y)?x:y;}
#include<iostream>
using namespace std;

FUNCTION(maximum, >);

int main() {
    
    cout << maximum(3,4);
    return 0;
}
