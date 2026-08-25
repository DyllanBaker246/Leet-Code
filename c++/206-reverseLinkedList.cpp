/*
206. Reverse Linked List
Easy
Topics
premium lock icon
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
*/


// Definition for singly-linked list.
#include <vector>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* copy = head;
        std::vector<int> vec;
        while (copy != nullptr){
            vec.insert(vec.begin(), copy->val);
            copy = copy->next;
        }

        if(vec.size() == 0)
            return head;
        
        ListNode* revHead = new ListNode(vec[0]);
        ListNode* current = revHead;

        for(int i = 1; i < vec.size(); i++){
            current->next = new ListNode(vec[i]);
            current = current->next;
        }
        return revHead;
    }
};

void printVec(std::vector<int> vec){
    for(int i = 0; i < vec.size(); i++){

    }
}

int main(){
    return 0;
}