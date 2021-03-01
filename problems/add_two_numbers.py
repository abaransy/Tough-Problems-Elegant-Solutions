# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    res = []

    temp1 = l1
    temp2 = l2
    carry = False

    while temp1 or temp2:
        first_num = temp1.val if temp1 else 0
        second_num = temp2.val if temp2 else 0
        carry_previous = 1 if carry == True else 0
        add = first_num + second_num + carry_previous

        res.append( add % 10)

        if add > 9:
            carry = True
        else:
            carry = False

        if temp1:
            temp1 = temp1.next
        if temp2:
            temp2 = temp2.next

    if carry:
        res.append(1)

    def construct_list():
        l3 = ListNode()
        temp3 = l3

        for i in range(len(res)):
            temp3.val = res[i]

            if (i != len(res) - 1):
                temp3.next = ListNode()

            temp3 = temp3.next

        return l3

    return construct_list()
