class node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class sll:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        new_node.next = None

        if self.head == None:
            new_node.prev = None
            self.head = new_node
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def delete(self, value):
        temp = self.head

        while temp != None and temp.data != value:
            temp = temp.next

        if temp == None:
            print("Value is not present in the list")
            return

        if temp.prev == None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next

        if temp.next != None:
            temp.next.prev = temp.prev

        # Detach the removed node.
        temp.next = None
        temp.prev = None

    def insert(self, new_node, pos):
        # Positions are 1-based.
        if pos < 1:
            return("Position must be at least 1")

        if pos == 1:
            new_node.next = self.head
            new_node.prev = None

            if self.head != None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp != None and p < pos - 1:
            temp = temp.next
            p += 1

        if temp == None:
            return("Position is out of range")

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next != None:
            temp.next.prev = new_node

        temp.next = new_node

    def reverse(self):
        curr = self.head

        while curr != None:
            curr.prev, curr.next = curr.next, curr.prev
            self.head = curr
            curr = curr.prev

    def print(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")
    def count_occurence(self,value):
        temp = self.head
        a = 0
        while temp!=None:
            if temp.data == value:
                a+=1
            temp=temp.next
        print(a)
        return


list1 = sll()
list1.append(node(10))
list1.append(node(20))
list1.append(node(30))
list1.append(node(40))
list1.append(node(30))
list1.insert(node(400), 2)

list1.delete(100)
list1.delete(10)

list1.print()
list1.reverse()
list1.print()
list1.count_occurence(30)