# 2
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# EXAMPLE
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            val = l1Val + l2Val + carry
            carry = val // 10
            val = val % 10

            # now the curr.next node is the new node
            curr.next = ListNode(val)
            # and the current is the new node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            print(curr.val)
        return dummy.next


# node1 -> node2 -> node3
# node4 -> node5 -> node6

# dummy -> None

# l1.val = 1
# l2.val = 4
# val = 5
# carry = 0
# val =  5

# curr.next = node(5) [ dummy - node(5)]
# curr = node(5)

# l1 = node2
# l2 = node3

# -----

# l1.val = 2
# l2.val = 5
# val = 7
# carry = 0
# val =  7

# curr.next = node(7) [ dummy - [node(5) - node(7)]]
# curr = node(7)

# l1 = node3
# l2 = node4

# -----

# l1.val = 3
# l2.val = 6
# val = 9
# carry = 0
# val =  9

# curr.next = node(9) [ dummy - [node(5) - node(7) - node(9)]]
# curr = node(9)

# l1 = None
# l2 = None
# carry = 0

# break

# dummy.next = [node(5) - node(7) - node(9)]


node1 = ListNode()
node1.val = 1

node2 = ListNode()
node2.val = 2

node3 = ListNode()
node3.val = 3

node4 = ListNode()
node4.val = 4

node5 = ListNode()
node5.val = 5

node6 = ListNode()
node6.val = 6


node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

# [1, 2, 3] -> 321
# [ 4, 5, 6]-> 654

result = Solution()
print("*******")
print(result.addTwoNumbers(node1, node4))


# 234. Palindrome Linked List
# Easy

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


# Example 1:

# Input: head = [1,2,2,1]
# Output: true

# Example 2:

# Input: head = [1,2]
# Output: false


def isPalindrome(head):

    cur = head
    lst_data = []

    while cur:
        lst_data.append(cur.val)
        cur = cur.next

    if lst_data == lst_data[::-1]:
        return True

    return False


a = "a"
b = "b"

c = a + b
print(c)


row = 4
columns = 5
table = []

for i in range(4):
    for j in range(5):
        x = i
        y = j + 1
        table.append([x, y])
print(table)


# 21. Merge Two Sorted Lists
# Easy

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

def mergeTwoLists(l1, l2):

    # if l1 is None:
    #     return l2
    # elif l2 is None:
    #     return l1
    # elif l1.val < l2.val:
    #     l1.next = self.mergeTwoLists(l1.next, l2)
    #     return l1
    # else:
    #     l2.next = self.mergeTwoLists(l1, l2.next)
    #     return l2

    cur = dummy = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1, cur = l1.next, l1
        else:
            cur.next = l2
            l2, cur = l2.next, l2

    if l1 or l2:
        cur.next = l1 if l1 else l2

    return dummy.next


# 83. Remove Duplicates from Sorted Lis
# Easy

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

def deleteDuplicates(head):

    curr = head

    while curr != None and curr.next != None:
        while curr.val == curr.next.val:
            curr.next = curr.next.next
            if curr.next == None:
                break
        curr = curr.next

    return head
