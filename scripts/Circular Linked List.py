class Node:
    def __init__(self, data, next_node=None):
        """
        Initialize a Node object with the given data.

        Args:
            data: The data to be stored in the node.
            next_node (optional): The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next = next_node

class CLL:
    def __init__(self):
        """
        Initialize a Circular Linked List object.
        """
        self.last = None

    def is_empty(self):
        """
        is_empty method to check if the linked list is empty or not
        """
        return self.last is None

    def insert_at_start(self, value):
        """
        Insert a node at the start of the linked list
        Args:
            value: data to be stored in the node
        """
        new_node = Node(value)

        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def insert_at_last(self, value):
        """
        Insert a node at the end of the linked list
        Args:
            value: data to be stored in the node
        """
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

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

        temp = self.last.next
        while temp != self.last:
            if temp.data == value:
                return temp
            temp = temp.next
        if temp.data == value:
            return temp
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

        new_node = Node(value, temp.next)
        temp.next = new_node

        if temp == self.last:
            self.last = new_node

    def print_list(self):
        """
        Print the elements of the linked list
        """
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.data, end=' ')
                temp = temp.next
            print(temp.data)

    def delete_first(self):
        """
        Delete the first node of the linked list
        """
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        """
        Delete the last node of the linked list
        """
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        """
        Delete a node with the given value
        Args:
            data: data to be deleted
        """
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next

                    while temp != self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                            break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    def __iter__(self):
        """
        Iterator method to traverse the linked list
        Returns:
            Iterator object
        """
        temp = self.last.next
        while temp != self.last:
            yield temp.data
            temp = temp.next

        yield temp.data

cll = CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(50, cll.search(10))
for x in cll:
    print(x, end=' ')
print()
cll.print_list()