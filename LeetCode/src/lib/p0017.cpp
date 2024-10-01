#include "leetcode.hpp"
#include <string>
#include <unordered_map>
#include <vector>

std::vector<std::string> leetcode::Solution0017::letterCombinations(const std::string& digits) {
    if (digits.empty())
        return {};

    std::unordered_map<char, std::string> digit_2_characters = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"},
    };
    std::vector<std::string> combinations;
    std::string working_string;

    generateCombinations(digits, 0, working_string, combinations, digit_2_characters);

    return combinations;
}

void leetcode::Solution0017::generateCombinations(
    const std::string& digits,
    const int index,
    std::string &working_string,
    std::vector<std::string> &combinations,
    std::unordered_map<char, std::string> &digit_2_characters)
{
    if (index == digits.size()) {
        combinations.push_back(working_string);
    } else {
        for (const char c : digit_2_characters[digits[index]]) {
            working_string.push_back(c);
            generateCombinations(digits, index + 1, working_string, combinations, digit_2_characters);
            working_string.pop_back();
        }
    }
}
