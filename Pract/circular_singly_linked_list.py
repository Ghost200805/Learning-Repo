class node:
    def __init__(self,value):
        self.data = value
        self.next = None

class sll:
    def __init__(self):
        self.head = None
    def append(self,new_node):
        if self.head==None:
            self.head= new_node
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
                if temp.next == self.head:
                    break
            temp.next = new_node
            new_node.next = self.head
    def delete(self,value):
        temp = self.head
        prev = None
        if temp.data == value:
            a = temp
            self.head = self.head.next
            while True:
                temp = temp.next
                if temp.next==a:
                    break
            temp.next = self.head
        else:
            while temp.data!=value:
                prev=temp
                temp = temp.next
                if temp == self.head:
                    print("Value is not present in the list")
                    return
            prev.next = temp.next
            temp = None
    def insert(self,new_node,pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while (p!=pos-1):
                temp = temp.next
                p+=1
                if temp.next == self.head:
                    print("That position doesnt exist.")
                    break
        if temp.next!=self.head:
            new_node.next = temp.next
            temp.next  = new_node
    def reverse(self):
        curr=self.head
        if self.head==None:
            return
        l = [curr.data]
        while(True):
            l.append(curr.data)
            curr=curr.next
            if curr.next==self.head:
                break
            
        temp = self.head
        for i in range(len(l)-1,-1,-1):
            temp.data = l[i]
            print(temp.data)
            if temp.next == self.head:
                break
            temp = temp.next
        
            
    def print(self):
        temp = self.head
        while(True):
            print(temp.data,sep=" -> ")
            temp=temp.next
            if temp == self.head:
                break

list1=sll()
n1 = node(10)
n2 = node(20)
list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(40))
list1.print()
print("---------------------")
list1.delete(100)
list1.delete(10)
list1.print()
print("---------------------")
list1.insert(node(400),5)
list1.insert(node(400),2)
list1.print()
print("---------------------")
list1.reverse()