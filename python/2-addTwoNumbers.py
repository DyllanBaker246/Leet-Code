'''
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        num3 = 0
        currentNum = 0
        position = 1

        head = ListNode()
        currentNode = head

        while l1 != None:
            currentNum = l1.val
            currentNum *= position
            num1 += currentNum

            position *= 10
            l1 = l1.next

        position = 1
        while l2 != None:
            currentNum = l2.val
            currentNum *= position
            num2 += currentNum

            position *= 10
            l2 = l2.next

        
        num3 = num1 + num2

        while num3 != 0:
            currentNum = num3 % 10
            currentNode.val = currentNum
            if num3 >= 10:
                currentNode.next = ListNode()
                currentNode = currentNode.next

            num3 //= 10

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

    printLinkedList(solution.addTwoNumbers(node1, node4))

main()

        