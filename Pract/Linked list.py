class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class sll:
    def __init__(self):
        self.head = None

    # Create the list by adding nodes at the end
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    # Traverse and print
    def print(self):
        if self.head == None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Insert at a specific position (starting from 1)
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head

            while temp != None and p < pos - 1:
                temp = temp.next
                p += 1

            if temp == None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

    # Find middle node
    def middle(self):
        if self.head == None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # Delete the first node containing the given value
    def delete(self, value):
        temp = self.head
        prev = None

        if temp == None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = self.head.next
        else:
            while temp != None and temp.data != value:
                prev = temp
                temp = temp.next

            if temp == None:
                print("Value is not present in the list")
                return

            prev.next = temp.next

    # Reverse the list
    def reverse(self):
        temp = self.head
        prev = None

        while temp:
            next_node = temp.next  # Save the next node
            temp.next = prev      # Reverse the link
            prev = temp           # Move prev forward
            temp = next_node      # Move temp forward

        self.head = prev

    # Sum of every two consecutive nodes
    def consecutive_sum(self):
        if self.head == None or self.head.next == None:
            print("At least two nodes are required")
            return

        temp = self.head

        while temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


# Create linked list
list1 = sll()

n1 = node(10)
n2 = node(20)

list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(40))
list1.append(node(50))

print("Original list:")
list1.print()

print("\nAfter inserting 400 at position 2:")
list1.insert(node(400), 2)
list1.print()

print("\nMiddle node:")
list1.middle()

print("\nAfter deleting 10:")
list1.delete(10)
list1.print()

print("\nAfter reversing:")
list1.reverse()
list1.print()

print("\nSum of consecutive nodes:")
list1.consecutive_sum()