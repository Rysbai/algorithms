import sys

prev_s = 0
p = 1000000001

sys.setrecursionlimit(100000)


class Node:
    key: int or None
    parent: 'Node' or None
    left: 'Node' or None
    right: 'Node' or None
    subtree_sum: int

    def __init__(self, key: int = None, parent: 'Node' = None,
                 left: 'Node' = None, right: 'Node' = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.subtree_sum = 0

    def search(self, key: int):
        stopped_node, is_found = self._search(key)

        print('Found' if is_found else 'Not found')
        return self._splay(stopped_node)

    def add(self, key) -> 'Node':
        if not self.key:
            self.key = key
            return self

        stopped_node, is_found = self._search(key)
        if is_found:
            return self._splay(stopped_node)

        side = 'left' if key < stopped_node.key else 'right'

        replace_node = stopped_node.__getattribute__(side)
        new_node = Node(key=key, **{side: replace_node})
        stopped_node.__setattr__(side, new_node)
        new_node.parent = stopped_node

        if replace_node:
            replace_node.parent = new_node

        new_node.update_subtree_sum()
        self._msg_parents_subtree_sum(new_node, amount=new_node.key, operator='+')
        return self._splay(new_node)

    def remove(self, key) -> 'Node':
        node = self
        new_root = None

        if node.key is None:
            return node

        if not node.left and not node.right and node.key == key:
            node.key = None
            return node

        stopped_node, is_found = self._search(key)
        if is_found:
            node = self._splay(stopped_node)
            if node.right:
                node.right.parent = None
            if node.left:
                node.left.parent = None
            else:
                return node.right

            new_root = self._merge(node.left, node.right)

        return new_root if new_root else self._splay(stopped_node)

    def section_sum2(self, left: int, right: int):
        global prev_s
        generic_root = self
        while True:
            if not generic_root.key:
                break

            if left <= generic_root.key <= right:
                break

            if generic_root.left and generic_root.left.key > left:
                generic_root = generic_root.left
                continue

            if generic_root.right and generic_root.right.key < right:
                generic_root = generic_root.right
                continue

            break
        generic_root = self._splay(generic_root)
        s = generic_root._section_sum(left, right)
        prev_s = s
        print(s)

        return self

    def section_sum(self, left: int, right: int):
        global prev_s
        l_node, _ = self._search(left)
        s = 0
        next_node = l_node
        while True:
            if not next_node or not next_node.key:
                break

            if next_node.key < left:
                next_node = self._next_node(next_node)
                continue

            if next_node.key > right:
                break

            s += next_node.key

            next_node = self._next_node(next_node)
        print(s)
        prev_s = s
        return self

    def _section_sum(self, left: int, right: int) -> int:
        s = 0
        if not self.key:
            return s

        if left <= self.key <= right:
            s += self.key

        if self.key > left and self.left:
            s += self.left._section_sum(left, right)

        if self.key < right and self.right:
            s += self.right._section_sum(left, right)

        return s

    @staticmethod
    def _next_node(node: 'Node') -> 'Node' or None:
        if node.right:
            return node.right.min()

        while True:
            if not node.parent:
                return None

            if node.parent.left == node:
                return node.parent

            node = node.parent

    @staticmethod
    def _msg_parents_subtree_sum(node: 'Node', amount: int, operator: str) -> None:
        parent = node.parent
        while parent:
            if operator == '+':
                parent.subtree_sum += amount
            else:
                parent.subtree_sum -= amount

            parent = parent.parent

    def _search(self, s_key) -> ('Node', bool):
        if self.key is None:
            return self, False

        node = self

        while True:
            if s_key == node.key:
                return node, True

            if s_key < node.key and node.left:
                node = node.left
                continue

            if s_key > node.key and node.right:
                node = node.right
                continue

            return node, False

    def _splay(self, node: 'Node') -> 'Node':
        while True:
            if node.parent is None:
                return node

            side = 'left' if node.parent.left == node else 'right'

            if node.parent.parent is None:
                node = self._zig(node, side=side)
                continue

            if node.parent.parent.__getattribute__(side) == node.parent:
                node = self._zig_zig(node, side=side)
            else:
                node = self._zig_zag(node, side=side)

    def _merge(self, l_node: 'Node', r_node: 'Node') -> 'Node':
        l_node = self._splay(l_node.max())
        l_node.right = r_node
        if r_node:
            r_node.parent = l_node

        return l_node

    def max(self) -> 'Node':
        node = self
        while True:
            if node.right:
                node = node.right
                continue
            break

        return node

    def min(self) -> 'Node':
        node = self
        while True:
            if node.left:
                node = node.left
                continue
            break

        return node

    @staticmethod
    def _zig_zig(node: 'Node', side: str) -> 'Node':
        opposite_side = 'right' if side == 'left' else 'left'
        c_parent = node.parent
        c_grandpa = c_parent.parent
        c_great_grandpa = c_grandpa.parent

        # current grandpa
        c_parent_op_child = c_parent.__getattribute__(opposite_side)
        c_grandpa.__setattr__(side, c_parent_op_child)
        if c_parent_op_child:
            c_parent_op_child.parent = c_grandpa
        c_grandpa.parent = c_parent

        # current parent
        c_parent.__setattr__(opposite_side, c_grandpa)
        c_node_op_child = node.__getattribute__(opposite_side)
        c_parent.__setattr__(side, c_node_op_child)
        if c_node_op_child:
            c_node_op_child.parent = c_parent
        c_parent.parent = node

        # current node
        node.__setattr__(opposite_side, c_parent)
        node.parent = c_great_grandpa
        if c_great_grandpa:
            if c_great_grandpa.left == c_grandpa:
                c_great_grandpa.left = node
            else:
                c_great_grandpa.right = node

        c_grandpa.update_subtree_sum()
        c_parent.update_subtree_sum()
        node.update_subtree_sum()

        return node

    def update_subtree_sum(self):
        s = 0
        if self.left:
            s += self.left.subtree_sum + self.left.key

        if self.right:
            s += self.right.subtree_sum + self.right.key

        self.subtree_sum = s

    @staticmethod
    def _zig_zag(node: 'Node', side: str) -> 'Node':
        opposite_side = 'right' if side == 'left' else 'left'
        c_parent = node.parent
        c_grandpa = c_parent.parent
        c_great_grandpa = c_grandpa.parent

        # current grandpa
        c_node_side_child = node.__getattribute__(side)
        c_grandpa.__setattr__(opposite_side, c_node_side_child)
        if c_node_side_child:
            c_node_side_child.parent = c_grandpa
        c_grandpa.parent = node

        # current parent
        c_node_op_child = node.__getattribute__(opposite_side)
        c_parent.__setattr__(side, c_node_op_child)
        if c_node_op_child:
            c_node_op_child.parent = c_parent
        c_parent.parent = node

        # current node
        node.__setattr__(side, c_grandpa)
        node.__setattr__(opposite_side, c_parent)
        node.parent = c_great_grandpa
        if c_great_grandpa:
            if c_great_grandpa.left == c_grandpa:
                c_great_grandpa.left = node
            else:
                c_great_grandpa.right = node

        c_grandpa.update_subtree_sum()
        c_parent.update_subtree_sum()
        node.update_subtree_sum()

        return node

    @staticmethod
    def _zig(node: 'Node', side: str) -> 'Node':
        opposite_side = 'right' if side == 'left' else 'left'
        c_parent = node.parent
        c_grandpa = c_parent.parent

        c_node_op_side = node.__getattribute__(opposite_side)
        c_parent.__setattr__(side, c_node_op_side)
        if c_node_op_side:
            c_node_op_side.parent = c_parent

        node.__setattr__(opposite_side, c_parent)
        c_parent.parent = node
        node.parent = c_grandpa
        if c_grandpa:
            if c_grandpa.left and c_grandpa.left.key == c_parent.key:
                node.parent.left = node
            elif c_grandpa.right and c_grandpa.right.key == c_parent.key:
                node.parent.right = node

        c_parent.update_subtree_sum()
        node.update_subtree_sum()
        return node

    def __str__(self, level=0, side='root'):
        ret = '\t'*level + f'{side}: ' + \
              str(self.key) + \
              f', parent: {self.parent and self.parent.key}, subtree_sum: {self.subtree_sum}' '\n'
        if self.left:
            ret += self.left.__str__(level + 1, 'left')

        if self.right:
            ret += self.right.__str__(level + 1, 'right')

        return ret


operators = {
    '+': 'add',
    '-': 'remove',
    '?': 'search',
    's': 'section_sum2'
}


def main():
    func = lambda x: (x % p + prev_s % p) % 1000000001
    n = int(input())
    node = Node()
    for _ in range(n):
        code, *params = input().split()
        node = node.__getattribute__(operators[code])(*[func(int(i)) for i in params])


def test_section_sum():
    ten = Node(key=10)
    eight = Node(key=8, right=ten)
    ten.parent = eight
    five = Node(key=5)
    seven = Node(key=7, left=five, right=eight)
    eight.parent = seven
    five.parent = seven

    root = Node(key=15, left=seven)
    seven.parent = root

    root.section_sum2(4, 9)
