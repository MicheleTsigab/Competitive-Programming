class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch!=']':
                stack.append(ch)
            else: #]
                substr=''
                while stack[-1]!='[':
                    substr=stack.pop()+substr
                    
                stack.pop() #[ is popped
                number=''
                while stack and stack[-1].isdigit():
                    number=stack.pop()+number
                stack.append(substr*int(number))
        return ''.join(stack)