"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'


--------------------------------------
Solutions: 
check for constratints

if len(s) < 1 or len(s) > 10**4:
    return false

if invalidInput(s):
    return false

if len(s) % 2 != 0:
    return false

-----------------------------------------------------------------------------------------
OPTION 1: NAIVE NOT WORKING
- make hash map with "key" for each bracket including opening and closing 
star with value 1 and opening bracket key (, value 2 with the closing bracket as key ) and so on.
- find the middle string
- loop through the string in range of its half
- check starting char and its value under the key - save the value
- check the last char and its value under the key - compare with first char value if it is +1 then continue


OPTION 2: NAIVE NOT WORKING

- get middle of the string
- loop through range of half of the string
- check the first char order with the last char order is the same if + 1 or + 2 if not return false
this order solution ord() is working because the brackets closing is max 2 away from the opening one.

BOTH WILL FAIL WITH: Input: s = "()[]{}"

########################################################################################
OPTION 3:  WORKING!!! 
Runtime: 20 ms, faster than 69.64% of Python online submissions for Valid Parentheses.
Memory Usage: 13.6 MB, less than 63.95% of Python online submissions

        # - create a new empty arr STACK LIFO for values of brackets (keys)
        # - loop through the string
        # - check ith char value in brackets dictionary
        # - check if odd --> for opening brackets
        # --> to current value add + 1 for closing one and append to queue
        # - else if even --> for closing bracket
        # - check if queue is not empty then
        # - check next ith char and if closing bracket then MUST BE THE SAME as the bracket in LIFO last in
        # - If yes remove the key from stack LIFO 

        # - after loop if queue is empty then return True
    

#########################################################################################
"""

class Solution(object):
    def invalidInput(self, s):

        brackets = ['(','{','[',']','}',')']

        for char in s:
            if char not in brackets:
                return True

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        from collections import deque
       # check for constratints

        if len(s) < 1 or len(s) > 10**4:
            return False

        if self.invalidInput(s):
            return False

        if len(s) % 2 != 0:
            return False

        brackets_dictionary = {'(': 1,
                            ')': 2,
                            '[': 3,
                            ']': 4,
                            '{': 5,
                            '}': 6
                            }

        if (brackets_dictionary[s[0]] % 2 == 0) or (brackets_dictionary[s[len(s) - 1]] % 2 != 0):
            return False


        stack_brackets = deque()

        for char in s:
            current_value = brackets_dictionary[char]
            if current_value % 2 != 0:
                val_in_queue = brackets_dictionary[char] + 1
                #key_in_queue = next((k for k in brackets_dictionary if brackets_dictionary[k] == val_in_queue))
                #stack_brackets.append(key_in_queue)
                stack_brackets.append(val_in_queue)
            elif current_value % 2 == 0:
                #print(current_value)
                #key_popped = stack_brackets.pop()
                if len(stack_brackets) != 0:
                    value_popped = stack_brackets.pop()
               # print(value_popped)
                #print(key_popped)
               # if key_popped is not char:
                    if value_popped != current_value:
                        #print("here")
                        return False
                else:
                    return False


        if len(stack_brackets) == 0:
            return True


#s = "()[]{}"
# s = "(]"
#s = "()"
s = "()))"
sol = Solution()
print(sol.isValid(s))



