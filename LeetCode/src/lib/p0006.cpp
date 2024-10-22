#include "leetcode.hpp"
#include <string>
#include <vector>

std::string leetcode::Solution0006::convert(std::string s, int numRows) {
    if (numRows == 1) {
        return s;
    }

    auto rows_strings = std::vector<std::string>(numRows);
    for (int i = 0; i < numRows; ++i) {
        rows_strings[i] = "";
    }

    int i = 0;
    int direction = 1;
    for (const char c : s) {
        rows_strings[i] += c;
        i += direction;
        if (i == 0 || i == numRows - 1) {
            direction *= -1;
        }
    }

    std::string result;
    for (const std::string& row_string : rows_strings) {
        result += row_string;
    }

    return result;
}
