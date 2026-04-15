class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

def search(node,target):
  if node is None:
    print("Node is not found")
    return None
  
  if node.data==target:
    print(f"Node {target} Found")
    return node
  
  if target > node.data:
    return search(node.right,target)
  else: 
    return search(node.left,target)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
inOrderTraversal(root)
print()
try:
    target = int(input("Enter node to search: "))
    search(root, target)
except ValueError:
    print("Please enter a valid number.")
