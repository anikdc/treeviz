import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define the TreeNode and BinaryTree classes as before
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val):
        self.root = TreeNode(root_val)

    def insertleft(self, current, val):
        if current.left is None:
            current.left = TreeNode(val)
        else:
            new_node = TreeNode(val)
            new_node.left = current.left
            current.left = new_node

    def insertright(self, current, val):
        if current.right is None:
            current.right = TreeNode(val)
        else:
            new_node = TreeNode(val)
            new_node.right = current.right
            current.right = new_node

    def visualize(self, canvas, fig):
        def draw_tree(node, x=0, y=0, dx=1, dy=-1, layer=1):
            if node:
                plt.text(x, y, node.val, ha='center', va='center', bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='circle'))
                if node.left:
                    plt.plot([x, x - dx], [y, y + dy], color='black')
                    draw_tree(node.left, x - dx, y + dy, dx / 2, dy, layer + 1)
                if node.right:
                    plt.plot([x, x + dx], [y, y + dy], color='black')
                    draw_tree(node.right, x + dx, y + dy, dx / 2, dy, layer + 1)
        
        fig.clear() 
        draw_tree(self.root)
        plt.axis('off')
        canvas.draw()

def find_node(node, value):
    if node is None:
        return None
    if node.val == value:
        return node
    left = find_node(node.left, value)
    if left:
        return left
    return find_node(node.right, value)

# Function to update the tree and redraw the visualization
def update_tree():
    node_value = current_node_entry.get()
    new_value = new_node_entry.get()
    
    if not tree.root:
        tree.root = TreeNode(node_value)
        result_label.config(text=f"Root set to {node_value}")
    else:
        current_node = find_node(tree.root, node_value)
        if current_node is None:
            result_label.config(text=f"Node {node_value} not found!")
        else:
            if insert_side.get() == 'left':
                tree.insertleft(current_node, new_value)
                result_label.config(text=f"Inserted {new_value} to the left of {node_value}")
            else:
                tree.insertright(current_node, new_value)
                result_label.config(text=f"Inserted {new_value} to the right of {node_value}")

    tree.visualize(canvas, fig)

# Initialize the Tkinter window
rtk = tk.Tk()
rtk.title("Binary Tree Visualization")

# Create and place GUI elements
tk.Label(rtk, text="Root Value:").grid(row=0, column=0, padx=10, pady=10)
root_entry = tk.Entry(rtk)
root_entry.grid(row=0, column=1, padx=10, pady=10)

def set_root():
    global tree
    root_value = root_entry.get()
    tree = BinaryTree(root_value)
    update_tree()

tk.Button(rtk, text="Set Root", command=set_root).grid(row=0, column=2, padx=10, pady=10)

tk.Label(rtk, text="Current Node Value:").grid(row=1, column=0, padx=10, pady=10)
current_node_entry = tk.Entry(rtk)
current_node_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(rtk, text="New Node Value:").grid(row=2, column=0, padx=10, pady=10)
new_node_entry = tk.Entry(rtk)
new_node_entry.grid(row=2, column=1, padx=10, pady=10)

insert_side = tk.StringVar(value='left')
tk.Radiobutton(rtk, text="Insert Left", variable=insert_side, value='left').grid(row=3, column=0, padx=10, pady=10)
tk.Radiobutton(rtk, text="Insert Right", variable=insert_side, value='right').grid(row=3, column=1, padx=10, pady=10)

tk.Button(rtk, text="Insert Node", command=update_tree).grid(row=4, column=0, columnspan=2, pady=20)

result_label = tk.Label(rtk, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Create the Matplotlib figure and canvas
fig = plt.figure(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=rtk)
canvas.get_tk_widget().grid(row=6, column=0, columnspan=3)

# Start the Tkinter event loop
rtk.mainloop()
