# sequential_collection.py
# A superclass for Stack and Queue
# Do not modify
from abc import ABC, abstractmethod

class SequentialCollection(ABC):
    def __init__(self):
        self._data = []

    @property
    def is_empty(self):
        return len(self._data) == 0

    # add    
    @abstractmethod
    def push(self, item):
        pass

    # remove and return
    # raise IndexError if empty
    @abstractmethod
    def pop(self):
        pass

    # return without removing
    # raise IndexError if empty
    @abstractmethod
    def peek(self):
        pass

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)

