'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

def isValid(s):
    stack = []
    for c in s:
        # pop condition
        if stack:
            if c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(c)
        #when not match pop or (,[,{ 
        else:
            stack.append(c)
    
    # Check if stack is empty or not 
    if not stack:
        return True
    return False


print(isValid(s="()[]{}"))