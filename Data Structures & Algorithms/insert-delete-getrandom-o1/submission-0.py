class RandomizedSet:

    def __init__(self):
        self.list = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            remove_index = self.map[val]
            last_item = self.list[-1]
            self.map[last_item] = remove_index
            self.list[remove_index] = last_item
            self.list.pop(-1)
            del self.map[val] 
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()