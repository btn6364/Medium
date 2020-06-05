class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = Node("dummy")
        self.size = 0

    """
    Pretty print the linked list to the console.
    """
    def __str__(self):
        out = ""
        cur = self.head
        while cur.next:
            out += str(cur.data) + " -> "
            cur = cur.next
        return out + str(cur.data)
    

    """
    Insert a new node to a given location.
    """
    def insert(self, data, position):
        node = Node(data)
        cur = self.head
        if position > self.size:
            raise Exception("[ERROR]: Inserting to an out-of-bound index")
        #find the location
        while position > 0:
            cur = cur.next
            position -= 1

        # change the pointers
        node.next = cur.next
        cur.next = node

        #increase the size
        self.size += 1

    """
    Search a node at a given location.
    """
    def search(self, position):
        if position >= self.size :
            raise Exception("[ERROR]: Searching an out-of-bound element")
        cur = self.head.next
        while position > 0:
            cur = cur.next
            position -= 1
        return cur


    """
    Delete a node at a given location and return the removed data. 
    """
    def delete_position(self, position):
        if position >= self.size:
            raise Exception("[ERROR]: Deleting an out-of-bound position")

        #find the location
        cur = self.head
        while position > 0:
            cur = cur.next
            position -= 1

        #get the removed data
        removed = cur.data
        cur.next = cur.next.next

        #update the size of the linked list
        self.size -= 1
        return removed

    """
    Delete specific value.
    """
    def delete_node(self, value):
        prev, cur = self.head, self.head.next
        while cur is not None:
            if cur.data == value:
                break
            #update pointers
            prev = cur
            cur = cur.next
        
        if cur:
            prev.next = cur.next
            self.size -= 1
        else:
            raise Exception("[ERROR]: value does not exist in the linked list!")

    

def main1():
    linkedlist = LinkedList()
    for data in range(5):
        linkedlist.insert(data, 0)

    print(linkedlist)
    linkedlist.delete_position(0)
    print(linkedlist)
    linkedlist.delete_position(3)
    print(linkedlist)
    linkedlist.delete_position(0)
    print(linkedlist)
    try:
        linkedlist.delete_position(2)
    except Exception as e:
        print(e)

def main2():
    linkedlist = LinkedList()
    for data in range(5):
        linkedlist.insert(data, data)
    
    print(linkedlist)
    for val in range(3):
        linkedlist.delete_node(val)
        print(linkedlist)
    
    try:
        linkedlist.delete_node(5)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("############# TEST 1 #############")
    main1()

    print("\n############# TEST 2 #############")
    main2()
    
    
    


