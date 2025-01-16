#Classe per arbres

class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, i):
        return self.child[i]

    def num_children(self):
        return len(self.child)
    

#subclasse de Tree

class Pre(Tree):
    def preorder(self):
        l = [self.root()]
        for c in self.child:
            l = l + c.preorder()
        return l

#python3
#from P71608 import *