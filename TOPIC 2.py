class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def getHeight(self, node):
        return node.height if node else 0

    def getBalance(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0

    def rotateRight(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def rotateLeft(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insert(self, root, key, value):
        if not root:
            return AVLNode(key, value)
        if key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rotateRight(root)
        if balance < -1 and key > root.right.key:
            return self.rotateLeft(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def preOrder(self, root):
        if root:
            print(f"Node: {root.key}, Value: {root.value}, Height: {root.height}")
            if root.left:
                print(f"Edge: {root.key} -> {root.left.key} (Left)")
            if root.right:
                print(f"Edge: {root.key} -> {root.right.key} (Right)")
            self.preOrder(root.left)
            self.preOrder(root.right)


avl = AVLTree()
root = None

while True:
    choice = input("Do you want to add a lesson to your schedule? (yes/no): ").strip().lower()
    if choice == 'yes':
        key = int(input("Enter code for lesson (integer): "))
        value = input("Enter name of lesson(string): ")
        root = avl.insert(root, key, value)
    else:
        break

print("\nAVL Tree (Nodes, Edges, and Heights):")
avl.preOrder(root)
print()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue("Learn Python")
q.enqueue("Learn JavaScript")
q.enqueue("Learn Algorithm")
print("Queue Size:", q.size())
print("Dequeued:", q.dequeue())
print("Queue Size after dequeue:", q.size())
