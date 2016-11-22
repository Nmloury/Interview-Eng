class Queue:
    '''
    Create a Queue in Python
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


class Deque:
    '''
    Create a Deque in Python
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0, item)

    def addBack(self, item):
        self.items.append(item)

    def removeFront(self):
        self.items.pop(0)

    def removeBack(self):
        self.items.pop()

    def size(self):
        return len(self.items)


def hotPotato(names, num):
    '''
    Hot Potato funnction uses the Queue class
    '''
    Q = Queue()
    for name in names:
        Q.enqueue(name)

    while Q.size() > 1:
        for i in range(num):
            Q.enqueue(Q.dequeue())
        Q.dequeue()

    return Q.dequeue()


def is_palindrome(string):
    D = Deque()

    for c in string:
        D.addBack(c)

    is_equal = True

    while D.size() > 1 and is_equal:
        first = D.removeFront()
        last = D.removeBack()
        if first != last:
            is_equal = False
            break

    return is_equal
