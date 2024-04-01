class Node:
    def __init__(self,key):
        self.leftchild=None
        self.rightchild=None
        self.data=key
def inorder(root):
    if root:
        inorder(root.leftchild)
        print(root.data, end=" ")
        inorder(root.rightchild)
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.leftchild)
        preorder(root.rightchild)
     
def postorder(root):
    if root:
        postorder(root.leftchild)
        postorder(root.rightchild)
        print(root.data,end=" ")
    

if __name__=="__main__":
    root=Node(1)
    root.leftchild=Node(2)
    root.rightchild=Node(3)
    root.leftchild.leftchild=Node(4)
    root.leftchild.rightchild=Node(5)
    root.rightchild.leftchild=Node(6)

    inorder(root)
    print(end="\n")
    preorder(root)
    print(end="\n")
    postorder(root)
