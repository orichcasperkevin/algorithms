from adt import Tree

tree = Tree()

for symbol in "abcdefghijklmn":
    tree.insert_node(symbol)

tree.insert_edge('a','b')
tree.insert_edge('a','c')
tree.insert_edge('a','d')

tree.insert_edge('b','e')
tree.insert_edge('b','f')

tree.insert_edge('e','k')
tree.insert_edge('e','l')

tree.insert_edge('c','g')

tree.insert_edge('d','h')
tree.insert_edge('d','i')
tree.insert_edge('d','j')

tree.insert_edge('h','m')

print(tree.pre_order_traversal(tree.root()))
