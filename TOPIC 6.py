class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 2 + self.data)
        for child in self.children:
            child.display(level + 1)

    def find_node(self, data):
        """Recursively find a node in the tree."""
        if self.data == data:
            return self
        for child in self.children:
            result = child.find_node(data)
            if result:
                return result
        return None


def insert_node(root):
    """Allow user to insert a node in the tree."""
    parent_data = input("Enter the name of the parent node: ")
    parent_node = root.find_node(parent_data)
    if not parent_node:
        print(f"Parent node '{parent_data}' not found. Please try again.")
        return
    new_node_data = input("Enter the name of the new node to add: ")
    new_node = TreeNode(new_node_data)
    parent_node.add_child(new_node)
    print(f"Node '{new_node_data}' added under parent '{parent_data}'.")

if __name__ == "__main__":
    root = TreeNode("Lessons")
    coding = TreeNode("Coding")
    design = TreeNode("Design")
    root.add_child(coding)
    root.add_child(design)
    python_skill = TreeNode("Python")
    web_design = TreeNode("Web Design")
    coding.add_child(python_skill)
    design.add_child(web_design)
    
    while True:
        print("\nCurrent Tree:")
        root.display()
        print("\nOptions: ")
        print("1. Add Node")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            insert_node(root)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
