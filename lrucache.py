class Node(object):
    def __init__(self,k,x):
        self.key = k
        self.val = x
        self.prev = None
        self.next = None
class DoubleLinkedList(object):
    def __init__(self):
        self.tail = None
        self.head = None
    def isEmpty(self):
        return (self.tail is not None)
    def removeLast(self):
        self.remove(self.tail)
    def remove(self,node):
        if self.head == self.tail:
            self.head,self.tail = None,None
            return
        if node == self.head:
            node.next.prev = None
            self.head = node.next
            return
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.prev.next=node.next
        node.next.prev=node.prev
        node.prev = None
        node.next = None
    def addFirst(self,node):
        if not self.head:
            self.head=self.tail = node
            node.prev =node.next = None
            return
        node.next=self.head
        self.head.prev = node
        self.head = node
        node.prev = None    
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.list = DoubleLinkedList()
    # @return an integer
    def get(self, key):
        if key in self.cache and self.cache[key]:
            self.list.remove(self.cache[key])
            self.list.addFirst(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.list.remove(self.cache[key])
            self.list.addFirst(self.cache[key])
            self.cache[key].val = value
        else:
            node = Node(key,value)
            self.cache[key] = node
            self.list.addFirst(node)
            self.size = self.size+1
            if self.size>self.capacity:
                self.size=self.size-1
                del self.cache[self.list.tail.key]
                self.list.removeLast()

lru = LRUCache(3)
lru.set(1,'hello')
lru.set(2,'world')
print lru.get(1)
lru.set(3,'huang')
print lru.get(3)
lru.set(3,'wei')
print lru.get(3)
lru.set(4,'huang')
print lru.get(3)
print lru.get(4)
print lru.get(1)
print lru.get(2)