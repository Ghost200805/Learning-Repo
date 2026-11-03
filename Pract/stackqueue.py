# Question 1 

class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, new_node):
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def print(self):
        temp = self.top
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def peek(self):
        if self.top != None:
            print(self.top.data)

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        temp = self.top
        self.top = self.top.next
        return temp

    # 5. Reverse Stack using another Stack
    def reverse(self):
        new_stack = stack()
        while not self.isempty():
            popped = self.pop()
            new_stack.push(node(popped.data))
        return new_stack

# 4. Reverse String using Stack
def reverse_string(text):
    s = stack()
    for char in text:
        s.push(node(char))
    
    reversed_str = ""
    while not s.isempty():
        popped_node = s.pop()
        reversed_str += popped_node.data
    return reversed_str

print("\n\n\n")
n1 = stack()
n1.push(node(10))
n1.push(node(20))
n1.push(node(30))
n1.push(node(40))
n1.print()

print("Popped element:", n1.pop().data)
n1.print()

print("\n--- Reverse Stack ---")
n2 = n1.reverse()
n2.print()

print("\n--- Reverse String ---")
my_string = "Hello World"
print("Original:", my_string)
print("Reversed:", reverse_string(my_string))



# Question 2

class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next
            if self.front == None:
                self.rear = None
                
            temp.next = None 
            
            return temp
        else:
            print("Queue is empty")
            return None

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    # 4. Reverse the queue using stack
    def reverse(self):
        stack = []

        while self.front:
            stack.append(self.dequeue())

        while stack:
            self.enqueue(stack.pop())

    # 5. Merge two queues into one
    def merge(self, q2):
        if not self.front:
            self.front = q2.front
            self.rear = q2.rear
        elif q2.front:
            self.rear.next = q2.front
            self.rear = q2.rear

        q2.front = q2.rear = None

    # 6. Check if two queues are identical
    def is_identical(self, q2):
        temp1 = self.front
        temp2 = q2.front
        
        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
            
        return temp1 == None and temp2 == None


q1 = queue()
q1.enqueue(node(10))
q1.enqueue(node(20))
q1.enqueue(node(30))

print("Original Queue 1:")
q1.print()

print("\nAfter 1 Dequeue:")
q1.dequeue()
q1.print()

print("\nReversed Queue:")
q1.reverse()
q1.print()

print("\n--- Merge & Identical Check ---")
q2 = queue()
q2.enqueue(node(30))
q2.enqueue(node(20))

print("Is q1 identical to q2?", q1.is_identical(q2))

q3 = queue()
q3.enqueue(node(40))
q3.enqueue(node(50))

q1.merge(q3)
print("Queue 1 after merging with Queue 3:")
q1.print()