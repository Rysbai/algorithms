from collections import namedtuple

Node = namedtuple('Node', ['key', 'left', 'right'])


class SearchTree(list):
    prev: Node = None
    prev_i = 0

    def in_order_check(self, node: Node):
        if node.left != -1:
            self.in_order_check(self[node.left])

        if self.prev and self.prev.key > node.key:
            raise TypeError('Search tree isnt correct!')

        elif self.prev and self.prev.key == node.key and node.left == self.prev_i:
            raise TypeError('Search tree isnt correct!')

        self.prev = node
        self.prev_i += 1

        if node.right != -1:
            self.in_order_check(self[node.right])

        return node


data = """
2 1 2
2 -1 -1
3 -1 -1
"""

if __name__ == '__main__':
    n = int(input())
    tree = SearchTree()
    for row in data.split('\n'):
        if not row: continue

        key, left, right = [int(i) for i in row.split()]
        tree.append(Node(key=key, left=left, right=right))

    try:
        if tree:
            tree.in_order_check(tree[0])
        print('CORRECT')
    except TypeError:
        print('INCORRECT')
