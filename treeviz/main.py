from bst import *
btsearch = BinaryTree(input("Enter root value: "))

while True:
    command = input("Enter command (insert left(a), insert right(d), or exit(e) to stop): ")
    if command == "e":
        break
    
    node_value = input("Enter current node value: ")
    new_value = input("Enter value to insert: ")
    #treelist.append(new_value)

    # Search for the node with node_value
    # We are starting the search from Root, and this is Preorder Traversal (DFS)
    def find_node(node, value):
        if node is None:
            return None
        if node.val == value:
            return node
        left = find_node(node.left, value)
        #We keep finding left nodes till Depth
        if left:
            return left 
        else:
            find_node(node.right, value)

    current_node = find_node(btsearch.root, node_value)
    
    if current_node is None:
        print(f"Node {node_value} not found!")
        continue

    if command == "a":
        btsearch.insertleft(current_node, new_value)
    elif command == "d":
        btsearch.insertright(current_node, new_value)
    else:
        print("Invalid command")
    #print(treelist)
    btsearch.visualize()
