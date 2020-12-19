from collections import namedtuple

Node = namedtuple('Node', ['key', 'left', 'right'])


class Tree(list):
    def in_order_detour(self, node: Node):
        if node.left != -1:
            yield from self.in_order_detour(self[node.left])
        yield node.key
        if node.right != -1:
            yield from self.in_order_detour(self[node.right])

    def pre_order_detour(self, node: Node):
        yield node.key
        if node.left != -1:
            yield from self.pre_order_detour(node)
        if node.right != -1:
            yield from self.pre_order_detour(node)

    def post_order_detour(self, node: Node):
        if node.left != -1:
            yield from self.post_order_detour(node)
        if node.right != -1:
            yield from self.post_order_detour(node)

        yield node.key


def main():
    n = int(input())
    tree = Tree()
    for _ in range(n):
        key, left, right = [int(i) for i in input().split()]
        tree.append(Node(key=key, left=left, right=right))

    print(*list(tree.in_order_detour(tree[0])), sep=' ')
    print(*list(tree.pre_order_detour(tree[0])), sep=' ')
    print(*list(tree.post_order_detour(tree[0])), sep=' ')
