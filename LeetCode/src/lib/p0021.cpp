#include "leetcode.hpp"

using ListNode = leetcode::Solution0021::ListNode;

ListNode* leetcode::Solution0021::mergeTwoLists(ListNode* list1, ListNode* list2) {
    auto dummy_head = new ListNode();
    auto current_node = dummy_head;

    while (list1 != nullptr && list2 != nullptr) {
        if (list1->val < list2->val) {
            current_node->next = list1;
            current_node = current_node->next;
            list1 = list1->next;
        } else {
            current_node->next = list2;
            current_node = current_node->next;
            list2 = list2->next;
        }
    }

    if (list1 != nullptr) {
        current_node->next = list1;
    }
    if (list2 != nullptr) {
        current_node->next = list2;
    }

    auto head = dummy_head->next;
    delete dummy_head;

    return head;
}
