class HuffmanTree:
    def __init__(self, value=None, priority=0):
        self.value = value
        self.priority = priority
        self.right = None
        self.left = None

    def set_right_and_left(self, right, left):
        self.right = right
        self.left = left

    def walk_to_encode(self, codes, acc=""):
        if self.value is not None:
            codes[self.value] = acc or "0"
        if self.left is not None:
            self.left.walk_to_encode(codes, acc + "1")
        if self.right is not None:
            self.right.walk_to_encode(codes, acc + "0")

    def __str__(self):
        return str(self.priority)


class MinHeap:
    def __init__(self, huffman_trees=None):
        if huffman_trees is None:
            huffman_trees = []
        self.array = huffman_trees

    def insert(self, huffman_tree):
        self.array.append(huffman_tree)
        self._sift_up()

    def _sift_up(self):
        assert self.array
        last_elem = self.array[-1]
        index = len(self.array) - 1
        if index == 0:
            return
        parent_index = (index - 1) // 2
        parent = self.array[parent_index]
        while index > 0 and parent.priority > last_elem.priority:
            self.array[parent_index] = last_elem
            self.array[index] = parent
            index = parent_index
            parent_index = (index - 1) // 2
            parent = self.array[parent_index]

    def pop(self):
        min_elem = None
        if self.array:
            min_elem = self.array[0]
            self.array[0] = self.array[-1]
            del self.array[-1]
            if len(self.array) > 1:
                self._sift_down()

        return min_elem

    def _sift_down(self):
        assert len(self.array) > 1
        first_elem = self.array[0]
        elem_index = 0
        child1_index = 1
        child2_index = 2

        min_child, index_min_child = self.find_min_child(child1_index, child2_index)
        while min_child is not None and index_min_child is not None and min_child.priority < first_elem.priority:
            self.array[index_min_child] = first_elem
            self.array[elem_index] = min_child
            elem_index = index_min_child
            child1_index = elem_index * 2 + 1
            child2_index = elem_index * 2 + 2
            min_child, index_min_child = self.find_min_child(child1_index, child2_index)

    def find_min_child(self, child1_index, child2_index):
        assert len(self.array) > 1
        if child2_index >= len(self.array):
            if child1_index >= len(self.array):
                return None, None
            return self.array[child1_index], child1_index

        child1 = self.array[child1_index]
        child2 = self.array[child2_index]

        if child1.priority < child2.priority:
            return child1, child1_index
        else:
            return child2, child2_index


class Encoder:
    def __init__(self, s):
        self.string = s
        self.codes = {}

    def encode(self):
        heap = self._make_frequencies_heap()
        while len(heap.array) > 1:
            first_min = heap.pop()
            second_min = heap.pop()
            tree = HuffmanTree(None, first_min.priority
                               + second_min.priority)
            tree.set_right_and_left(first_min, second_min)
            heap.insert(tree)
        tree = heap.array[0]
        tree.walk_to_encode(self.codes)
        return self.codes, "".join(self.codes[x] for x in self.string)

    def _make_frequencies_heap(self):
        heap = MinHeap()
        frequencies = {}
        for letter in self.string:
            if letter not in frequencies:
                frequencies[letter] = 1
            else:
                frequencies[letter] += 1
        for k, value in frequencies.items():
            heap.insert(HuffmanTree(k, value))

        return heap


class Decoder:
    def __init__(self, key):
        self.key = key

    def decode(self, s):
        tree = self._make_tree()
        decoded = ''
        pointer = tree

        for letter in s:
            if letter == '0':
                pointer = pointer.right
                if pointer.value is not None:
                    decoded += pointer.value
                    pointer = tree
            elif letter == '1':
                pointer = pointer.left
                if pointer.value is not None:
                    decoded += pointer.value
                    pointer = tree
        return decoded

    def _make_tree(self):
        tree = HuffmanTree()
        pointer = tree
        for k, v in self.key.items():
            for letter in v:
                node = HuffmanTree()
                if letter == '1':
                    if pointer.left is None:
                        pointer.left = node
                    pointer = pointer.left
                elif letter == '0':
                    if pointer.right is None:
                        pointer.right = node
                    pointer = pointer.right
            pointer.value = k
            pointer = tree
        return tree


s = input()
encoder = Encoder(s)
key, encoded = encoder.encode()
decoder = Decoder(key)
print(encoded)
print(decoder.decode(encoded))
