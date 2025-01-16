#Definició d'un iterable
class Tree:
    def __init__(self, x):
        self.rt = x 
        self.child = []

    def addChild(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ithChild(self, i):
        return self.child[i]

    def num_children(self):
        return len(self.child)
    
    def __iter__(self):
        nodes = [self]

        while(nodes):
            node = nodes.pop(0)
            yield node.root()
            for child in node.child:
                nodes.append(child)