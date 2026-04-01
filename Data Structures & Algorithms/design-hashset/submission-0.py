class MyHashSet:

    def __init__(self):
        self.hs = []

    def add(self, key: int) -> None:
        
        if not self.contains(key):
            self.hs.append(key)
            self.hs.sort()
        return
        
    def remove(self, key: int) -> None:
        if self.contains(key):
            l, r= 0, len(self.hs) - 1 

            while l <= r:
                k = (l+r)//2

                if key == self.hs[k]:
                    self.hs.pop(k)
                    return
                elif key < self.hs[k]:
                    r = k - 1
                else:
                    l = k + 1
        return
        

    def contains(self, key: int) -> bool:
        l, r= 0, len(self.hs) - 1 

        while l <= r:
            k = (l+r)//2

            if key == self.hs[k]:
                return True
            elif key < self.hs[k]:
                r = k - 1
            else:
                l = k + 1
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)