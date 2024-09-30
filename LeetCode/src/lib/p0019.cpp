#include "leetcode.hpp"

using ListNode = leetcode::Solution0019::ListNode;

ListNode* leetcode::Solution0019::removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy_head(0, head);
    const ListNode* current_node = &dummy_head;
    for (int i = 0; i < n + 1; i++) {
        current_node = current_node->next;
    }
    ListNode* node_before_nth = &dummy_head;
    while (current_node != nullptr) {
        current_node = current_node->next;
        node_before_nth = node_before_nth->next;
    }
    const ListNode* node_to_remove = node_before_nth->next;
    node_before_nth->next = node_to_remove->next;
    delete node_to_remove;
    return dummy_head.next;
}
