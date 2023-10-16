class ListNode():
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.next,self.prev=None,None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.left,self.right=ListNode(0,0),ListNode(0,0)
        self.left.next,self.right.prev=self.right,self.left

    def remove(self,node): # from linked list 
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p
        
    def insert(self,node):
        p=self.right.prev
        n=self.right
        p.next=n.prev=node
        node.next,node.prev=n,p
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key]=ListNode(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[key] # deleting key from hashmap

obj = LRUCache(2)
print(obj.get(2))
obj.put(2,4)
print(obj.get(1))
obj.put(1,5)
obj.put(1,2)
print(obj.get(1))
print(obj.get(2))


