class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def is_full(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_full(root.left) and is_full(root.right)
    return False
def is_complete(root):
    if root is None:
        return True
    queue=[root]
    flag=True
    while queue:
        current=queue.pop(0)
        if current:
            if flag:
                return False
            queue.append(current.left)
            queue.append(current.right)
        else:
            flag=True
    return True
def is_perfect(root,depth=0,level=0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return depth==level+1
    if root.left is None or root.right is None:
        return False
    return is_perfect(root.left,depth,level+1)<=is_perfect(root.right,depth,level+1)
def is_balanced(root):
    if root is None:
        return True
    left_height=height(root.left)
    right_height=height(root.right)
    return abs(left_height-right_height)<=1 and is_balanced(root.left)and is_balanced(root.right)
def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))

if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.right=Node(4)
    root.right.left=Node(5)
    root.right.right=Node(6)
    print(is_full(root))
    print(is_balanced(root))
    print(is_complete(root))
    print(is_perfect(root))
    
    

            
