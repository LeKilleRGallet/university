import random

class Array:
    def __init__(self, capacity, fill_value=None):
        self._items = list()
        for i in range(capacity):
            self.items.append(fill_value)
            
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __str__(self):
        return str(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, value, index):
        self._items[index] = value
        
    def __random__(self):
        for i in range(self.__len__()):
            self._items[i] = random.randint(0, 100)
            
    def __clear__(self):
        for i in range(self.__len__()):
            self._items[i] = None
        