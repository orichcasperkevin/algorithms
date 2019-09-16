class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def reverse(self):
        return [ self.items[(len(self.items)-1) - i] for i in range(len(self.items)) ]

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class HashTable:
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and \
            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def put(self, key, data):
        hash_value = self.hash_function(key,len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data #replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and \
                    self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data #replace

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

class Tree:
    def __init__(self):
        self.height = 0
        self.d_ary = 2
        self.nodes = []
        self.edges = []
        self.path = []

    def nodes(self):
        return self.nodes

    def edges(self):
        return self.edges

    def root(self):
        return self.nodes[0]

    def size(self):
        return len(self.nodes)

    def children_count(self,node):
        count = 0
        for edge in self.edges:
            if edge[0] == node:
                count += 1
        return count

    def has_children(self,node):
        for edge in self.edges:
            if edge[0] == node:
                return True
        return False

    def insert_root(self,label):
        self.nodes.insert(0,label)

    def insert_node(self,label):
        self.nodes.append(label)

    def insert_edge(self,from_node,to_node):
        self.edges.append([from_node,to_node])

    def pre_order_traversal(self,node):
        if node == self.root():
            self.path.append(node)
        for edge in self.edges:
            if edge[0] == node:
                self.path.append(edge[1])
                self.pre_order_traversal(edge[1])
        return self.path
