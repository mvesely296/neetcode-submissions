from dataclasses import dataclass


@dataclass
class LRUNode:
    key: int = -1
    val: int = -1
    left: "LRUNode | None" = None
    right: "LRUNode | None" = None


class LRUCache:
    capacity: int
    lru: LRUNode
    mru: LRUNode
    key_map: dict[int, LRUNode]

    def __init__(self, capacity: int):
        self.lru = LRUNode()
        self.mru = LRUNode()
        self.lru.right = self.mru
        self.mru.left = self.lru
        self.key_map = {}
        self.capacity = capacity

    def pop_node(self) -> int:
        key = self.lru.right.key
        self.lru.right = self.lru.right.right
        self.lru.right.left = self.lru

        return key

    def insert_node(self, key: int, value: int):
        new_node = LRUNode(key=key, val=value, left=self.mru.left, right=self.mru)
        self.mru.left.right = new_node
        self.mru.left = new_node
        self.key_map[key] = new_node

    def update_node(self, key: int):
        if key not in self.key_map:
            raise KeyError(f"Trying to update key {key} but not found in map")

        node = self.key_map[key]

        # remap the nodes around our node
        node.left.right = node.right
        node.right.left = node.left

        # append the node to the end
        node.left = self.mru.left
        node.right = self.mru
        self.mru.left.right = node
        self.mru.left = node

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        self.update_node(key)
        return self.key_map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            self.key_map[key].val = value
            self.update_node(key)
            return

        if len(self.key_map) >= self.capacity:
            del self.key_map[self.pop_node()]

        self.insert_node(key, value)
