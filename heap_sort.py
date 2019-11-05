from comparators import default_comparator


class Heap:
    def __init__(self, array=None, comparator=default_comparator, reverse=False):
        if array is None:
            array = []
        self.heap = array
        self.comparator = comparator
        self.size = len(array)
        self.sign = -1 if reverse else 1

    def insert(self, value):
        self.heap.append(value)
        if len(self.heap) > 1:
            self._sift_up()
        self.size += 1

    def _sift_up(self):
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2
        while index > 0 and self.sign * self.comparator(self.heap[index], self.heap[parent_index]) > 0:
            tmp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = tmp
            index = parent_index
            parent_index = (index - 1) // 2

    def pop(self):
        assert self.heap
        elem = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap[self.size - 1] = elem
        self.size -= 1
        if self.size > 1:
            self._sift_down()

    def _sift_down(self, index=0):
        item = self.heap[index]
        child1_index = 1
        child2_index = 2
        child, child_index = self._find_child_and_index(child1_index, child2_index)
        while child is not None and child_index is not None and self.sign * self.comparator(item, child) < 0:
            self.heap[index] = child
            self.heap[child_index] = item
            index = child_index
            child1_index = 2 * index + 1
            child2_index = 2 * index + 2
            child, child_index = self._find_child_and_index(child1_index, child2_index)

    def _find_child_and_index(self, index1, index2):
        if index2 >= self.size:
            if index1 >= self.size:
                return None, None
            return self.heap[index1], index1

        child1 = self.heap[index1]
        child2 = self.heap[index2]

        if self.sign * self.comparator(child1, child2) > 0:
            return child1, index1
        else:
            return child2, index2


def heap_sort(array, comparator=default_comparator, reverse=False):
    heap = Heap(comparator=comparator, reverse=reverse)
    for n in array:
        heap.insert(n)
    while heap.size > 1:
        heap.pop()
    return heap.heap


a = list(map(int, input().split()))
print(heap_sort(a))
