class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  #each element points to itself as a parent initially
        self.rank = [0] * n  #each elements rank is set to 0 at the start

    def find(self, x):
        if self.parent[x] != x: #if elements parent does not point to the element itself then
            self.parent[x] = self.find(self.parent[x])  #recursivly find the parent that point to itself in the set and assign it to the first element in question (path compression)
                                                        #for example if self.parent=[0,0,0,2,3] and we check find(3) then we can see that 3 points to 2 which points to 0 so we assign 0 for number 3 (add it to the set)
                                                        #outcome: self.parent=[0,0,0,0,3]
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        #check if already in the same set / nothing to union
        if x_root == y_root:
            return False

        #based on rank we assign the value with the smaller rank to the set of the value with higher tank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            #if ranks are the same x becomes a parent of y and its rank is raised by 1
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


        #return true if union successful
        return True