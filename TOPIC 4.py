class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.max_size
        print()


def main():
    print("Welcome to the Circular Queue for Learning New Skills!")
    max_size = int(input("Enter the maximum size of the queue: "))
    cq = CircularQueue(max_size)

    while True:
        print("\nMenu:")
        print("1. Add a new lesson to the queue")
        print("2. Remove the oldest lesson from the queue")
        print("3. Display all lessons in the queue")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            lesson = input("Enter the name of the lesson to add: ")
            cq.enqueue(lesson)
        elif choice == 2:
            removed = cq.dequeue()
            if removed:
                print(f"Removed lesson: {removed}")
        elif choice == 3:
            print("Current lessons in the queue:")
            cq.display()
        elif choice == 4:
            print("Exiting the application. Happy Learning!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
