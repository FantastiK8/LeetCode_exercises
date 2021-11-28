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
POSSIBLE SOLUTION: 1. --> GOOD THOUGHT BUT IT OVERIDES THE WHOLE LIST ALHTOUGH A NEW TEMP ELEMENT WAS
CREATED... SO i MUST MAKE A COMPLETELY NEW INSTANCE OF THE NODELIST

- loop through the first LinkedList
- take the head of the second list (node b) and compare it with the node a from first list.
- if they are the same or node b is smaller put the node b (without the tail (nexts)) before node a of the first list and attach node a to node b     -> DOES THIS INFLUENCE THE LOOP?
- If node b is bigger than node a and smaller or same than node a next then add it behind then node a
- ---else keep it fro the next itteration node to place it to the right spot

while node_a.next != None:
    if node_a >= node_b:
        node_new_b = node_b
        # attach new tail to node b
        node_new_b.next = node_a

        # move in the second list to next node to allocate.
        node_b = node_b.next 
        node_a = node_a.next

    elif node_a < node_b:
        # jump in the itteration to the next one node in the first list
        # so update node_a for the next itteration
        node_a = node_a.next


        # if node_a.next > node_b:
        #     # store node_a.next (tail of node_a)
        #     node_a_next = node_a.next
        #     # manipulate with node_b so store it
        #     temp_node_b = node_b
        #     # Change the tail of node_b for node_a.next (tail of node_a) instead of previous tail of node_b
        #     temp_node_b.next = node_a_next
        #     # add the updated tail to node_a
        #     node_a.next = temp_node_b

        #     #update node_b to next one in the list to be checked
        #     node_b = node_b.next
        #     # update the node_a for the next itteration
        #     node_a = node_a.next
        # else:
        #     # insert it after node_a and node_a.next  BUT WHAT IF THERE X NUMBER OF SAME VALUES.

