def perform_operation(op, b, a):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '%':
        return a % b
    elif op == '^' or op == '$':
        return a ** b

exp=[5, 10, 2, '-', 3, '*', '+'] 
stack=[]

for i in exp:
    if isinstance(i, int):
        stack.append(i)
    else:
        b=stack.pop()
        a=stack.pop()
        result=perform_operation(i,b,a)
        stack.append(result)

print("Result of postfix expression:", stack[-1])