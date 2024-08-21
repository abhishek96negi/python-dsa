class Node:
    def __init__(self, item=None, prev=None, next=None):
        """
        Initialize a Node object with the given item, previous node, and next node.

        Args:
            item: The data to be stored in the node.
            prev (optional): The previous node in the linked list. Defaults to None.
            next (optional): The next node in the linked list. Defaults to None.
        """
        self.prev = prev
        self.item = item
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        """
        Check if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return self.item_count == 0

    def insert_front(self, data):
        """
        Insert an item at the front of the deque.

        Args:
            data: The data to be inserted.
        """
        n = Node(data, None, self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n

        self.front = n
        self.item_count += 1

    def insert_rear(self, data):
        """
        Insert an item at the rear of the deque.

        Args:
            data: The data to be inserted.
        """
        n = Node(data, self.rear)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def delete_front(self):
        """
        Delete an item from the front of the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None

        self.item_count -= 1

    def delete_rear(self):
        """
        Delete an item from the rear of the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None

        self.item_count -= 1

    def get_front(self):
        """
        Get the item at the front of the deque.

        Returns:
            The item at the front of the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.item

    def get_rear(self):
        """
        Get the item at the rear of the deque.

        Returns:
            The item at the rear of the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")

        return self.rear.item

    def size(self):
        return self.item_count


d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(), d1.get_rear())
print(d1.item_count)


