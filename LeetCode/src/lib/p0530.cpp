#include "leetcode.hpp"
#include <algorithm>

int leetcode::Solution0530::getMinimumDifference(const TreeNode* root) {
    // tree is guaranteed to have at least 2 nodes
    // values are 0 <= val <= 10^5
    int prev = -1000000;
    int minDiff = 1000000;
    inOrderTrav(root, prev, minDiff);
    return minDiff;
}

void leetcode::Solution0530::inOrderTrav(const TreeNode* root, int& prev, int& minDiff) {
    if (root != nullptr) {
        inOrderTrav(root->left, prev, minDiff);
        const int diff = root->val - prev;
        minDiff = std::min(diff, minDiff);
        prev = root->val;
        inOrderTrav(root->right, prev, minDiff);
    }
}
