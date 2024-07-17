class Node:
    """
    Node class to represent each node in the doubly linked list
    """
    def __init__(self, data, prev_node=None, next_node=None):
        """
        Constructor to initialize a node
        Args:
            data: data to be stored in the node
            prev_node: pointer to the previous node
            next_node: pointer to the next node
        """
        self.prev = prev_node
        self.data = data
        self.next = next_node

class DLL:
    """
    Doubly Linked List class
    """
    def __init__(self, start=None):
        """
        Constructor to initialize the linked list
        Args:
            start: starting node of the linked list
        """
        self.start = start

    def is_empty(self):
        """
        Check if the linked list is empty
        """
        return True if self.start is None else False

    def insert_at_start(self, value):
        """
        Insert a node at the start of the linked list
        Args:
            value: data to be stored in the node
        """
        new_node = Node(value, next_node=self.start)

        if not self.is_empty():
            self.start.prev = new_node

        self.start = new_node

    def insert_at_last(self, value):
        """
        Insert a node at the end of the linked list
        Args:
            value: data to be stored in the node
        """

        temp = self.start

        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next

        new_node = Node(value, prev_node=temp)

        if temp is None:
            self.start = new_node
        else:
            temp.next = new_node


    def search(self, value):
        """
        Search for a node with the given value in the linked list
        Args:
            value: data to be searched
        Returns:
            Node: node with the given value if found, else None
        """
        if self.is_empty():
            return None

        temp = self.start

        while temp is not None:
            if temp.data == value:
                return temp
            temp = temp.next

        return None

    def insert_after(self, value, temp):
        """
        Insert a node after a given node
        Args:
            value: data to be stored in the node
            temp: node after which the new node should be inserted
        """

        if temp is None:
            return None

        new_node = Node(value, prev_node=temp, next_node=temp.next)
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node

    def print_all(self):
        """
        Print all the nodes in the linked list
        """
        temp = self.start
        while temp.next is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def __iter__(self):
        """
        Iterator method to traverse the linked list
        """
        temp = self.start
        while temp:
            yield temp.data
            temp = temp.next

    def delete_first(self):
        """
        Delete the first node of the linked list
        """
        if not self.is_empty():
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        """
        Delete the last node of the linked list
        """

        if self.is_empty():
            return None

        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, value):
        """
        Delete a node with the given value
        Args:
            value: data to be deleted
        """
        if self.is_empty():
            return None

        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next
                break
            temp = temp.next

mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(15, mylist.search(10))
for x in mylist:
    print(x,end=' ')
print()