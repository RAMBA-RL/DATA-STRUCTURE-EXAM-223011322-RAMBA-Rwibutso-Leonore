def mergeSort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        mergeSort(left, key)
        mergeSort(right, key)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][key] <= right[j][key]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


def display_lessons(lessons):
    print("\nCurrent Lessons:")
    for lesson in lessons:
        print(f"Lesson: {lesson['lesson']}, Priority: {lesson['priority']}")
    print()


def add_lesson(lessons):
    lesson_name = input("Enter the lesson name: ")
    priority = int(input("Enter the priority (integer value): "))
    lessons.append({"lesson": lesson_name, "priority": priority})
    print(f"Added lesson: {lesson_name} with priority {priority}.\n")

if __name__ == "__main__":
    lessons = [
        {"lesson": "Learn Python", "priority": 3},
        {"lesson": "Design a Logo", "priority": 2},
        {"lesson": "Build a Website", "priority": 1},
        {"lesson": "Learn Data Structures", "priority": 4},
    ]

    while True:
        print("\nOptions:")
        print("1. Display Lessons")
        print("2. Add New Lesson")
        print("3. Sort Lessons by Priority")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_lessons(lessons)
        elif choice == "2":
            add_lesson(lessons)
        elif choice == "3":
            mergeSort(lessons, key="priority")
            print("Lessons sorted by priority.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
