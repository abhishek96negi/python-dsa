class Node:
    def __init__(self, item=None, next=None):
        """
        Initialize a Node object with the given item and next pointer.

        Args:
            item: The data to be stored in the node.
            next (optional): The next node in the linked list. Defaults to None.
        """
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        """
        Initialize an empty Stack object with start set to None and item_count set to 0.
        """
        self.start = None
        self.item_count = 0

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.start == None

    def push(self, data):
        """
        Push an item onto the stack.

        Args:
            data: The data to be pushed onto the stack.
        """
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The data of the top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        """
        Return the top item from the stack without removing it.

        Returns:
            The data of the top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")

    def size(self):
            """
            Return the number of items in the stack.

            Returns:
                int: The number of items in the stack.
            """
            return self.item_count


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Total elements in the stack=",s1.size())
print("Top element on the stack is",s1.peek())
print("Poped element is",s1.pop())
print("Total elements in the stack=",s1.size())
print("Top element on the stack is",s1.peek())
print()
