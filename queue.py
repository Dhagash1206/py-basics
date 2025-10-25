# Queue class using OOP
class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue element (add at rear)
    def enqueue(self, data):
        self.queue.append(data)
        print(f"{data} added to queue.")

    # Dequeue element (remove from front)
    def dequeue(self):
        if not self.queue:
            print("Queue is empty! Nothing to dequeue.")
            return
        removed = self.queue.pop(0)
        print(f"{removed} removed from queue.")

    # Peek front element
    def peek(self):
        if not self.queue:
            print("Queue is empty.")
            return
        print(f"Front element: {self.queue[0]}")

    # Display queue
    def display(self):
        if not self.queue:
            print("Queue is empty.")
            return
        print("Queue elements (front to rear):")
        print(" -> ".join(map(str, self.queue)))

queue = Queue()

while True:
    print("\n===== Queue Menu =====")
    print("1. Enqueue element")
    print("2. Dequeue element")
    print("3. Peek front element")
    print("4. Display queue")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        data = int(input("Enter element to enqueue: "))
        queue.enqueue(data)
    elif choice == '2':
        queue.dequeue()
    elif choice == '3':
        queue.peek()
    elif choice == '4':
        queue.display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
