"""
Tree
"""
print(__doc__)

"""
            2
         /     \
        7       9
       / \       \
      1   6       8
         / \     / \
        5  10   3   4

"""

class Tree():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, node):

        self.left = node

    def add_right(self, node):

        self.right = node

def tree():

    two = Tree(2)
    seven = Tree(7)
    nine = Tree(9)
    two.add_left(seven)
    two.add_right(nine)

    one = Tree(1)
    six = Tree(6)
    seven.add_left(one)
    seven.add_right(six)

    five = Tree(5)
    ten = Tree(10)
    six.add_left(five)
    six.add_right(ten)

    eight = Tree(8)
    nine.add_right(eight)

    three = Tree(3)
    four = Tree(4)
    eight.add_left(three)
    eight.add_right(four)

    return two

def pre_order(node):

    print(node.data, end = " ")
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

def post_order(node):

    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node.data, end = " ")

def in_order(node):

    if node.left:
        in_order(node.left)
    print(node.data, end = " ")
    if node.right:
        in_order(node.right)

if __name__ == "__main__":

    # print(tree().data, tree().left, tree().right)

    pre_order(tree())
    print("\n")
    post_order(tree())
    print("\n")
    in_order(tree())