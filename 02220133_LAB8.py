#02220133-PART2

class Node:
    def __init__(self, value, color="red"):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(None, color="black")
        self.TNULL.left = self.TNULL.right = self.TNULL.parent = self.TNULL
        self.root = self.TNULL

    def insert(self, value):
        node = Node(value)
        node.left = node.right = node.parent = self.TNULL

        parent = self.TNULL
        current = self.root

        while current != self.TNULL:
            parent = current
            if node.value < current.value:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent == self.TNULL:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        if node.parent == self.TNULL:
            node.color = "black"
            return

        if node.parent.parent == self.TNULL:
            return

        self._fix_insert(node)

    def _fix_insert(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.TNULL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.TNULL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, value):
        node = self.root
        while node != self.TNULL:
            if node.value == value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def get_black_height(self):
        node = self.root
        height = 0
        while node != self.TNULL:
            if node.color == "black":
                height += 1
            node = node.left
        return height

    def _minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def delete(self, value):
        node = self.root
        while node != self.TNULL:
            if node.value == value:
                break
            node = node.left if value < node.value else node.right
        if node == self.TNULL:
            return
        self._delete_node(node)

    def _delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "black":
            self._fix_delete(x)

    def _transplant(self, u, v):
        if u.parent == self.TNULL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "red":
                    s.color = "black"
                    x.parent.color = "red"
                    self._left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == "black" and s.right.color == "black":
                    s.color = "red"
                    x = x.parent
                else:
                    if s.right.color == "black":
                        s.left.color = "black"
                        s.color = "red"
                        self._right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = "black"
                    s.right.color = "black"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "red":
                    s.color = "black"
                    x.parent.color = "red"
                    self._right_rotate(x.parent)
                    s = x.parent.left
                if s.left.color == "black" and s.right.color == "black":
                    s.color = "red"
                    x = x.parent
                else:
                    if s.left.color == "black":
                        s.right.color = "black"
                        s.color = "red"
                        self._left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = "black"
                    s.left.color = "black"
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def print_tree(self):
        def _print_helper(node, indent, last):
            if node != self.TNULL:
                print(indent, end="")
                if last:
                    print("R----", end="")
                    indent += "     "
                else:
                    print("L----", end="")
                    indent += "|    "
                print(f"{node.value}({'B' if node.color == 'black' else 'R'})")
                _print_helper(node.left, indent, False)
                _print_helper(node.right, indent, True)
        
        if self.root != self.TNULL:
            _print_helper(self.root, "", True)
        else:
            print("Empty tree")

# Example usage:
rb = RedBlackTree()
rb.insert(55)
rb.insert(40)
rb.insert(65)
rb.insert(60)
rb.insert(75)
rb.insert(57)

print("Initial tree:")
rb.print_tree()
print("Black Height:", rb.get_black_height())

print("\nAfter deleting 40:")
rb.delete(40)
rb.print_tree()
print("Black Height:", rb.get_black_height())

print("\nSearch for 60:", rb.search(60))
print("Search for 40:", rb.search(40))
  