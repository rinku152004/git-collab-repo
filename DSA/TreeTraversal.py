class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrderTraversal(node):
  if node is None:
    return
  print(node.data, end=", ")
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end=", ")


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')
nodeH = TreeNode('H')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG
nodeF.right = nodeH

# Traverse
print(root.right.right.left.data)
print(root.right.right.right.data)
print(root.data)
print("root.right.left.data:", root.right.left.data)
print("Pre-Order: ", end="")
preOrderTraversal(root)

print("\nIn-Order: ", end="")
inOrderTraversal(root)

print("\nPost-Order: ", end="")
postOrderTraversal(root)

