class LRUCache:

    def __init__(self, capacity: int):
        self._dic = dict()
        self._que = []
        self._cap = capacity

    def get(self, key: int) -> int:
        if key in self._dic:
            self._que.pop(self._que.index(key))
            self._que.insert(0,key)
            return self._dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._dic:
            self._que.pop(self._que.index(key))
        elif len(self._que) == self._cap:
            popped = self._que.pop()
            del self._dic[popped]
        self._que.insert(0, key)
        self._dic[key] = value
        
## using orderedDict
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.cap:
            self.popitem(last = False)  # FIFO if last = False. LIFO if last = True