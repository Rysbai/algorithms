# n = 10
# array = [int(x) for x in "4 -1 4 1 1".split(' ')]
#
# enumerated_tree = list(enumerate(array))
#
#
# def height(r):
#     h = 1
#
#     for i in [j for j, x in enumerated_tree if x == r]:
#         h = max(h, 1 + height(i))
#
#     return h
#
#
# print(height(array.index(-1)))

n = 10
array = [int(x) for x in "4 -1 4 1 1".split(' ')]
enumerated_tree = list(enumerate(array))

length = 1

branches = {}
tops = []

for child, parent in enumerated_tree:
    if parent not in tops:
        tops.append(parent)
        branches[parent] = [child]
