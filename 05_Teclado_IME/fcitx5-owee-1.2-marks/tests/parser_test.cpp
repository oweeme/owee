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
    // compuestos y nombres propios (1.2)
    auto j = owee::romanWordToScript("sade-kelo");
    assert(j && j->find("\xEE\x80\xBC") != std::string::npos);        // U+E03C
    auto n = owee::romanWordToScript("Ana");
    assert(n && n->rfind("\xEE\x80\xBD", 0) == 0);                    // U+E03D al inicio
    assert(!owee::romanWordToScript("sade-"));
    assert(!owee::romanWordToScript("sade-mi"));
    std::cout << "Owee parser: OK\n";
}
