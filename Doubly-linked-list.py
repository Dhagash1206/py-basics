# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # Case 1: Deleting the head node
        if current and current.data == key:
            if current.next:
                current.next.prev = None
            self.head = current.next
            current = None
            return

        # Traverse and find the node
        while current and current.data != key:
            current = current.next

        # Node not found
        if current is None:
            print(f"{key} not found in list!")
            return

        # Case 2: Deleting middle or last node
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

        current = None

    # Display list forward
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Display list backward
    def display_backward(self):
        current = self.head
        if current is None:
            print("List is empty")
            return
        # Move to the end
        while current.next:
            current = current.next
        # Traverse backward
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


dll = DoublyLinkedList()

while True:
    print("\n===== Doubly Linked List Menu =====")
    print("1. Append element")
    print("2. Prepend element")
    print("3. Delete element")
    print("4. Display forward")
    print("5. Display backward")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        data = int(input("Enter element to append: "))
        dll.append(data)
        print(f"{data} appended.")
    elif choice == '2':
        data = int(input("Enter element to prepend: "))
        dll.prepend(data)
        print(f"{data} prepended.")
    elif choice == '3':
        key = int(input("Enter element to delete: "))
        dll.delete(key)
    elif choice == '4':
        print("List (Forward): ", end="")
        dll.display_forward()
    elif choice == '5':
        print("List (Backward): ", end="")
        dll.display_backward()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
