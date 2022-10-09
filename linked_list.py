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

# 88. Merge Sorted Array
# Easy

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # for i in range(n):
#             nums1[i + m] = nums2[i]

#         # Sort nums1 list in-place.
#         nums1.sort()

#         j = 0
#         for i in range(max(len(nums1), len(nums2))):
#             print(nums1[i])
#             if nums1[i] == 0 and j < (min(len(nums1), len(nums2))):
#                 nums1[i] = nums2[j]
#                 j +=1

#         print(nums1)
#         nums1.sort()

# [1,2,3,5,6], m = 3,
# [1, 1,5,6], n = 3
    last = m + n - 1

    while m > 0 and n > 0:
        if nums2[n - 1] >= nums1[m - 1]:
            nums1[last] = nums2[n - 1]
            n -= 1
        elif nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        last, n = last - 1, n - 1


# 141. Linked List Cycle
# Easy

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

def hasCycle(head):

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# 160. Intersection of Two Linked Lists
# Easy

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.


def getIntersectionNode(headA, headB):

    l1, l2 = headA, headB

    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA

    return l1

    # list_of_visited_nodes = set()

    # cur , curb = headA, headB

    # while cur:
    #     list_of_visited_nodes.add(cur)
    #     cur = cur.next

    # while curb:
    #     if curb in list_of_visited_nodes:
    #         return curb
    #     curb = curb.next

    # return None

    # list_of_visited_nodes = set()

    # cur = headA

    # while cur:
    #     list_of_visited_nodes.add(cur)
    #     if not cur.next:
    #         break
    #     cur = cur.next

    # cur = headB

    # while cur:
    #     if cur in list_of_visited_nodes:
    #         return cur
    #     if cur.next == None:
    #         return None
    #     else:
    #         cur = cur.next


# 206. Reverse Linked List
# Easy
# Given the head of a singly linked list, reverse the list, and return the reversed list.

def reverseList(head):

    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

# 1669. Merge In Between Linked Lists
# Medium

# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# The blue edges and nodes in the following figure indicate the result:


def mergeInBetween(list1, a, b, list2):

    l1 = []
    cur = list1

    while cur:
        l1.append(cur.val)
        cur = cur.next

    l2 = []
    cur = list2

    while cur:
        l2.append(cur.val)
        cur = cur.next

    l3 = l1[:a] + l2 + l1[b + 1:]

    head = ListNode(l3[0])
    curr = head

    for x in l3[1:]:
        curr.next = ListNode(x)
        curr = curr.next

    return head
