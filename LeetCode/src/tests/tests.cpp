#include "leetcode.hpp"
#include "tests.hpp"
#include <algorithm>
#include <cstdint>
#include <stdexcept>
#include <string>
#include <vector>

int main(const int argc, char *argv[]) {
    if (argc != 2) {
        return -2;
    }

    int problem_number;
    try {
        problem_number = std::stoi(argv[1]);
    } catch (std::invalid_argument &_) {
        return -3;
    } catch (std::out_of_range &_) {
        return -4;
    } catch (...) {
        return -5;
    }

    bool test_result;
    switch (problem_number) {
        case 1:
            test_result = test_p0001();
            break;
        case 2:
            test_result = test_p0002();
            break;
        case 6:
            test_result = test_p0006();
            break;
        case 7:
            test_result = test_p0007();
            break;
        case 8:
            test_result = test_p0008();
            break;
        case 9:
            test_result = test_p0009();
            break;
        case 12:
            test_result = test_p0012();
            break;
        case 13:
            test_result = test_p0013();
            break;
        case 14:
            test_result = test_p0014();
            break;
        case 17:
            test_result = test_p0017();
            break;
        case 19:
            test_result = test_p0019();
            break;
        case 20:
            test_result = test_p0020();
            break;
        case 21:
            test_result = test_p0021();
            break;
        case 26:
            test_result = test_p0026();
            break;
        case 27:
            test_result = test_p0027();
            break;
        case 33:
            test_result = test_p0033();
            break;
        case 35:
            test_result = test_p0035();
            break;
        case 67:
            test_result = test_p0067();
            break;
        case 69:
            test_result = test_p0069();
            break;
        case 83:
            test_result = test_p0083();
            break;
        case 88:
            test_result = test_p0088();
            break;
        case 125:
            test_result = test_p0125();
            break;
        case 190:
            test_result = test_p0190();
            break;
        case 530:
            test_result = test_p0530();
            break;
        case 783:
            test_result = test_p0783();
            break;
        default:
            return -6;
    }

    return test_result ? 0 : -1;
}

bool test_p0001() {
    // Test case 1
    std::vector nums1{2, 7, 11, 15};
    constexpr int target1 = 9;

    const std::vector expected1 = {0, 1};
    std::vector<int> result1 = leetcode::Solution0001::twoSum(nums1, target1);
    std::sort(result1.begin(), result1.end());

    if (expected1 != result1) {
        return false;
    }

    // Test case 2
    std::vector<int> nums2 = {3, 2, 4};
    constexpr int target2 = 6;

    const std::vector expected2{1, 2};
    std::vector<int> result2 = leetcode::Solution0001::twoSum(nums2, target2);
    std::sort(result2.begin(), result2.end());

    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    std::vector nums3{3, 3};
    constexpr int target3 = 6;

    const std::vector expected3{0, 1};
    std::vector<int> result3 = leetcode::Solution0001::twoSum(nums3, target3);
    std::sort(result3.begin(), result3.end());

    return expected3 == result3;
}

