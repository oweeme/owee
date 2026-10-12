#include "oweeparser.h"
#include <algorithm>
#include <array>
#include <cctype>
#include <cstdint>
#include <unordered_map>

namespace {

std::string utf8(uint32_t cp) {
    std::string out;
    if (cp <= 0x7F) {
        out.push_back(static_cast<char>(cp));
    } else if (cp <= 0x7FF) {
        out.push_back(static_cast<char>(0xC0 | (cp >> 6)));
        out.push_back(static_cast<char>(0x80 | (cp & 0x3F)));
    } else {
        out.push_back(static_cast<char>(0xE0 | (cp >> 12)));
        out.push_back(static_cast<char>(0x80 | ((cp >> 6) & 0x3F)));
        out.push_back(static_cast<char>(0x80 | (cp & 0x3F)));
    }
    return out;
}

const std::unordered_map<std::string, uint32_t> &map() {
    static const std::unordered_map<std::string, uint32_t> m = [] {
        std::unordered_map<std::string, uint32_t> r;
        const std::array<std::string, 4> vowels = {"a","e","o","u"};
        const std::array<std::string, 14> consonants =
            {"p","b","t","d","k","g","f","s","m","n","l","r","sh","ch"};
        uint32_t cp = 0xE000;
        for (const auto &v : vowels) r[v] = cp++;
        for (const auto &c : consonants)
            for (const auto &v : vowels) r[c + v] = cp++;
        return r;
    }();
    return m;
}

bool vowel(char c) {
    return c == 'a' || c == 'e' || c == 'o' || c == 'u';
}

}

namespace owee {

bool isRomanLetter(char c) {
    c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
    return (c >= 'a' && c <= 'z');
}

std::optional<std::string> romanWordToScript(const std::string &input) {
    std::string w = input;
    std::transform(w.begin(), w.end(), w.begin(), [](unsigned char c) {
        return static_cast<char>(std::tolower(c));
    });

    std::string out;
    size_t i = 0;
    while (i < w.size()) {
        std::string syllable;

        if (vowel(w[i])) {
            syllable.push_back(w[i++]);
        } else {
            std::string c;
            if (i + 1 < w.size() &&
                (w.substr(i, 2) == "sh" || w.substr(i, 2) == "ch")) {
                c = w.substr(i, 2);
                i += 2;
            } else {
                c.push_back(w[i++]);
            }

            if (i >= w.size() || !vowel(w[i])) return std::nullopt;
            syllable = c + w[i++];
        }

        auto it = map().find(syllable);
        if (it == map().end()) return std::nullopt;
        out += utf8(it->second);
    }
    return out;
}

}
