class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class cqueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        else:
            self.front = self.rear = new_node
            self.rear.next = self.front 

    def dequeue(self):
        if not self.front:
            print("Queue is empty")
            return None
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def print(self):
        if not self.front:
            print("Queue is empty")
            return
        temp = self.front
        print(temp.data, end=" -> ")
        while temp.next != self.front:
            temp = temp.next
            print(temp.data, end=" -> ")

    def reverse(self):
        if not self.front or self.front == self.rear:
            return
        prev = self.rear
        curr = self.front
        start = self.front
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == start:
                break
        self.front, self.rear = self.rear, self.front


n1 = cqueue()
n1.enqueue(node(10))
n1.enqueue(node(20))
n1.enqueue(node(30))
n1.enqueue(node(40))
n1.dequeue()
print("Original:")
n1.print()

n1.reverse()

print("\nReversed:")
n1.print() 