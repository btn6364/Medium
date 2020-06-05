#######################################################
## LINKED LIST IMPLEMENTATION
#######################################################

"""
The fundamental component of a linked list. 
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
"""
The linked list
"""
class LinkedList:
    """
    Initialize the linked list
    """
    def __init__(self):
        self.head = Node("dummy")
        self.size = 0

    """
    Pretty print the linked list to the console.
    """
    def __str__(self):
        out = ""
        tmp = self.head
        while tmp.next:
            out += str(tmp.data) + " -> "
            tmp = tmp.next
        return out + str(tmp.data)
    

    """
    Insert a new node to a given location.

    Runtime: O(position)
    Space: O(1)
    """
    def insert(self, data, position):
        node = Node(data)
        tmp = self.head
        if position > self.size:
            raise Exception("[ERROR]: Inserting to an out-of-bound index")
        #find the location
        while position > 0:
            tmp = tmp.next
            position -= 1

        # change the pointers
        node.next = tmp.next
        tmp.next = node

        #increase the size
        self.size += 1

    """
    Search a node at a given location.

    Runtime: O(position)
    Space: O(1)
    """
    def search(self, position):
        if position >= self.size :
            raise Exception("[ERROR]: Searching an out-of-bound element")
        tmp = self.head.next
        while position > 0:
            tmp = tmp.next
            position -= 1
        return tmp


    """
    Delete a node at a given location and return the removed data. 

    Runtime: O(position)
    Space: O(1)
    """
    def delete_position(self, position):
        if position >= self.size:
            raise Exception("[ERROR]: Deleting an out-of-bound position")

        #find the location
        tmp = self.head
        while position > 0:
            tmp = tmp.next
            position -= 1

        #get the removed data
        removed = tmp.data
        tmp.next = tmp.next.next

        #update the size of the linked list
        self.size -= 1
        return removed

    """
    Delete specific value.

    Runtime: O(position)
    Space: O(1)
    """
    def delete_node(self, value):
        prev, tmp = self.head, self.head.next
        while tmp is not None:
            if tmp.data == value:
                break
            #update pointers
            prev = tmp
            tmp = tmp.next
        
        if tmp:
            prev.next = tmp.next
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
    
    
    


