#Task1

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is None:
            self.root = None
            print("Created new Binary Tree\nRoot: None")
        else:
            self.root = Node(root_value)
            print(f"Created new Binary Tree\nRoot: {self.root.value}")

# Example usage
tree = BinaryTree()

#Task2

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def height(self, node):
        if node is None:
            return -1  # If no nodes, height is -1
        return max(self.height(node.left), self.height(node.right)) + 1

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node):
        if node is None:
            return True  # An empty tree is full
        if (node.left is None and node.right is None):
            return True
        if node.left and node.right:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False  # If one child is missing

    def is_complete_binary_tree(self):
        if self.root is None:
            return True

        queue = [(self.root, 1)]
        index = 0
        while queue:
            node, pos = queue.pop(0)
            index += 1
            if pos != index:
                return False  # If positions mismatch, it's not complete

            if node.left:
                queue.append((node.left, pos * 2))
            if node.right:
                queue.append((node.right, pos * 2 + 1))

        return True

    def get_tree_info(self):
        print(f"Tree Height: {self.height(self.root)}")
        print(f"Total Nodes: {self.size(self.root)}")
        print(f"Leaf Nodes Count: {self.count_leaves(self.root)}")
        print(f"Is Full Binary Tree: {self.is_full_binary_tree(self.root)}")
        print(f"Is Complete Binary Tree: {self.is_complete_binary_tree()}")

# Example Usage
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.get_tree_info()

