from node import Node

class Stack:
    """
    Initialize the stack 
    """
    def __init__(self):
        self.head = None
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
    Get the size of the stack
    """
    def getSize(self):
        return self.size

    """
    Return whether the stack is empty
    """
    def isEmpty(self):
        return self.getSize() == 0
    
    """
    Push the element into the top of the stack
    """
    def push(self, data):
        #create a new node
        node = Node(data)
        
        #insert it between the dummy node and the actual first node
        node.next = self.head
        self.head = node

        #increase size
        self.size += 1

    """
    Pop the top element from the stack and return its value. 
    """
    def pop(self):
        if self.isEmpty():
            raise Exception("[ERROR]: Popping from an empty stack!")
        #get the removed element
        removed = self.head

        #manipulate the pointers
        self.head = self.head.next
        removed.next = None

        #decrease size
        self.size -= 1

        #return the removed value
        return removed.data
    
    """
    Return the top element from the stack
    """
    def peek(self):
        if self.isEmpty():
            raise Exception("[ERROR]: Peeking from an empty stack!")

        return self.head.data

"""
Test all the functions
"""
def test():
    stack = Stack()
    for i in range(1, 10):
        stack.push(i)
    print(stack)

    for _ in range(5):
        removed = stack.pop()
        print(f"Pop: {removed}")
    print(stack)

    print(f"Peek: {stack.peek()}")

if __name__ == "__main__":
    test()