from node import Node

node_2 = Node(3)
node_1 = Node(5, node_2)

print(node_1.next is node_2) # True
print(node_1.value) # 5
print(node_1.next.value) # 3
print(node_2.value) # 3