from DataTypes.adt import Tree

tree = Tree()

print(tree)
tree.insert_root("root")
print(tree.nodes)
tree.insert_root("root1")
print(tree.nodes)
