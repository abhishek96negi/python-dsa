class Node:

    def __init__(self, item=None, next=None):
        """
        Initialize a Node object with the given item and next pointer.

        Args:
            item (optional): The data to be stored in the node.
            next (optional): The next node in the linked list. Defaults to None.
        """
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        """
        Initialize an empty Queue object with front and rear set to None and item_count set to 0.
        """
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.front==None

    def enqueue(self, data):
        """
        Add an item to the rear of the queue.

        Args:
            data: The data to be added to the queue.
        """
        temp = Node(data)
        if self.is_empty():
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.item_count += 1

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.

        Returns:
            The data of the removed item.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count


q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())
