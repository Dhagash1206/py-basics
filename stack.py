# Stack class using OOP
class Stack:
    def __init__(self):
        self.stack = []

    # Push element onto stack
    def push(self, data):
        self.stack.append(data)
        print(f"{data} pushed to stack.")

    # Pop element from stack
    def pop(self):
        if not self.stack:
            print("Stack is empty! Nothing to pop.")
            return
        popped = self.stack.pop()
        print(f"{popped} popped from stack.")

    # Peek top element
    def peek(self):
        if not self.stack:
            print("Stack is empty.")
            return
        print(f"Top element: {self.stack[-1]}")

    # Display stack
    def display(self):
        if not self.stack:
            print("Stack is empty.")
            return
        print("Stack elements (top to bottom):")
        for item in reversed(self.stack):
            print(item)


stack = Stack()

while True:
    print("\n===== Stack Menu =====")
    print("1. Push element")
    print("2. Pop element")
    print("3. Peek top element")
    print("4. Display stack")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        data = int(input("Enter element to push: "))
        stack.push(data)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.peek()
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
