'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next   

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        head = ListNode()
        currentHead = head
        list1Current = list1
        list2Current = list2

        while list1Current is not None and list2Current is not None:
            # print(list1Current.val)
            # print(list2Current.val)
            if list1Current.val <= list2Current.val:
                currentHead.val = list1Current.val
                list1Current = list1Current.next
                currentHead.next = ListNode()
                currentHead = currentHead.next
                continue
                
            
            if list1Current.val > list2Current.val:
                currentHead.val = list2Current.val
                list2Current = list2Current.next
                currentHead.next = ListNode()
                currentHead = currentHead.next
                continue

        if list1Current is None and list2Current is not None:
            currentHead.val = list2Current.val
            currentHead.next = list2Current.next
            return head

        if list2Current is None and List1Current is not None:
            currentHead.val = list1Current.val
            currentHead.next = list1Current.next
            return head

        currentHead = None
        return head



def printLinkedList(list1: Optional[ListNode]):
    if(list1 == None):
        print("List is Empty")

    while(list1 != None):
        print(list1.val)
        list1 = list1.next

def main():
    solution = Solution()

    # initialize linked list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node4.next = node5
    node5.next = node6

    printLinkedList(solution.mergeTwoLists(node1, node4))

    # sortedNode = solution.mergeTwoLists(node1, node4)

main()
            

        