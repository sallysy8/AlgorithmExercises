# Given a singly linked list, find middle of the linked list. For example, if given linked list is 1 -> 2 -> 3-
# >4 -> 5 then output should be 3.
# If there are even nodes, then there would be two middle nodes, we need to print second middle
# element. For example, if given linked list is 1 -> 2 -> 3 -> 4 -> 5 -> 6 then output should be 4.

class Node:

    #initialise the node object
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        slow_tr = self.head
        fast_tr = self.head

        if self.head is not None:
            while (fast_tr is not None and fast_tr.next is not None):
                fast_tr = fast_tr.next.next
                slow_tr = slow_tr.next
            print("The midlle element is ", slow_tr.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
