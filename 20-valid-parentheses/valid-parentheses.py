class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # 닫는 괄호
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:  # 여는 괄호
                stack.append(char)
        
        return not stack  # 스택이 비어 있으면 True