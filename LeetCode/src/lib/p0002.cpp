#include "leetcode.hpp"

using ListNode = leetcode::Solution0002::ListNode;

ListNode* leetcode::Solution0002::addTwoNumbers(ListNode* l1, ListNode* l2) {
    auto *dummy_head = new ListNode();

    auto *result = dummy_head;
    bool carry = false;
    while (l1 != nullptr || l2 != nullptr) {
        int sum = 0;
        if (l1 != nullptr) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != nullptr) {
            sum += l2->val;
            l2 = l2->next;
        }
        if (carry) {
            sum++;
        }
        carry = sum >= 10;
        result->next = new ListNode(sum % 10);
        result = result->next;
    }
    if (carry) {
        result->next = new ListNode(1);
    }

    auto *result_head = dummy_head->next;
    delete dummy_head;

    return result_head;
}
