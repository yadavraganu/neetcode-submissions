class MyHashMap:

    def __init__(self):
        self.storage = {}

    def put(self, key: int, value: int) -> None:
        self.storage[key] = value
        

    def get(self, key: int) -> int:
        return self.storage.get(key,-1)

    def remove(self, key: int) -> None:
        if key in self.storage:
            del self.storage[key]