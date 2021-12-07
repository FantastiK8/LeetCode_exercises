"""
141. Linked List Cycle
Easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# SOLUTION OF TWO POINTERS ONE IS MOVING BY ONE NODE AND THE SECOND POINTERS I MOVING BY TWO NODES
# IF THERE IS A CIRCLE THEY WILL EVENTUALLY MEET.

# this solution achieves:
# Success
# Details 
# Runtime: 40 ms, faster than 94.02% of Python online submissions for Linked List Cycle.
# Memory Usage: 20.5 MB, less than 44.55% of Python online submissions for Linked List Cycle.

#SECOND TIME RUN: GOT WORSE
# Success
# Details 
# Runtime: 48 ms, faster than 66.27% of Python online submissions for Linked List Cycle.
# Memory Usage: 20.3 MB, less than 85.52% of Python online submissions for Linked List Cycle.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return
        
        one_node_move = head # assign it to the first node in the list
        two_node_move = head
        
        # use the two node move because it will hit next None faster if there is one.
        while two_node_move.next: # e.g. [3,2,0,-4] TWO MOVE is 3 and TWOMOVE.next is 2
            #assign correctly new values to movements one and two moves at time. 
            one_node_move = one_node_move.next
            if two_node_move.next.next is not None:
                two_node_move = two_node_move.next.next # e.g. ONE was 3 but will be now 2, TWO will be 0
            else:
                return False
            # if there is a circle then the two nodes moving will catch the one node moving pointer 
            # and will be pointing to the same node.
            if one_node_move is two_node_move: #checking 2 with 0; checking 0 with 2; -4 with -4
                return True
        return False


# THIS SOLUTIONS STORES VISITED NODES IN A DICTIONARY. - NOT SURE IF THAT IS NEEDED THOUGH...
# but if array instead of dictionary the solution is much worse
# Success
# Details 
# Runtime: 1572 ms, faster than 5.24% of Python online submissions for Linked List Cycle.
# Memory Usage: 20.3 MB, less than 85.52% of Python online submissions for Linked List Cycle.

# this solution gets:

# Success
# Details 
# Runtime: 50 ms, faster than 48.70% of Python online submissions for Linked List Cycle.
# Memory Usage: 21.4 MB, less than 7.12% of Python online submissions for Linked List Cycle.



 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = {}
        
        while head:
            if head.next is not None:
                if head in seen:
                    return True
                
                else:
                    seen[head] = "dummy value"
                    head = head.next
                
            elif head.next is None:
                return False
                
        
