class Node:
    '''
    Create a Node class in Python for lists
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    '''
    Create an Unordered List class in Python
    '''
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
                if previous is not None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
            else:
                previous = current
                current = current.getNext()
        if found is True:
            print "item removed!"
        else:
            print "item not found!"

    def append(self, item):
        current = self.head
        if current is None:
            self.head = Node(item)
        else:
            next_item = current.getNext()
            while next_item is not None:
                current = next_item
                next_item = current.getNext()
            current.setNext(Node(item))

    def insert(self, index, item):
        position = 0
        previous = None
        current = self.head
        if index == 0:
            ins = Node(item)
            ins.setNext(current)
            self.head = ins
        else:
            while current is not None:
                if index == position:
                    ins = Node(item)
                    ins.setNext(current)
                    previous.setNext(ins)
                    break
                else:
                    previous = current
                    current = current.getNext()
                    position += 1

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current is not None and not found:
            if current.data == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if found is True:
            return index
        else:
            print "item not found!"
            return None

    def pop(self, index=None):
        position = 0
        previous = None
        current = self.head
        if index is None:
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            return current.getData()
        else:
            while current is not None:
                if index == position:
                    previous.setNext(current.getNext())
                    return current.getData()
                else:
                    previous = current
                    current = current.getNext()
                    position += 1
        print "index not in range!"

    def lprint(self):
        current = self.head
        while current is not None:
            print current.getData()
            current = current.getNext()
