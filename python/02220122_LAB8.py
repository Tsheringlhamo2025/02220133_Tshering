# Part 1- AVL tree implementation (02220122)

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0 

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def search(self, value):
        return self._search(self.root, value)

    def get_height(self):
        return self._get_height(self.root)

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _insert(self, node, value):
        if not node:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and value < node.left.value:  # LL
            return self._right_rotate(node)
        if balance < -1 and value > node.right.value:  # RR
            return self._left_rotate(node)
        if balance > 1 and value > node.left.value:  # LR
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and value < node.right.value:  # RL
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _delete(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:  # LL
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:  # LR
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:  # RR
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:  # RL
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def _is_balanced(self, node):
        if not node:
            return True
        left_balanced = self._is_balanced(node.left)
        right_balanced = self._is_balanced(node.right)
        return abs(self._get_balance(node)) <= 1 and left_balanced and right_balanced

    # Tree Printer (correct alignment)
    def print_tree(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        if node is None:
            return [" "], 1, 1, 0

        line = str(node.value)
        width = len(line)

        if node.left is None and node.right is None:
            return [line], width, 1, width // 2

        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + line
            second_line = x * " " + "/" + (n - x - 1 + width) * " "
            shifted_lines = [line + width * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + width, p + 2, n + width // 2

        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            first_line = line + x * "_" + (n - x) * " "
            second_line = (width + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [width * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + width, p + 2, width // 2

        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + line + y * "_" + (m - y) * " "
        second_line = x * " " + "/" + (n - x - 1 + width + y) * " " + "\\" + (m - y - 1) * " "
        if p < q:
            left += [" " * n] * (q - p)
        elif q < p:
            right += [" " * m] * (p - q)
        zipped_lines = zip(left, right)
        lines = [a + width * " " + b for a, b in zipped_lines]
        return [first_line, second_line] + lines, n + m + width, max(p, q) + 2, n + width // 2


# Example Usage
if __name__ == "__main__":
    avl = AVLTree()
    avl.insert(12)
    avl.insert(8)
    avl.insert(18)
    avl.insert(5)
    avl.insert(11)
    avl.insert(17)
    avl.insert(4)
    avl.insert(3)

    print("Is Balanced?", avl.is_balanced())  # True
    print("Tree Height:", avl.get_height())   # Height of the AVL Tree

    print("\nTree Structure:")
    avl.print_tree()

