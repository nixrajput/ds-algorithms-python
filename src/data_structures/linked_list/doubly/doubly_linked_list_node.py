class DoublyLinkedListNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def toString(self, callback=None):
        if callback is not None:
            return callback(self.value)
        else:
            return self.value
