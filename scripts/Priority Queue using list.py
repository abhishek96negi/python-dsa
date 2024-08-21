class PriorityQueue:
    """
    * A priority queue is a collection of elements such that each element has been assigned a priority .
    * The order of elements are deleted and processed comes from the following rules
    * An element of higher priority is processed before any element of lower priority
    * Two elements with the same priority are processed according to the order in which they were added in the priority
    queue .
    """
    def __init__(self):
        self.items = []


    def push(self, data, priority):
        """
        Insert the data into the queue with the given priority
        :param data: Data to be inserted
        :param priority: Priority of the data
        :return: None
        """
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index,  (data, priority))

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items.pop(0)[0]

    def size(self):
        return len(self.items)


p = PriorityQueue()
p.push("Amit", 4)
p.push("Arjun", 7)
p.push("Ashima", 2)
p.push("Agrah", 5)
p.push("Anant", 8)
p.push("Ambika", 1)

while not p.is_empty():
    print(p.pop())
