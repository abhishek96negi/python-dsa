class Stack:
    def __init__(self):
        """
        Initialize an empty list to store the stack elements.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.
        Returns True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, data):
        """
        Add an element to the top of the stack.
        Args:
            data: The element to be added to the stack.
        """
        self.items.append(data)

    def pop(self):
        """
        Remove and return the top element from the stack.
        Raises IndexError if the stack is empty.
        Returns the removed element.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")

    def peek(self):
        """
        Return the top element of the stack without removing it.
        Raises IndexError if the stack is empty.
        Returns the top element.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        """
        Return the number of elements in the stack.
        Returns the length of the list representing the stack.
        """
        return len(self.items)


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is",s1.peek())
print("Removed element is",s1.pop())
print("Top element is",s1.peek())
print()