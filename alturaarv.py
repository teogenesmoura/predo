#receber um no raiz
#adicionar cada filho a uma pilha de filhos nao percorridos
#vai retirar um filho e armazenar sua altura num mapa
#vai percorrer todos os filhos ate esgotar

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

def print_tree(Node):
    nodes = [] # [Node, Node, Node] -> [(Node, height), (Node, height)] ...
    height = 0
    if not nodes:
        curr = nodes.append((Node, height))
    while nodes: # []
        current_tuple = nodes.pop(0) #[(a3,1)] #nodes = [(a2,1)]
        node = current_tuple[0] #a3 == Node(3)
        value = node.value # a3.value == Node(3).value = 3
        current_height = current_tuple[1] #1
        print("Node " + str(value) + " is at height " + str(current_height) + " \n")
        if node.left:
            nodes.append((node.left, current_height + 1))
        if node.right:
            nodes.append((node.right, current_height + 1))


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a1.left = a2
a1.right = a3
a2.left = a4
a3.right = a5
a5.right = Node(6)

# a1 = Node(1)
# a2 = Node(2)
# a3 = Node(3)
# a1.left = a2
# a1.right = a3

print_tree(a1)
