class MyHashSet:

    def __init__(self):
        self.storage = set()
    def add(self, key: int) -> None:
        self.storage.add(key)
    def remove(self, key: int) -> None:
        if key in self.storage:
            self.storage.remove(key)
    def contains(self, key: int) -> bool:
        if key in self.storage:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)