bool test_p0002() {
    using ListNode = leetcode::Solution0002::ListNode;

    // Test case 1
    auto *l1_1 = new ListNode(2);
    l1_1->next = new ListNode(4);
    l1_1->next->next = new ListNode(3);

    auto *l2_1 = new ListNode(5);
    l2_1->next = new ListNode(6);
    l2_1->next->next = new ListNode(4);

    auto *expected1 = new ListNode(7);
    expected1->next = new ListNode(0);
    expected1->next->next = new ListNode(8);

    ListNode *result1 = leetcode::Solution0002::addTwoNumbers(l1_1, l2_1);

    while (expected1 != nullptr && result1 != nullptr) {
        if (expected1->val != result1->val) {
            return false;
        }
        expected1 = expected1->next;
        result1 = result1->next;
    }
    if (expected1 != nullptr || result1 != nullptr) {
        return false;
    }

    // Test case 2
    auto *l1_2 = new ListNode(0);
    auto *l2_2 = new ListNode(0);

    auto *expected2 = new ListNode(0);

    const ListNode *result2 = leetcode::Solution0002::addTwoNumbers(l1_2, l2_2);

    while (expected2 != nullptr && result2 != nullptr) {
        if (expected2->val != result2->val) {
            return false;
        }
        expected2 = expected2->next;
        result2 = result2->next;
    }
    if (expected2 != nullptr || result2 != nullptr) {
        return false;
    }

    // Test case 3
    auto *l1_3 = new ListNode(9);
    l1_3->next = new ListNode(9);
    l1_3->next->next = new ListNode(9);
    l1_3->next->next->next = new ListNode(9);
    l1_3->next->next->next->next = new ListNode(9);
    l1_3->next->next->next->next->next = new ListNode(9);
    l1_3->next->next->next->next->next->next = new ListNode(9);

    auto *l2_3 = new ListNode(9);
    l2_3->next = new ListNode(9);
    l2_3->next->next = new ListNode(9);
    l2_3->next->next->next = new ListNode(9);

    auto *expected3 = new ListNode(8);
    expected3->next = new ListNode(9);
    expected3->next->next = new ListNode(9);
    expected3->next->next->next = new ListNode(9);
    expected3->next->next->next->next = new ListNode(0);
    expected3->next->next->next->next->next = new ListNode(0);
    expected3->next->next->next->next->next->next = new ListNode(0);
    expected3->next->next->next->next->next->next->next = new ListNode(1);

    const ListNode *result3 = leetcode::Solution0002::addTwoNumbers(l1_3, l2_3);

    while (expected3 != nullptr && result3 != nullptr) {
        if (expected3->val != result3->val) {
            return false;
        }
        expected3 = expected3->next;
        result3 = result3->next;
    }

    return expected3 == nullptr && result3 == nullptr;
}

bool test_p0006() {
    // Test case 1
    const std::string s1 = "PAYPALISHIRING";
    constexpr int numRows1 = 3;
    const std::string expected1 = "PAHNAPLSIIGYIR";

    const std::string result1 = leetcode::Solution0006::convert(s1, numRows1);
    if (expected1 != result1) {
        return false;
    }

    // Test case 2
    const std::string s2 = "PAYPALISHIRING";
    constexpr int numRows2 = 4;
    const std::string expected2 = "PINALSIGYAHRPI";

    const std::string result2 = leetcode::Solution0006::convert(s2, numRows2);
    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    const std::string s3 = "A";
    constexpr int numRows3 = 1;
    const std::string expected3 = "A";

    const std::string result3 = leetcode::Solution0006::convert(s3, numRows3);

    return expected3 == result3;
}

bool test_p0007() {
    // Test case 1
    constexpr int x1 = 123;
    constexpr int expected1 = 321;
    const int result1 = leetcode::Solution0007::reverse(x1);
    if (expected1 != result1) {
        return false;
    }

    // Test case 2
    constexpr int x2 = -123;
    constexpr int expected2 = -321;
    const int result2 = leetcode::Solution0007::reverse(x2);
    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    constexpr int x3 = 120;
    constexpr int expected3 = 21;
    const int result3 = leetcode::Solution0007::reverse(x3);

    return expected3 == result3;
}

bool test_p0008() {
    // Test case 1
    const std::string s1 = "42";
    constexpr int expected1 = 42;
    const int result1 = leetcode::Solution0008::myAtoi(s1);
    if (expected1 != result1) {
        return false;
    }

    // Test case 2
    const std::string s2 = "   -042";
    constexpr int expected2 = -42;
    const int result2 = leetcode::Solution0008::myAtoi(s2);
    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    const std::string s3 = "1337c0d3";
    constexpr int expected3 = 1337;
    const int result3 = leetcode::Solution0008::myAtoi(s3);
    if (expected3 != result3) {
        return false;
    }

    // Test case 4
    const std::string s4 = "0-1";
    constexpr int expected4 = 0;
    const int result4 = leetcode::Solution0008::myAtoi(s4);
    if (expected4 != result4) {
        return false;
    }

    // Test case 5
    const std::string s5 = "words and 987";
    constexpr int expected5 = 0;
    const int result5 = leetcode::Solution0008::myAtoi(s5);

    return expected5 == result5;
}

bool test_p0009() {
    // Test case 1
    constexpr int x1 = 121;
    constexpr bool expected1 = true;
    const bool result1 = leetcode::Solution0009::isPalindrome(x1);
    if (expected1 != result1) {
        return false;
    }

    // Test case 2
    const int x2 = -121;
    const bool expected2 = false;
    const bool result2 = leetcode::Solution0009::isPalindrome(x2);
    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    const int x3 = 10;
    const bool expected3 = false;
    const bool result3 = leetcode::Solution0009::isPalindrome(x3);

    return expected3 == result3;
}

