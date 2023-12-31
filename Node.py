class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
          total+=1
          cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self,index):
        if index>=self.length():
            print ("Error, index out of range")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur.node.next
            if cur_idx==index:return cur_node.data
            cur_idx==1

    def erase(self,index):
        if index == self.len():
            print("Error, erase")
            return
        cur_idx=0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return
            cur_idx+=1



my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(23)
my_list.append(3)
my_list.append(4)

my_list.display()




# class Node:

#   def __init__(self, value):
#     self.value = value
#     self.right = None
#     self.left = None

#   def __repr__(self):
#     return f'<Node: {self.value}>'

# node = Node('Monday')


# node2 = Node('Tuesday')

# node.right = node2


# node3 = Node('Wednesday')

# node2.right = node3

# print(node, node.right.right)

# node4 = Node('Friday')

# node3.right = node4