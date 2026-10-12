#pragma once
#include <optional>
#include <string>

namespace owee {
std::optional<std::string> romanWordToScript(const std::string &word);
bool isRomanLetter(char c);
}