bool test_p0012() {
    // Test case 1
    constexpr int num1 = 3749;
    const std::string result1 = leetcode::Solution0012::intToRoman(num1);
    if (const std::string expected1 = "MMMDCCXLIX"; expected1 != result1)
        return false;

    // Test case 2
    constexpr int num2 = 58;
    const std::string result2 = leetcode::Solution0012::intToRoman(num2);
    if (const std::string expected2 = "LVIII"; expected2 != result2)
        return false;

    // Test case 3
    constexpr int num3 = 1994;
    const std::string result3 = leetcode::Solution0012::intToRoman(num3);
    if (const std::string expected3 = "MCMXCIV"; expected3 != result3)
        return false;

    return true;
}

bool test_p0013() {
    // Test case 1
    const std::string s1 = "III";
    const int result1 = leetcode::Solution0013::romanToInt(s1);
    if (constexpr int expected1 = 3; result1 != expected1)
        return false;

    // Test case 2
    const std::string s2 = "LVIII";
    const int result2 = leetcode::Solution0013::romanToInt(s2);
    if (constexpr int expected2 = 58; result2 != expected2)
        return false;

    // Test case 3
    const std::string s3 = "MCMXCIV";
    const int result3 = leetcode::Solution0013::romanToInt(s3);
    if (constexpr int expected3 = 1994; result3 != expected3)
        return false;

    return true;
}

bool test_p0014() {
    // Test case 1
    const std::vector<std::string> strs1 = {"flower", "flow", "flight"};
    const std::string result1 = leetcode::Solution0014::longestCommonPrefix(strs1);
    if (const std::string expected1 = "fl"; expected1 != result1) {
        return false;
    }

    // Test case 2
    const std::vector<std::string> strs2 = {"dog", "racecar", "car"};
    const std::string result2 = leetcode::Solution0014::longestCommonPrefix(strs2);
    if (const std::string expected2; expected2 != result2) {
        return false;
    }

    return true;
}

