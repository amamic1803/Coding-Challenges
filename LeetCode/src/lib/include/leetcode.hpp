#ifndef LEETCODE_LIB_HPP
#define LEETCODE_LIB_HPP

#include <string>
#include <vector>

namespace leetcode {
    class Solution0001 {
    public:
        static std::vector<int> twoSum(std::vector<int>& nums, int target);
    };

    class Solution0002 {
    public:
        // Definition for singly-linked list.
        struct ListNode {
            int val;
            ListNode *next;
            ListNode() : val(0), next(nullptr) {}
            explicit ListNode(int x) : val(x), next(nullptr) {}
            ListNode(int x, ListNode *next) : val(x), next(next) {}
        };
        static ListNode* addTwoNumbers(ListNode* l1, ListNode* l2);
    };

    class Solution0006 {
    public:
        static std::string convert(std::string s, int numRows);
    };

    class Solution0007 {
    public:
        static int reverse(int x);
    };

    class Solution0008 {
    public:
        static int myAtoi(std::string s);
    };

    class Solution0009 {
    public:
        static bool isPalindrome(int x);
    };

    class Solution0020 {
    public:
        static bool isValid(const std::string& s);
    };

    class Solution0021 {
    public:
        // Definition for singly-linked list.
        struct ListNode {
            int val;
            ListNode *next;
            ListNode() : val(0), next(nullptr) {}
            explicit ListNode(int x) : val(x), next(nullptr) {}
            ListNode(int x, ListNode *next) : val(x), next(next) {}
        };

        static ListNode* mergeTwoLists(ListNode* list1, ListNode* list2);
    };
}

#endif // LEETCODE_LIB_HPP
