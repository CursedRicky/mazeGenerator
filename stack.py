# LIFO stack
stack = []

def push(element) :
    stack.append(element)

def pop():
    element = stack[len(stack)-1]
    stack.remove(element)
    return element

