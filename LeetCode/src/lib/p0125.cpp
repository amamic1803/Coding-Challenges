#include "leetcode.hpp"
#include <string>

bool leetcode::Solution0125::isPalindrome(std::string s) {
    int loc = 0;
    for (char c : s)
        if (isalnum(c))
            s[loc++] = c;
    s.resize(loc);

    int start = 0;
    int end = static_cast<int>(s.length() - 1);

    while (start < end)
        if (tolower(s[start++]) != tolower(s[end--]))
            return false;

    return true;
}