"""


# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        #self.head = False
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
    
    # def addLast(self, new_node):
    #     print( "LAST ADD ALST SO THIS ONE IS NEW_NODE AND SELF",new_node, " \n self \n", self )
        
    #     for current_node in self:
    #         #print(current_node)
    #         if current_node.next == None:

    #             print("\n CURRENT NODE ", current_node)
    #             print("\n NEW NODE ", new_node)
    #             current_node.next = new_node
    #             print("================================", current_node)
    #             #print(self)
    #             current_node = current_node.next
    #             return 
    def addAfterNode(self, new_node, target_node):
        print("\n SELF ", self)
        print("\n new node ", new_node)
        print("\n target node ", target_node)

        
        for node in self:
            print("\n\n\n NOOOODEEEE ", node)
            if node.val == target_node.val and node.next == target_node.next:
                new_node.next = node.next
                node.next = new_node
                print("\n node now  ", node)
        #print("\n 2SELFFFFF ", self)
                return 


    
    def addFirst(self, new_node):#, list):
        # dummy = ListNode(new_node.val, new_node.next)
        # dummy.next = self
        
        # # self = new_node
        # #print("#################", self)
        # return dummy
        dummy = ListNode(new_node.val, self)
        # print(dummy)
        # self = dummy
        #new_node.next = self #list
        #self = ListNode(new_node.val, new_node)
        
        print("\n selfffff ", self)
        # self = new_node
        #print("#################", self)
        return dummy

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next
        


    def addMiddle(self, new_node, insert_before_node): #, insert_after_node):    
        insert_after_node = self
        #insert_after_node = self
        # print("INSTER AFTER INITIALISATION ", insert_after_node)
        print("\n BEFORE NODE \n", insert_before_node)
        #for node in self:
       # node = self
        #print("INSTER AFTER INITIALISATION of node ", node)
       # while node is not None:
        for node in self:
            if node.val == insert_before_node.val and node.next == insert_before_node.next:
                # if new_node.next is None:
                #     print("\n afternode before changing \n ", insert_after_node)
                #     insert_after_node = insert_after_node.next
                #     print("\n after node changed when it was last one should be now only 4 INSTEAD OF 3 AND 4 \n", insert_after_node)
               # print("SELF #########  ", self)
                #print(node)
                print("\n NEW NODE \n", new_node)
                print("\n AFTER node beforeeeeeee changed  \n", insert_after_node)
                insert_after_node.next = new_node
                print("\n AFTER INSTERING NEW NODE AFTER NODE should change  \n", insert_after_node)
                new_node.next = node
                print("\n NEW NODE \n", new_node)
                print(" ")
                #print("\n insert after nodeeeeee NOW#### ", insert_after_node)
                #print("node   ", node)
               # print("'##########################################", node)
                return 
           # node = node.next
            insert_after_node = node

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1.head = True
        list2.head = True
        checked_all = False
        copy_list2 = ListNode(list2.val, list2.next)
        copy_list1 = ListNode(list1.val, list1.next)
        first = True
 
        while list1.next != None:
        # previous_node = ListNode(list1.val, list1.next)
            # print(list1.head)
            print(list1.val)
            print(list2.val)
            while (list1.val >= list2.val):
            # (list2.next != None):# or counter<4:
                #counter += 1
                # print(list1.val)
                # print(list2.val)
        # if list1.val >= list2.val:
                if first:
                # node_new_b.val, node_new_b.next = list2.val, list1
                    #list1.head = False
                    #copy_list1.head = False
                #    print("before adding first: \n", list1)
                    copy_list1 = copy_list1.addFirst(list2)#, copy_list1)
                    print("FIRST ADDED: \n", copy_list1)
                    first = False
             
                    
                else: #PUT IN THE MIDDLE OF THE LIST AND CHANGE TAIL AND HEAD WILL HAVE NEXT THIS CHANGE AS A TAIL
                   # print("\n before adding middle: \n", copy_list1)
                    copy_list1.addMiddle(list2, list1)#, previous_node) #self, new_node, insert_before_node, insert_after_node):   
                    #print("\n after adding middle: \n", copy_list1)
    
                if list2.next != None:
                    list2 = list2.next
                  #  print("\n LIST 2 NEXT ONE IS NOW (should be 3): \n ", list2)
               
                if list1.next is not None:
                    list1 = list1.next

            if list1.next is not None:
                list1 = list1.next
              #  print("WHERE AT IN IST1  \n", list1)


                
   #     print("LIST 1 ", list1)
        while list2.next is not None: 
            if list1.next == None:
                if (list1.val >= list2.val):
                    print("\n HEEEEERR #before adding middle: \n", copy_list1)
                    copy_list1.addMiddle(list2, list1)#, previous_node) #self, new_node, insert_before_node, insert_after_node):   
                    print("\n after adding middle: \n", copy_list1)
                    if list2.next != None:
                        list2 = list2.next
                        print("\n LIST 2 NEXT ONE IS NOW (should be 4): \n ", list2)
                else:
                    copy_list1.addLast(list2)
            if(list2.next is not None):
                list2 = list2.next
            
        if list2.next is None:
            print("finallleee is hereeeeee##########################")
            copy_list1 = copy_list1.addAfterNode(list2, list1)
            #copy_list1 = copy_list1.addLast(list2)
            # copy_list1.addMiddle(list2, list1)

        #             node_new_b.val, node_new_b.next = list2.val, list1
        #             list2 = list2.next 
        #         else:
        #             # i must add it at the end.....
        #             #node_new_b.val, node_new_b.next = list2.val, list1
        #             node_new_b.addLast(list2)




            
        return copy_list1

list1 = ListNode(1,ListNode(2, ListNode(4, None)))
# list1.head = True
list2 = ListNode(1,ListNode(3, ListNode(4, None))) 
#list2.head = True
sol = Solution()
print(sol.mergeTwoLists(list1, list2))