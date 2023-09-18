from bst import Tree
tree = Tree()
tree.insert_from_list([50,30,20,40,70,60,80])
#tree.in_order_traversal(tree.root)
#tree.pre_order_traversal(tree.root)
#tree.post_order_traversal(tree.root)
print(tree.height(tree.root))
