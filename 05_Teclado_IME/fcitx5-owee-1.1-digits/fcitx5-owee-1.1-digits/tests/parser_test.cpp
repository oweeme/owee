#include "../src/oweeparser.h"
#include <cassert>
#include <iostream>
int main() {
    assert(owee::romanWordToScript("me"));
    assert(owee::romanWordToScript("suna"));
    assert(owee::romanWordToScript("daro"));
    assert(owee::romanWordToScript("dare"));
    assert(owee::romanWordToScript("sha"));
    assert(owee::romanWordToScript("chu"));
    assert(!owee::romanWordToScript("mi"));   // i does not exist in Owee
    assert(!owee::romanWordToScript("str"));
    std::cout << "Owee parser: OK\n";
}
