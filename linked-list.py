# Node class
class Node:
    def __init__(self, data):
        self.data = data      # Data field
        self.next = None      # Pointer to next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None      # Initialize empty list

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

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # If head node holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return  # Key not found

        prev.next = current.next
        current = None

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()

while True:
    print("\n===== Singly Linked List Menu =====")
    print("1. Append element")
    print("2. Prepend element")
    print("3. Delete element")
    print("4. Display list")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        data = int(input("Enter element to append: "))
        ll.append(data)
        print(f"{data} appended.")
    elif choice == '2':
        data = int(input("Enter element to prepend: "))
        ll.prepend(data)
        print(f"{data} prepended.")
    elif choice == '3':
        key = int(input("Enter element to delete: "))
        ll.delete(key)
    elif choice == '4':
        print("Linked List: ", end="")
        ll.display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
