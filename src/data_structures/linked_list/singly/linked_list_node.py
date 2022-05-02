class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def toString(self, callback=None):
        if callback is not None:
            return callback(self.value)
        else:
            return self.value
