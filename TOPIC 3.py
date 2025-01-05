class SkillQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def enqueue(self, lesson):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue is full. Cannot add more lessons.")
            return
        elif self.front == -1:  
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = lesson
        print(f"Lesson '{lesson}' added to the queue.")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty. No lessons to process.")
            return None
        lesson = self.queue[self.front]
        if self.front == self.rear:  
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        print(f"Lesson '{lesson}' processed and removed from the queue.")
        return lesson

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        print("Current lessons in the queue:")
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.max_size
        print()

if __name__ == "__main__":
    print("Welcome to the Skill Learning Queue!")
    max_size = int(input("Enter the maximum size of the queue: "))
    sq = SkillQueue(max_size)

    while True:
        print("\nMenu:")
        print("1. Add a lesson to the queue")
        print("2. Process a lesson from the queue")
        print("3. Display the current queue")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            lesson = input("Enter the name of the lesson to add: ")
            sq.enqueue(lesson)
        elif choice == "2":
            sq.dequeue()
        elif choice == "3":
            sq.display()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
