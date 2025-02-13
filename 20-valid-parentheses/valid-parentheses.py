class Solution:
    def isValid(self,s:str) ->bool:
        stack = []
        mapping = {')' : '(',']' : '[', '}':'{'}

        for char in s:
            if char in mapping:
                new_ele = stack.pop() if stack else '#'
                if mapping[char] != new_ele : return False
            else:
                stack.append(char)
        return not stack