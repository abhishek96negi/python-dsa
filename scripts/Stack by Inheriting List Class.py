class Stack(list):

    def is_empty(self):
        """
        In this method we are checking the stack is empty or not
        :return: True or False
        """
        return len(self)==0

    def push(self, data):
        """
        In this method we are adding the data to the stack
        :param data: data which we want to add
        :return: None
        """
        self.append(data)

    def pop(self):
        """
        In this method we are removing the data from the stack
        :return: None
        """
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")

    def peek(self):
        """
        In this method we are getting the top element of the stack
        :return: top element of the stack
        """
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        """
        In this method we are getting the size of the stack
        :return: size of the stack
        """
        return len(self)

    def insert(self, index, data):
        """
        In this method we are inserting the data at the given index
        :param index: index at which we want to insert the data
        :param data: data which we want to insert
        :return: None
        """
        raise AttributeError("No attribute 'insert' in Stack")


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top value=",s1.peek())
print()
