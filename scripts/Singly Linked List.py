# Singly Linked List

class Node:
    """
    Node  class to create a node for the linked list
    """

    def __init__(self, data=None, next_node=None):
        """
        Constructor to initialize the node
        Args:
            data: data to be stored in the node
            next_node: pointer to the next node
        """
        self.data = data
        self.next = next_node


class SLL:
    """
    Singly Linked List class
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
        Returns:
            bool: True if the linked list is empty, False otherwise

        """
        return True if self.start is None else False

    def insert_at_start(self, value):
        """
        Insert a node at the start of the linked list
        Args:
            value: data to be stored in the node
        """

        new_node = Node(value, self.start)
        self.start = new_node

    def insert_at_last(self, value):
        """
        Insert a node at the end of the linked list
        Args:
            value: data to be stored in the node
        """
        new_node = Node(value)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
        else:
            self.start = new_node

    def search(self, value):
        """
        Search for a node in the linked list
        Args:
            value: data to be searched
        Returns:
            bool: True if the node is found, False otherwise
        """
        temp = self.start
        while temp.next is not None:
            if temp.data == value:
                return temp
            temp = temp.next
        return None

    def insert_after(self, value, temp):
        """
        Insert a node after a given node
        Args:
            value: data to be searched
            temp: node to be inserted after
        """
        if temp is not None:
            new_node = Node(value, temp.next)
            temp.next = new_node

    def print_all(self):
        """
        Print all the nodes in the linked list
        """
        temp = self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def delete_first(self):
        """
        Delete the first node of the linked list
        """
        if not self.is_empty():
            self.start = self.start.next

    def delete_last(self):
        """
        Delete the last node of the linked list
        """
        if self.is_empty():
           pass
        elif self.start.next is None:
            self.start = None
        else:
            # Traverse to the second last node
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, value):
        """
        Delete a node with the given value
        Args:
            value: data to be deleted
        """
        if self.is_empty():
            pass
        elif self.start.next is None:
            if self.start.data == value:
                self.start = None
        else:
            temp = self.start
            if temp.data == value:
                self.start = temp.next
            else:
                # Traverse to the node before the node to be deleted
                while temp.next is not None:
                    if temp.next.data == value:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        """
        Iterator to traverse the linked list
        Returns:
           iterator: Iterator object to traverse the linked list.
        """
        temp = self.start
        while temp is not None:
            yield temp.data
            temp = temp.next


# Testing the Singly Linked List
my_list = SLL()
my_list.insert_at_start(10)
my_list.insert_at_start(20)
my_list.insert_at_last(30)
my_list.insert_after(25, my_list.search(20))
my_list.print_all()
my_list.delete_item(20)

# Printing all elements in the list
for x in my_list:
    print(x, end=' ')
