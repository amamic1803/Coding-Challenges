#include "leetcode.hpp"

using ListNode = leetcode::Solution0083::ListNode;

ListNode* leetcode::Solution0083::deleteDuplicates(ListNode* head) {
    if (head == nullptr)
        return nullptr;

    ListNode* last_node = head;
    ListNode* current_node = head->next;

    while (current_node != nullptr) {
        if (current_node->val == last_node->val) {
            last_node->next = current_node->next;
            delete current_node;
        } else {
            last_node = current_node;
        }
        current_node = last_node->next;
    }

    return head;
}
