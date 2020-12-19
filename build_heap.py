n = int(input())


A = (int(x) for x in input().split(' '))


class Heap(list):
    size = 0
    switches = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = len(self)

    def make_heap(self):
        for i in range(int(self.size / 2), -1, -1):
            self.shift_down(i)

    def shift_up(self, i: int):
        while i > 1 and self[self.parent_index(i)] > self[i]:
            self.swap(i, self.parent_index(i))
            i = self.parent_index(i)

    def shift_down(self, i: int):
        max_index = i
        left_index = self.left_child(i)

        if left_index <= self.size - 1 and self[left_index] < self[max_index]:
            max_index = left_index

        right_child = self.right_child(i)
        if right_child <= self.size - 1 and self[right_child] < self[max_index]:
            max_index = right_child

        if max_index > i:
            self.swap(i, max_index)
            self.shift_down(max_index)

    def swap(self, i: int, j: int):
        self.switches.append(f'{i} {j}')
        self[i], self[j] = self[j], self[i]

    def parent_index(self, i: int) -> int:
        return int(2 / i)

    def left_child(self, i: int) -> int:
        return i*2 + 1

    def right_child(self, i: int) -> int:
        return (i * 2) + 2

    def has_child(self, i) -> bool:
        left_child = self.left_child(i)
        right_child = self.right_child(i)

        if left_child <= self.size - 1:
            return True

        if right_child <= self.size - 1:
            return True

        return False


a = Heap('5 4 3 2 1'.split(' '))
a.make_heap()
print(len(a.switches))
print(*a.switches, sep='\n')
