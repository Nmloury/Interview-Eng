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

    def __init__(self):
        self.head = None
