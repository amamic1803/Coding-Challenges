#include "leetcode.hpp"
#include <stack>
#include <string>

bool leetcode::Solution0020::isValid(const std::string& s) {
    auto stack = std::stack<char>();

    for (const char c : s) {
        switch (c) {
            case '(':
            case '[':
            case '{':
                stack.push(c);
                break;
            case ')':
                if (stack.empty() || stack.top() != '(') {
                    return false;
                }
                stack.pop();
                break;
            case ']':
                if (stack.empty() || stack.top() != '[') {
                    return false;
                }
                stack.pop();
                break;
            case '}':
                if (stack.empty() || stack.top() != '{') {
                    return false;
                }
                stack.pop();
                break;
            default:
                return false;
        }
    }

    return stack.empty();
}
