/*
83. Remove Duplicates from Sorted List
Easy
Topics
premium lock icon
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
*/

// Definition for singly-linked list.
#include <iostream>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void printLinkedList(ListNode* head){
    ListNode* current = head;
    while (current != nullptr){
        std::cout << current << '\n';
        current = current->next;
    }
}

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == nullptr || head->next == nullptr)
            return head;
        ListNode* current = head->next;
        ListNode* prev = head;
        int currentVal = head->val;

        while(current != nullptr){
            // std::cout << "current address: " << current << '\n';
            // std::cout << "prev address: " << prev << std::endl;

            // std::cout << "current val: " << currentVal << std::endl;
            // printLinkedList(head);
            
            // std::cout << "Duplicate?: " << (currentVal == current->val) << std::endl;
            if(currentVal == current->val){
                prev->next = current->next;
                current = current->next;
            }else{
                currentVal = current->val;
                prev = current;
                current = current->next;
            }

            std::cout << '\n';
        }

        return head;
    }
};

int main(){
    ListNode* head = new ListNode(1);
    head->next = new ListNode(1);
    head->next->next = new ListNode(1);

    Solution solution = Solution();
    solution.deleteDuplicates(head);

    printLinkedList(head);

    return 0;
}