#include "leetcode.hpp"
#include <cctype>
#include <string>

bool leetcode::Solution0125::isPalindrome(std::string s) {
    int loc = 0;
    for (const char c : s)
        if (std::isalnum(c))
            s[loc++] = c;
    s.resize(loc);

    int start = 0;
    int end = static_cast<int>(s.length() - 1);

    while (start < end)
        if (std::tolower(s[start++]) != std::tolower(s[end--]))
            return false;

    return true;
}
