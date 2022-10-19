import sys

count = int(sys.stdin.readline())
stack = []

def do_order(order):
    if order == "pop":
        if len(stack) == 0:
            return -1
        else:
            return stack.pop()
    elif order == "size":
        return len(stack)
    elif order == "empty":
        if len(stack) == 0:
            return 1
        else:
            return 0
    elif order == "top":
        if len(stack) == 0:
            return -1
        else:
            return stack[-1]


result = []
for i in range(count):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        stack.append(order[1])
    else:
        result.append(do_order(order[0]))

for i in range(len(result)):
            print(result[i])