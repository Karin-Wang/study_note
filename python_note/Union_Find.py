class QuickFind:
    def __init__(self):
        self.id = {}
            
    def connected(self,p,q):
        return self.find(p) == self.find(q)
    
    def find(self,p):  
        if p not in self.id:
            self.id[p] = p
        while p in self.id and self.id[p] != p:
            p = self.id[p]
        return self.id[p]
    
    def union(self,p,q):
        p = self.find(p)
        q = self.find(q)
        self.id[p] = q
