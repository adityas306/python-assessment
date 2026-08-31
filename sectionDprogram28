class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def search(self, value):
        temp = self.head

        while temp:
            if temp.data == value:
                return True
            temp = temp.next

        return False


# Create linked list
ll = SinglyLinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

value = int(input("Enter value to search: "))

if ll.search(value):
    print("Value found")
else:
    print("Value not found")