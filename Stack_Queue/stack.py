from node import Node

class Stack:
    """
    Initialize the stack 
    """
    def __init__(self):
        self.head = Node("dummy")
        self.size = 0

    """
    String representation
    """
    def __str__(self):
        if self.isEmpty():
            return "None"
        out = ""
        cur = self.head.next
        while cur:
            out += str(cur.data) + "->"
            cur = cur.next
        return out[:-2]

    """
    Get the size of the stack
    """
    def size(self):
        return self.size

    """
    Return whether the stack is empty
    """
    def isEmpty(self):
        return self.size() == 0
    
    """
    Push the element into the top of the stack
    """
    def push(self, data):
        #create a new node
        node = Node(data)
        
        #insert it between the dummy node and the actual first node
        node.next = self.head.next
        self.head.next = node

        #increase size
        self.size += 1

    """
    Pop the top element from the stack and return its value. 
    """
    def pop(self):
        if self.isEmpty():
            raise Exception("[ERROR]: Popping from an empty stack!")
        #get the removed element
        removed = self.head.next

        #manipulate the pointers
        self.head.next = self.head.next.next
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

        return self.head.next.data

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