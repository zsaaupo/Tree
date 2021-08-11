"""
Tree 2
"""
print(__doc__)

class Node():

    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, node):

        self.left = node

    def add_right(self, node):

        self.right = node

def my_tree():

    one = Node(1) # root node
    
    # childe of root node
    two = Node(2)
    three = Node(3)
    one.add_left(two)
    one.add_right(three)

    # left side of root node
    
    # child of 2
    four = Node(4)
    five = Node(5)
    two.add_left(four)
    two.add_right(five)

    # child of 4
    eight = Node(8)
    nine = Node(9)
    four.add_left(eight)
    four.add_right(nine)

    # right side of root node

    # child of 3
    six = Node(6)
    seven = Node(7)
    three.add_left(six)
    three.add_right(seven)

    # child of 6 
    ten = Node(10)
    six.add_right(ten)

    # child of 7
    eleven = Node(11)
    twelve = Node(12)
    seven.add_left(eleven)
    seven.add_right(twelve)

    return one

class Travarse():

    def in_order(self, node):

        if node.left:
            self.in_order(node.left)
        print(node.data, end=" ")
        if node.right:
            self.in_order(node.right)

    def post_order(self, node):

        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)
        print(node.data, end=" ")

    def pre_order(self, node):

        print(node.data, end=" ")
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)

    

if __name__ == "__main__":

    print(my_tree().data)

    obj_t = Travarse()

    obj_t.in_order(my_tree())
    print("\n")
    obj_t.post_order(my_tree())
    print("\n")
    obj_t.pre_order(my_tree())