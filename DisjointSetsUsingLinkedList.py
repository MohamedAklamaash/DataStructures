class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DisjointSet:
    def __init__(self):
        self.sets = {}

    def makeSet(self, value):
        new_node = Node(value)
        self.sets[value] = new_node

    def union(self, value1, value2):
        set1 = self.findSet(value1)
        set2 = self.findSet(value2)

        if set1 == set2:
            return

        set1_head = set1
        set2_head = set2

        while set1_head.next is not None:
            set1_head = set1_head.next

        set1_head.next = set2_head

        del self.sets[value2]

    def findSet(self, value):
        set = self.sets[value]

        while set.next is not None:
            set = set.next

        return set.value
    
    def printSet(self):
        for key,value in enumerate(self.sets):
            print(value , end=" ")

if __name__ == "__main__":
    set1 = DisjointSet()
    set1.makeSet(2)
    set1.makeSet(10)
    set1.makeSet(20)
    set1.makeSet(30)
    set1.printSet()
