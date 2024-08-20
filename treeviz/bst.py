import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootv):
        self.root = TreeNode(rootv)
    
    def insertleft(self, current, val):
        if current.left is None:
            current.left = TreeNode(val)
        else:
            newnode = TreeNode(val)
            newnode.left = current.left
            current.left = newnode
    
    def insertright(self, current, val):
        if current.right is None:
            current.right = TreeNode(val)
        else:
            newnode = TreeNode(val)
            newnode.right = current.right
            current.right = newnode

    def visualize(self):
        def draw_tree(node, x=0, y=0, dx=1, dy=-1, layer=1):
            if node:
                #ha stands for horizontal alignment and va stands for vertical alignment
                #node.val is s which is the text to be added
                #bbox is for drawing the shape behind the text. In this case, its a circle
                plt.text(x, y, node.val, ha='center', va='center', bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='circle'))
                if node.left:
                    #dx controls the horizontal spacing between two nodes
                    #dy controls the vertical spacing between two nodes
                    plt.plot([x, x - dx], [y, y + dy], color='black')
                    draw_tree(node.left, x - dx, y + dy, dx / 2, dy, layer + 1)
                if node.right:
                    plt.plot([x, x + dx], [y, y + dy], color='black')
                    draw_tree(node.right, x + dx, y + dy, dx / 2, dy, layer + 1)
        plt.figure(figsize=(8, 6))
        draw_tree(self.root)
        plt.axis('off')
        plt.show()        
