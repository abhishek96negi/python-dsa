class Node:

    def __init__(self, item=None, priority=None, next=None):
        """
        Initialize a node with the given item and priority
        :param item: Data to be stored in the node
        :param priority: Priority of the node
        :param next: Reference to the next node
        """
        self.item = item
        self.priority = priority
        self.next = next


class PriorityQueue:

    def __init__(self):
        """
        Initialize an empty priority queue
        :return: None
        """
        self.start = None
        self.item_count = 0

    def push(self, data, priority):
        """
        Insert the data into the queue with the given priority
        :param data: Data to be inserted
        :param priority: Priority of the data
        :return: None
        """
        n = Node(data, priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1

    def is_empty(self):
        """
        Is the queue empty?
        :return: True if empty, False otherwise
        :rtype: bool
        """
        return self.start == None

    def pop(self):
        """
        Pop the data with the highest priority
        :return: Data with the highest priority
        :rtype: Any
        """
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data

    def size(self):
        """
        Size of the queue
        :return: Number of elements in the queue
        :rtype: int
        """
        return self.item_count



p = PriorityQueue()
p.push("Amit",4)
p.push("Arjun",7)
p.push("Ashima",2)
p.push("Agrah",5)
p.push("Anant",8)
p.push("Ambika",1)

while not p.is_empty():
    print(p.pop())