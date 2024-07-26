class Node:
    def __init__(self, data=None, prev=None, next=None):
        """
        Initialize a Node object with the given data.

        Args:
            data: The data to be stored in the node.
            prev (optional): The previous node in the linked list. Defaults to None.
            next (optional): The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.prev = prev
        self.next = next

class CDLL:
    def __init__(self, start=None):
        """
        Initialize a Circular Doubly Linked List object with the given start node.

        Args:
            start (optional): The starting node of the circular doubly linked list. Defaults to None.
        """
        self.start = start

    def is_empty(self):
        """
        Is_empty method to check if the linked list is empty or not
        """
        return self.start == None

    def insert_at_start(self, data):
        """
        Insert a new node with the given data at the start of the circular doubly linked list.

        Args:
            data: The data to be stored in the new node.
        """
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        """
        Insert a new node with the given data at the end of the circular doubly linked list.

        Args:
            data: The data to be stored in the new node.
        """
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n

    def search(self, data):
        """
        Search for a node with the given data in the circular doubly linked list.

        Args:
            data: The data to be searched.

        Returns:
            The node with the given data if found, otherwise None.
        """
        temp = self.start
        if temp == None:
            return None
        if temp.data == data:
            return temp
        else:
            temp = temp.next

        while temp != self.start:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        """
        Insert a new node with the given data after the given node in the circular doubly linked list.

        Args:
            temp: The node after which the new node should be inserted.
            data: The data to be stored in the new node.
        """
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n

    def print_list(self):
        """
        Print the elements of the circular doubly linked list.
        """
        temp = self.start
        if temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
            while temp is not self.start:
                print(temp.data, end=' ')
                temp = temp.next

    def delete_first(self):
        """
        Delete the first node of the circular doubly linked list.
        """
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

    def delete_last(self):
        """
        Delete the last node of the circular doubly linked list.
        """
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        """
        Delete the node with the given data from the circular doubly linked list.

        Args:
            data: The data of the node to be deleted.
        """
        if self.start is not None:
            temp = self.start
            if temp.data == data:
                self.delete_first()
            else:
                temp = temp.next
                while temp is not self.start:
                    if temp.data == data:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                    temp = temp.next

    def __iter__(self):
        """
        Iterator method to traverse the circular doubly linked list.
        """
        temp = self.start
        if temp is not None:
            yield temp.data
            temp = temp.next
            while temp is not self.start:
                yield temp.data
                temp = temp.next

mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30), 35)
mylist.delete_item(20)
for x in mylist:
    print(x)
