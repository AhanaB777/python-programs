def precedence(op):
    if op=='$' or op=='^' :
        return 3
    elif op=='*' or op=='/' or op=='%':
        return 2
    elif op=='+' or op=='-':
        return 1
    return 0
    
a=[5,'+','(',10,'-',2,')','*',3]
op=['+','-','*','/','%','$','^']
p=[]
stack=[]

for i in a:
    if i=='(':
        stack.append(i)
    elif i==')':
        while len(stack)>0 and stack[-1]!='(':
            p.append(stack.pop())
        stack.pop()
    elif i in op:
        while len(stack)>0 and precedence(stack[-1])>=precedence(i):
            p.append(stack.pop())
        stack.append(i)
    else:
        p.append(i)

while len(stack)>0:
    p.append(stack.pop())

print("Postfix expression:",p)





    