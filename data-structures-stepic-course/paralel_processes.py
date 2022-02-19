

class ProcessManager(list):
    size = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = len(self)

    @staticmethod
    def build(n):
        return ProcessManager(([0, x] for x in range(n)))

    def get_max(self):
        return self[0]

    def add_task(self, t):
        processor = self.get_max()
        print(f'{processor[1]} {processor[0]}')

        processor[0] += t
        self.shift_down(0)

    def swap(self, i: int, j: int):
        self[i], self[j] = self[j], self[i]

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

    def left_child(self, i: int) -> int:
        return i*2 + 1

    def right_child(self, i: int) -> int:
        return (i * 2) + 2

    def parent_index(self, i: int) -> int:
        return int(2 / i)


process_manager = ProcessManager.build(2)
for t in (int(i) for i in '0 0 1 0 0 0 2 1 2 3 0 0 0 2 1'.split(' ')):
    process_manager.add_task(t)
