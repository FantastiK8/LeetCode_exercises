"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
--image-- explanation of the example visualy not available here.
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

############################
POSSIBLE SOLUTION: 
THIS TASK WAS A STRUGGLE AND VERY HARD - CERTAINLY I WOULD NOT CONSIDER THIS AS AN EASY TASK...

#######################################################################################
Success
Details 
Runtime: 48 ms, faster than 6.95% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 11.66% of Python online submissions for Merge Two Sorted Lists.
#######################################################################################


"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
    
    def addLast(self, new_node):
        for node in self:
            if node.next == None:
                node.next = ListNode(new_node.val, None)
                node = node.next
                return self

    def addAllLast(self, new_nodes):
        dummy = new_nodes #ListNode(new_nodes.val, None)
        for node in self:
            if node.next == None:
                node.next = dummy
                node = node.next
                return self 


    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next
        

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
  
        if list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        empty = False
        merged_listNode = ListNode()
        while (((list1 is not None) or (list2 is not None)) and (not empty)):
            if list1.val == list2.val:
                merged_listNode.addLast(list1)
                merged_listNode.addLast(list2)
                list1 = list1.next
                list2 = list2.next
                

            elif list1.val < list2.val:
                merged_listNode.addLast(list1)
                list1 = list1.next
            
            elif list1.val > list2.val:
                merged_listNode.addLast(list2)
                list2 = list2.next
                
            if list1 is None or list2 is None:
                empty = True
            
            if list2 is None :
                empty = True

        print(merged_listNode)

        stop = False
        
        if list1 is not None:
            if list1.next is None:
                if list2 is not None:
                    while list2.next is not None and not stop:
                        if list2 is not None:
                            if list1.val == list2.val:
                                merged_listNode.addLast(list1)
                                merged_listNode.addLast(list2)
                                list1 = list1.next
                                list2 = list2.next

                            elif list1.val < list2.val:
                                merged_listNode.addLast(list1)
                                list1 = list1.next

                            elif list1.val > list2.val:
                                if list2 is None:
                                    merged_listNode.addLast(list1)
                                    list1 = list1.next
                                elif list2 is not None:
                                    merged_listNode.addLast(list2)
                                    list2 = list2.next

                        elif list1 is None or list2 is None:
                            stop = True

        if list1 is None:
            merged_listNode.addAllLast(list2)
        
        elif list2 is None:
            merged_listNode.addAllLast(list1)

        merged_listNode = merged_listNode.next

        return merged_listNode



# list1 = ListNode(1,ListNode(2, ListNode(4, None)))
# list2 = ListNode(1,ListNode(3, ListNode(4, None))) 
# list1 = []
# list2 = []
# list1 = ListNode(2, None)
# list2 = ListNode(1, None)
list1 = ListNode(5, None)
list2 = ListNode(1,ListNode(2, ListNode(4, None)))
sol = Solution()
print(sol.mergeTwoLists(list1, list2))


# ISSUE ListNode(val=2, next={ListNode(val=3, next={ListNode(val=4, next={None})})})
# SUDDENLY LOST 1, 1, AND 4!