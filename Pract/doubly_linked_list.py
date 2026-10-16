class node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class sll:
    def __init__(self):
        self.head = None
    def append(self,new_node):
        if self.head==None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    def delete(self,value):
        temp = self.head
        if temp.data == value:
            self.head = self.head.next
            self.head.prev = None
        else:
            while temp.data!=value:
                temp = temp.next
                if temp == None:
                    print("Value is not present in the list")
                    return
            temp.prev = temp.next
            temp = None
    def insert(self,new_node,pos):
        if pos == 1:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while (p!=pos-1):
                temp = temp.next
                p+=1
        new_node.next = temp.next
        new_node.prev = temp
        temp.next  = new_node
        temp.next.next.prev = new_node

    def print(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end=" -> ")
            temp=temp.next

list1=sll()
n1 = node(10)
n2 = node(20)
list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(40))

list1.insert(node(400),2)

list1.delete(100)
list1.delete(10)
list1.print()
