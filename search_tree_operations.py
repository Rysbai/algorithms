
class Node:
    key: int
    parent: 'Node' or None
    left: 'Node' or None
    right: 'Node' or None
    is_empty: bool

    def __init__(self, key: int, parent: 'Node' = None,
                 left: 'Node' = None, right: 'Node' = None, is_empty: bool = False):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.is_empty = is_empty

    def search(self, s_key) -> ('Node', bool):
        if self.is_empty:
            return self, False

        node = self

        while True:
            if s_key == self.key:
                self.splay(node)
                return node, True

            if s_key < node.key and node.left:
                node = node.left
                continue

            if s_key > node.key and node.right:
                node = node.right
                continue

            return node, False

    def splay(self, node: 'Node') -> 'Node':
        while True:
            if node.parent is None:
                return node

            if node.parent.left == node:
                node = self.zig(node)
            else:
                node = self.zag(node)

    def add(self, key):
        if self.is_empty:
            pass
        stopped_node, is_found = self.search(key)
        if is_found:
            return

        replace_node = stopped_node.left
        new_node = Node(key=key, left=replace_node)
        stopped_node.left = new_node
        self.splay(new_node)

    def remove(self, key):
        node = self

        while True:
            if key == self.key:
                self.splay(node)
                self.merge(node.left, node.right)

            if key < node.key and node.left:
                node = node.left
                continue

            if key > node.key and node.right:
                node = node.right
                continue

            break

    def merge(self, l_node: 'Node', r_node: 'Node') -> 'Node':
        l_node = self.splay(l_node.max())
        l_node.right = r_node

        return l_node

    def max(self) -> 'Node':
        node = self
        while True:
            if node.right:
                node = node.right
                continue
            break

        return node

    def zig(self, node: 'Node') -> 'Node':
        current_parent = node.parent
        current_parent.left = node.right

        node.right = current_parent
        node.parent = current_parent.parent
        if node.parent:
            new_parent = node.parent
            if new_parent.left.key == current_parent.key:
                node.parent.left = node
            else:
                node.parent.right = node

        return node

    def zag(self, node: 'Node') -> 'Node':
        current_parent = node.parent
        current_parent.right = node.left

        node.left = current_parent
        node.parent = current_parent.parent
        if node.parent:
            new_parent = node.parent
            if new_parent.left.key == current_parent.key:
                node.parent.left = node
            else:
                node.parent.right = node
        return node


operators = {
    '+': 'add',
    '-': 'delete',
    '?': 'search',
    's': 'section_sum'
}


if __name__ == '__main__':
    n = int(input())
    node = None
    for _ in range(n):
        operator, *params = [int(i) for i in input().split()]