bool test_p0017() {
    // Test case 1
    const std::string digits1 = "23";
    std::vector<std::string> expected1 = {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"};
    std::vector<std::string> result1 = leetcode::Solution0017::letterCombinations(digits1);
    std::sort(expected1.begin(), expected1.end());
    std::sort(result1.begin(), result1.end());
    if (expected1 != result1)
        return false;

    // Test case 2
    const std::string digits2;
    constexpr std::vector<std::string> expected2;
    const std::vector<std::string> result2 = leetcode::Solution0017::letterCombinations(digits2);
    if (expected2 != result2)
        return false;

    // Test case 3
    const std::string digits3 = "2";
    std::vector<std::string> expected3 = {"a", "b", "c"};
    std::vector<std::string> result3 = leetcode::Solution0017::letterCombinations(digits3);
    std::sort(expected3.begin(), expected3.end());
    std::sort(result3.begin(), result3.end());

    return expected3 == result3;
}

bool test_p0019() {
    using ListNode = leetcode::Solution0019::ListNode;

    // Test case 1
    auto *head1 = new ListNode(1);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(3);
    head1->next->next->next = new ListNode(4);
    head1->next->next->next->next = new ListNode(5);

    auto *expected1 = new ListNode(1);
    expected1->next = new ListNode(2);
    expected1->next->next = new ListNode(3);
    expected1->next->next->next = new ListNode(5);

    head1 = leetcode::Solution0019::removeNthFromEnd(head1, 2);

    while (head1 != nullptr && expected1 != nullptr) {
        if (head1->val != expected1->val) {
            return false;
        }
        head1 = head1->next;
        expected1 = expected1->next;
    }
    if (head1 != nullptr || expected1 != nullptr) {
        return false;
    }

    // Test case 2
    auto *head2 = new ListNode(1);

    head2 = leetcode::Solution0019::removeNthFromEnd(head2, 1);

    if (const constexpr ListNode* expected2 = nullptr; head2 != expected2) {
        return false;
    }

    // Test case 3
    auto *head3 = new ListNode(1);
    head3->next = new ListNode(2);

    const auto *expected3 = new ListNode(1);

    head3 = leetcode::Solution0019::removeNthFromEnd(head3, 1);

    while (head3 != nullptr && expected3 != nullptr) {
        if (head3->val != expected3->val) {
            return false;
        }
        head3 = head3->next;
        expected3 = expected3->next;
    }

    return head3 == nullptr && expected3 == nullptr;
}

bool test_p0020() {
    // Test case 1
    const std::string s1 = "()";
    constexpr bool expected1 = true;
    const bool result1 = leetcode::Solution0020::isValid(s1);
    if (expected1 != result1) {
        return false;
    }

    // Test case 2
    const std::string s2 = "()[]{}";
    constexpr bool expected2 = true;
    const bool result2 = leetcode::Solution0020::isValid(s2);
    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    const std::string s3 = "(]";
    constexpr bool expected3 = false;
    const bool result3 = leetcode::Solution0020::isValid(s3);
    if (expected3 != result3) {
        return false;
    }

    // Test case 4
    const std::string s4 = "([])";
    constexpr bool expected4 = true;
    const bool result4 = leetcode::Solution0020::isValid(s4);

    return expected4 == result4;
}

bool test_p0021() {
    using ListNode = leetcode::Solution0021::ListNode;

    // Test case 1
    auto *l1_1 = new ListNode(1);
    l1_1->next = new ListNode(2);
    l1_1->next->next = new ListNode(4);

    auto *l2_1 = new ListNode(1);
    l2_1->next = new ListNode(3);
    l2_1->next->next = new ListNode(4);

    auto *expected1 = new ListNode(1);
    expected1->next = new ListNode(1);
    expected1->next->next = new ListNode(2);
    expected1->next->next->next = new ListNode(3);
    expected1->next->next->next->next = new ListNode(4);
    expected1->next->next->next->next->next = new ListNode(4);
    auto *result1 = leetcode::Solution0021::mergeTwoLists(l1_1, l2_1);

    while (expected1 != nullptr && result1 != nullptr) {
        if (expected1->val != result1->val) {
            return false;
        }
        expected1 = expected1->next;
        result1 = result1->next;
    }
    if (expected1 != nullptr || result1 != nullptr) {
        return false;
    }

    // Test case 2
    ListNode *l1_2 = nullptr;
    ListNode *l2_2 = nullptr;

    ListNode *expected2 = nullptr;
    auto *result2 = leetcode::Solution0021::mergeTwoLists(l1_2, l2_2);

    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    ListNode *l1_3 = nullptr;
    auto *l2_3 = new ListNode(0);

    auto *expected3 = new ListNode(0);
    auto *result3 = leetcode::Solution0021::mergeTwoLists(l1_3, l2_3);

    while (expected3 != nullptr && result3 != nullptr) {
        if (expected3->val != result3->val) {
            return false;
        }
        expected3 = expected3->next;
        result3 = result3->next;
    }

    return expected3 == nullptr && result3 == nullptr;
}

bool test_p0026() {
    auto test_func = [](std::vector<int>& nums, const std::vector<int>& expectedNums){
        const int k = leetcode::Solution0026::removeDuplicates(nums);
        if (k != static_cast<int>(expectedNums.size()))
            return false;
        for (int i = 0; i < k; i++)
            if (nums[i] != expectedNums[i])
                return false;
        return true;
    };

    // Test case 1
    std::vector nums1{1, 1, 2};
    const std::vector expectedNums1{1, 2};
    if (!test_func(nums1, expectedNums1))
        return false;

    // Test case 2
    std::vector nums2{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    const std::vector expectedNums2{0, 1, 2, 3, 4};

    return test_func(nums2, expectedNums2);
}

bool test_p0027() {
    auto test_func = [](std::vector<int>& nums, int val, std::vector<int>& expectedNums){
        const int k = leetcode::Solution0027::removeElement(nums, val);
        if (k != static_cast<int>(expectedNums.size()))
            return false;
        std::sort(nums.begin(), nums.begin() + k); // Sort the first k elements of nums
        std::sort(expectedNums.begin(), expectedNums.end());
        for (int i = 0; i < static_cast<int>(expectedNums.size()); i++) {
            if (nums[i] != expectedNums[i])
                return false;
        }
        return true;
    };

    // Test case 1
    std::vector nums1{3, 2, 2, 3};
    constexpr int val1 = 3;
    std::vector expectedNums1{2, 2};
    if (!test_func(nums1, val1, expectedNums1))
        return false;

    // Test case 2
    std::vector nums2{0, 1, 2, 2, 3, 0, 4, 2};
    constexpr int val2 = 2;
    std::vector expectedNums2{0, 1, 3, 0, 4};

    return test_func(nums2, val2, expectedNums2);
}

bool test_p0033() {
    // Test case 1
    std::vector nums1{4, 5, 6, 7, 0, 1, 2};
    constexpr int target1 = 0;
    constexpr int expected1 = 4;
    const int result1 = leetcode::Solution0033::search(nums1, target1);
    if (expected1 != result1) {
        return false;
    }

    // Test case 2
    std::vector nums2{4, 5, 6, 7, 0, 1, 2};
    constexpr int target2 = 3;
    constexpr int expected2 = -1;
    const int result2 = leetcode::Solution0033::search(nums2, target2);
    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    std::vector nums3{1};
    constexpr int target3 = 0;
    constexpr int expected3 = -1;
    const int result3 = leetcode::Solution0033::search(nums3, target3);

    return expected3 == result3;
}

bool test_p0035() {
    // Test case 1
    const std::vector nums1{1, 3, 5, 6};
    constexpr int target1 = 5;
    const int result1 = leetcode::Solution0035::searchInsert(nums1, target1);
    if (constexpr int expected1 = 2; expected1 != result1) {
        return false;
    }

    // Test case 2
    const std::vector nums2{1, 3, 5, 6};
    constexpr int target2 = 2;
    const int result2 = leetcode::Solution0035::searchInsert(nums2, target2);
    if (constexpr int expected2 = 1; expected2 != result2) {
        return false;
    }

    // Test case 3
    const std::vector nums3{1, 3, 5, 6};
    constexpr int target3 = 7;
    const int result3 = leetcode::Solution0035::searchInsert(nums3, target3);
    if (constexpr int expected3 = 4; expected3 != result3) {
        return false;
    }

    return true;
}

bool test_p0067() {
    std::string a = "1";
    std::string b = "111";
    std::string result = leetcode::Solution0067::addBinary(a, b);
    std::string expected = "1000";
    if (result != expected) {
        return false;
    }

    a = "1010";
    b = "1011";
    result = leetcode::Solution0067::addBinary(a, b);
    expected = "10101";
    return result == expected;
}

bool test_p0069() {
    // Test case 1
    constexpr int x1 = 4;
    constexpr int expected1 = 2;
    const int result1 = leetcode::Solution0069::mySqrt(x1);
    if (expected1 != result1) {
        return false;
    }

    // Test case 2
    constexpr int x2 = 8;
    constexpr int expected2 = 2;
    const int result2 = leetcode::Solution0069::mySqrt(x2);
    if (expected2 != result2) {
        return false;
    }

    // Test case 3
    constexpr int x3 = 1;
    constexpr int expected3 = 1;
    const int result3 = leetcode::Solution0069::mySqrt(x3);

    return expected3 == result3;
}

bool test_p0083() {
    using ListNode = leetcode::Solution0083::ListNode;

    // Test case 1
    auto *head1 = new ListNode(1);
    head1->next = new ListNode(1);
    head1->next->next = new ListNode(2);

    auto *expected1 = new ListNode(1);
    expected1->next = new ListNode(2);
    auto *result1 = leetcode::Solution0083::deleteDuplicates(head1);

    while (expected1 != nullptr && result1 != nullptr) {
        if (expected1->val != result1->val) {
            return false;
        }
        expected1 = expected1->next;
        result1 = result1->next;
    }
    if (expected1 != nullptr || result1 != nullptr) {
        return false;
    }

    // Test case 2
    auto *head2 = new ListNode(1);
    head2->next = new ListNode(1);
    head2->next->next = new ListNode(2);
    head2->next->next->next = new ListNode(3);
    head2->next->next->next->next = new ListNode(3);

    auto *expected2 = new ListNode(1);
    expected2->next = new ListNode(2);
    expected2->next->next = new ListNode(3);
    auto *result2 = leetcode::Solution0083::deleteDuplicates(head2);

    while (expected2 != nullptr && result2 != nullptr) {
        if (expected2->val != result2->val) {
            return false;
        }
        expected2 = expected2->next;
        result2 = result2->next;
    }
    if (expected2 != nullptr || result2 != nullptr) {
        return false;
    }

    // Test case 3
    auto *head3 = new ListNode(1);
    head3->next = new ListNode(1);
    head3->next->next = new ListNode(1);

    auto *expected3 = new ListNode(1);
    auto *result3 = leetcode::Solution0083::deleteDuplicates(head3);

    while (expected3 != nullptr && result3 != nullptr) {
        if (expected3->val != result3->val) {
            return false;
        }
        expected3 = expected3->next;
        result3 = result3->next;
    }

    return expected3 == nullptr && result3 == nullptr;
}

bool test_p0088() {
    // Test case 1
    std::vector<int> nums11{1, 2, 3, 0, 0, 0};
    constexpr int m1 = 3;
    const std::vector<int> nums21{2, 5, 6};
    constexpr int n1 = 3;
    const std::vector<int> expected1{1, 2, 2, 3, 5, 6};
    leetcode::Solution0088::merge(nums11, m1, nums21, n1);
    if (nums11 != expected1) {
        return false;
    }

    // Test case 2
    std::vector<int> nums12{1};
    constexpr int m2 = 1;
    constexpr std::vector<int> nums22;
    constexpr int n2 = 0;
    const std::vector<int> expected2{1};
    leetcode::Solution0088::merge(nums12, m2, nums22, n2);
    if (nums12 != expected2) {
        return false;
    }

    // Test case 3
    std::vector<int> nums13{0};
    constexpr int m3 = 0;
    const std::vector<int> nums23{1};
    constexpr int n3 = 1;
    const std::vector<int> expected3{1};
    leetcode::Solution0088::merge(nums13, m3, nums23, n3);
    return nums13 == expected3;
}

bool test_p0125() {
    // Test case 1
    const std::string s1{"A man, a plan, a canal: Panama"};
    if (constexpr bool expected1 = true; expected1 != leetcode::Solution0125::isPalindrome(s1))
        return false;

    // Test case 2
    const std::string s2{"race a car"};
    if (constexpr bool expected2 = false; expected2 != leetcode::Solution0125::isPalindrome(s2))
        return false;

    // Test case 3
    const std::string s3{" "};
    if (constexpr bool expected3 = true; expected3 != leetcode::Solution0125::isPalindrome(s3))
        return false;

    return true;
}

bool test_p0190() {
    // Test case 1
    constexpr uint32_t n1 = 0b00000010100101000001111010011100;
    constexpr uint32_t expected1 = 0b00111001011110000010100101000000;
    if (expected1 != leetcode::Solution0190::reverseBits(n1))
        return false;

    // Test case 2
    constexpr uint32_t n2 = 0b11111111111111111111111111111101;
    constexpr uint32_t expected2 = 0b10111111111111111111111111111111;
    return expected2 == leetcode::Solution0190::reverseBits(n2);
}

bool test_p0530() {
    // test case 1
    const leetcode::Solution0530::TreeNode *root1 = new leetcode::Solution0530::TreeNode(
        4,
        new leetcode::Solution0530::TreeNode(
            2,
            new leetcode::Solution0530::TreeNode(1),
            new leetcode::Solution0530::TreeNode(3)
        ),
        new leetcode::Solution0530::TreeNode(6)
    );
    if (leetcode::Solution0530::getMinimumDifference(root1) != 1)
        return false;

    // test case 2
    const leetcode::Solution0530::TreeNode *root2 = new leetcode::Solution0530::TreeNode(
        1,
        new leetcode::Solution0530::TreeNode(0),
        new leetcode::Solution0530::TreeNode(48, new leetcode::Solution0530::TreeNode(12), new leetcode::Solution0530::TreeNode(49))
    );
    return leetcode::Solution0530::getMinimumDifference(root2) == 1;
}

bool test_p0783() {
    // test case 1
    const leetcode::Solution0783::TreeNode *root1 = new leetcode::Solution0783::TreeNode(
        4,
        new leetcode::Solution0783::TreeNode(
            2,
            new leetcode::Solution0783::TreeNode(1),
            new leetcode::Solution0783::TreeNode(3)
        ),
        new leetcode::Solution0783::TreeNode(6)
    );
    if (leetcode::Solution0783::minDiffInBST(root1) != 1)
        return false;

    // test case 2
    const leetcode::Solution0783::TreeNode *root2 = new leetcode::Solution0783::TreeNode(
        1,
        new leetcode::Solution0783::TreeNode(0),
        new leetcode::Solution0783::TreeNode(48, new leetcode::Solution0783::TreeNode(12), new leetcode::Solution0783::TreeNode(49))
    );
    return leetcode::Solution0783::minDiffInBST(root2) == 1;
}
