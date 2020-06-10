from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    """
    String representation
    """
    def __str__(self):
        if self.isEmpty():
            return "None"
        out = ""
        cur = self.head
        while cur:
            out += str(cur.data) + "->"
            cur = cur.next
        return out[:-2]

    """
    Return the size of the queue
    """
    def size(self):
        return self.size
    
    """
    Check if the queue is empty
    """
    def isEmpty(self):
        return self.size == 0
    
    """
    Add a new element to the end of the queue.
    """
    def enqueue(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    """
    Remove the top element of the queue and return it.
    """
    def dequeue(self):
        if self.isEmpty():
            raise Exception("[ERROR]: dequeue an empty queue!")
        removed = self.head.data
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return removed

    """
    Return the head element of the queue.
    """
    def head(self):
        if not self.head:
            return None
        return self.head.data

    """
    Return the tail element of the queue.
    """
    def tail(self):
        if not self.tail:
            return None
        return self.tail.data

def test():
    queue = Queue()
    for i in range(5):
        print(f"Enqueue: {i}")
        queue.enqueue(i)
    print(f"Queue: {queue}", end="\n\n")

    for _ in range(5):
        print(f"Dequeue: {queue.dequeue()}")
    print(f"Queue: {queue}")

if __name__ == "__main__":
    test()