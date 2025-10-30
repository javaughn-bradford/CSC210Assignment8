# que.py
# A First In First Out (FIFO) queue

from sequential_collection import SequentialCollection


class Queue(SequentialCollection):
    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty:
            raise IndexError("pop from empty queue")
        return self._data.pop(0)

    def peek(self):
        if self.is_empty:
            raise IndexError("peek from empty queue")
        return self._data[0]
