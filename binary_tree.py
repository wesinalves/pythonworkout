class Node:
    def __init__(self, key):
        self.left = None
        self.rigth = None
        self.value = key

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.value)
        print_inorder(root.rigth)

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.rigth = Node(2)
    root.left.left = Node(3)
    root.left.rigth = Node(4)
    root.rigth.left = Node(5)
    root.rigth.rigth = Node(6)

    print("In order traversal of binary tree is:")
    print_inorder(root)