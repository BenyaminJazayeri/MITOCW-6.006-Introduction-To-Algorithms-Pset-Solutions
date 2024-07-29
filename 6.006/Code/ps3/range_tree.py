import avl

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

def size(node):
    if node is None:
        return 0
    else:
        return node.size

def update_size(node):
    node.size = size(node.left) + size(node.right) + 1

class RangeTree(avl.AVL):
    
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_size(x)
        update_height(y)
        update_size(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_size(x)
        update_height(y)
        update_size(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            update_size(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def rank(self, k):
        node = self.root
        r = 0
        while node!=None:
            if k<node.key:
                node = node.left
            elif node.key<k:
                r+=size(node.left)+1
                node = node.right
        return r

    def count(self,l,h):
        return self.rank(h) - self.rank(l)

    def lca(self,l,h):
        node = self.root
        while not(node==None or (l<=node.key<=h)):
            if l<node.key:
                node = node.left
            else:
                node = node.right
        return node

    def node_list(self,node,l,h,result):
        if node == None:
            return
        if l<=node.key<=h:
            result.append(node.key)
        if l<=node.key:
            self.node_list(node.left,l,h,result)
        if node.key<=h:
            self.node_list(node.right,l,h,result)

    def list(self,l,h):
        lca = self.lca(l,h)
        result = []
        self.node_list(lca,l,h,result)
        return result

## insert(k), delete(k), find(k), find_min(), and next_larger(k) inherited from bst.BST


def test(args=None, BSTtype=RangeTree):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print 'usage: %s <number-of-random-items | item item item ...>' % \
              sys.argv[0]
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in xrange(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print tree
    for item in items:
        tree.insert(item)
        print
        print tree
    for i in range(16):
        print tree.rank(i+.5)

if __name__ == '__main__': test()


    
