class node:
    def __init__(self,value):
        self.data = value
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front:
            self.front = self.front.next
        else:
            self.front = self.rear = None

    def print(self):
        temp = self.front
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
    
    def reverse(self):
        temp = self.front
        prev = None
        next_node = None
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.rear,self.front = self.front,self.rear

n1 = queue()
n1.enqueue(node(10))
n1.enqueue(node(20))
n1.enqueue(node(30))
n1.dequeue()
n1.reverse()
n1.print()
