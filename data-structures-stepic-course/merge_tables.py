class TablesTree(list):
    max_amount = 0

    def __init__(self, string: str, *args, **kwargs):
        super(TablesTree, self).__init__(*args, **kwargs)
        for i, x in enumerate(string.split(' ')):
            amount = int(x)
            self.append([i, amount])

            if amount > self.max_amount:
                self.max_amount = amount

    def parent(self, i: int) -> int:
        return self[i][0]

    def find_top_index(self, i: int) -> int:
        if i != self.parent(i):
            parent_index = self.find_top_index(self.parent(i))
            self[i][0] = parent_index
            return parent_index

        return self.parent(i)

    def merge(self, des: int, source: int) -> None:
        des_i = self.find_top_index(des - 1)
        source_i = self.find_top_index(source - 1)

        if des_i != source_i:
            total = self[des_i][1] + self[source_i][1]
            self[source_i][0] = des_i
            self[des_i][1] = total

            if total > self.max_amount:
                self.max_amount = total


n, m = 5, 5
tables = '1 1 1 1 1'

merges = """
3 5
2 4
1 4
5 4
5 3
"""

merges = [x for x in merges.split('\n') if x]

table_tree = TablesTree(tables)
for i in range(n):
    destination, source = (int(x) for x in merges[i].split(' '))
    table_tree.merge(destination, source)
