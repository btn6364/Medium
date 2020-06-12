from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    """
    String representation
    """
    def __str__(self):
        if self.isEmpty():
            return "None"
        out = ""
        cur = self.front
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
    Return the front element of the queue.
    """
    def getFront(self):
        if not self.front:
            return None
        return self.front.data

    """
    Return the rear element of the queue.
    """
    def getRear(self):
        if not self.rear:
            return None
        return self.rear.data

    """
    Add a new element to the end of the queue.
    """
    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.size += 1

    """
    Remove the top element of the queue and return it.
    """
    def dequeue(self):
        if self.isEmpty():
            raise Exception("[ERROR]: dequeue an empty queue!")
        removed = self.front.data
        if self.front is self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.size -= 1
        return removed

   

def test():
    queue = Queue()
    for i in range(5):
        print(f"Enqueue: {i}")
        queue.enqueue(i)
    print(f"Queue: {queue}", end="\n\n")

    for _ in range(3):
        print(f"Dequeue: {queue.dequeue()}")
    print(f"Queue: {queue}")

if __name__ == "__main__":
    test()