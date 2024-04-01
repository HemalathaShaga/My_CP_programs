class Treenode:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def level_order(root):
    if root is None:
        return
    queue=[root]
    while queue:
        current_level=[]
        level_size=len(queue)
        for _ in range(level_size):
            node=queue.pop(0)
            current_level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print(*current_level,sep=' ',end=' ')

if __name__=="__main__":
    root=Treenode(1)
    root.left=Treenode(2)
    root.right=Treenode(3)
    root.left.left=Treenode(4)
    root.left.left.right=Treenode(5)
    root.right.left=Treenode(6)
    root.right.left.left=Treenode(7)
    level_order(root)

    
    root.left=Treenode(2)
