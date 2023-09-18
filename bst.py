# Python program to insert a node
# in a BST

# Given Node
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

class Tree:
    # Function to insert a new node with
    # given key in BST
    def insert(self,node, key):
    	# If the tree is empty, return a new node
    	if node is None:
    		return Node(key)

    	# Otherwise, recur down the tree
    	if key < node.key:
    		node.left = self.insert(node.left, key)
    	elif key > node.key:
    		node.right = self.insert(node.right, key)

    	# Return the node pointer
    	return node

    def insert_from_list(self,list):
        root = None
        for i,item in enumerate(list):
            if i == 0:
                root = self.insert(None,item)
                self.root = root
            self.insert(root,item)

    # Function to do inorder traversal of BST
    def in_order_traversal(self,root):
    	if root is not None:
    		self.in_order_traversal(root.left)
    		print(root.key, end=" ")
    		self.in_order_traversal(root.right)

    def pre_order_traversal(self,root):
        if root is not None:
            print(root.key, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self,root):
        if root is not None:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.key, end=" ")


    def height(self,root):
        # Check if the binary tree is empty
        if root is None:
            # If TRUE return 0
            return 0
        # Recursively call height of each node
        leftAns = self.height(root.left)
        rightAns = self.height(root.right)

        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1
