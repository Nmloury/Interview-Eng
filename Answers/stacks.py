class Stack:
    '''
    Create a Stack in Python
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def revstring(string):
    '''
    reverse the order of a string
    '''
    stk = Stack()
    out = ""
    for c in string:
        stk.push(c)
    for i in range(len(string)):
        out += stk.pop()
    return out


def baseConverter(num, base):
    '''
    change the base of a decimal number
    '''
    digits = "0123456789ABCDEF"

    remainder = Stack()

    while num > 0:
        rem = num % base
        remainder.push(rem)
        num = num // base

    new_num = ""
    while not remainder.isEmpty():
        new_num += digits[remainder.pop()]

    return new_num
