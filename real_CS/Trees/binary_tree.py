
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    def __str__(self):
        return f"{self.val}={self.right}-{self.left}"


tree = [
    TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7))),
]

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        path.append(root.val)
        in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        path.append(root.val)

path = []
in_order_traversal(tree[0])
print(path)

path = []
post_order_traversal(tree[0])
print(path)
