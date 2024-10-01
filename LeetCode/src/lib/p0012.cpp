#include "leetcode.hpp"
#include <string>

std::string leetcode::Solution0012::intToRoman(int num) {
    std::string roman;

    const int thousands = num / 1000;
    num %= 1000;
    for (int i = 0; i < thousands; i++)
        roman.push_back('M');

    int hundreds = num / 100;
    num %= 100;
    switch (hundreds) {
        case 4:
            roman += "CD";
            break;
        case 9:
            roman += "CM";
            break;
        default:
            if (hundreds >= 5) {
                roman.push_back('D');
                hundreds -= 5;
            }
            for (int i = 0; i < hundreds; i++)
                roman.push_back('C');
    }

    int tens = num / 10;
    num %= 10;

    switch (tens) {
        case 4:
            roman += "XL";
        break;
        case 9:
            roman += "XC";
        break;
        default:
            if (tens >= 5) {
                roman.push_back('L');
                tens -= 5;
            }
            for (int i = 0; i < tens; i++)
                roman.push_back('X');
    }

    switch (num) {
        case 4:
            roman += "IV";
        break;
        case 9:
            roman += "IX";
        break;
        default:
            if (num >= 5) {
                roman.push_back('V');
                num -= 5;
            }
            for (int i = 0; i < num; i++)
                roman.push_back('I');
    }

    return roman;
}
