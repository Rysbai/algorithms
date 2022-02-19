from collections import namedtuple

Node = namedtuple('Node', ['key', 'left', 'right'])


class SearchTree(list):
    prev: Node = None

    def in_order_check(self, node: Node):
        if node.left != -1:
            self.in_order_check(self[node.left])

        if self.prev and self.prev.key > node.key:
            raise TypeError('Search tree isnt correct!')

        self.prev = node

        if node.right != -1:
            self.in_order_check(self[node.right])

        return node

    def is_correct(self, node: Node, min_v: int = None, max_v: int = None):
        left = float('-inf') if node.left == -1 else self[node.left].key
        right = float('inf') if node.right == -1 else self[node.right].key

        if min_v and node.key < min_v:
            return False
        if max_v and node.key > max_v:
            return False

        if node.key < left or node.key > right:
            return False

        left_child_params = {
            'min_v': min_v or float('-inf'),
            'max_v': node.key
        }
        right_child_params = {
            'min_v': node.key,
            'max_v': max_v or float('inf')
        }

        if node.left != -1 and not self.is_correct(self[node.left], **left_child_params):
            return False

        if node.right != -1 and not self.is_correct(self[node.right], **right_child_params):
            return False

        return True


if __name__ == '__main__':
    n = int(input())
    tree = SearchTree()
    for _ in range(n):
        key, left, right = [int(i) for i in input().split()]
        tree.append(Node(key=key, left=left, right=right))

    try:
        if tree:
            tree.in_order_check(tree[0])
        print('CORRECT')
    except TypeError:
        print('INCORRECT')
