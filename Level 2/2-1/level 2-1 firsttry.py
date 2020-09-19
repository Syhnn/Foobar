class Node:

  @staticmethod
  def makePerfectBinaryTree(h):
    if h == 1:
      root = Node(None)
      root.value = 1
      return root

    ch = 1            # current height
    counter = 1       # node counter
    root = Node(None) # root of the tree
    n = root          # current node

    # generate the tree
    while True:
      if n.left == None:
        if ch < h:
          n.left = Node(n)
          n = n.left
          ch = ch + 1
        else:
          n = n.parent
          ch = ch - 1
      elif n.right == None:
        if ch < h:
          n.right = Node(n)
          n = n.right
          ch = ch + 1
        else:
          n = n.parent
          ch = ch - 1
      elif n.parent == None:
        break
      else:
        n = n.parent
        ch = ch - 1

    # then add the values
    while True:
      if n.left != None and n.left.value == 0:
        n = n.left
      elif n.right != None and n.right.value == 0:
        n = n.right
      else:
        n.value = counter
        counter = counter + 1
        if (n.parent != None):
          n = n.parent
        else:
          break

    return root
  
  def __init__(self, parent):
    self.parent = parent
    self.value = 0
    self.left = None
    self.right = None
  
  ####################################################################
  # must be removed before sending since foobar doesn't accept any i/o
  def displayTree(self):
    n = self
    h = 1
    while n.left != None:
      h = h+1
      n = n.left

    for i in range (1, h+1):
      self.displayTreeRec(1, i)
      print ""

  def displayTreeRec(self, p, h):
    if self.left != None:
      self.left.displayTreeRec(p+1, h)

    if self.right != None:
      self.right.displayTreeRec(p+1, h)

    if p == h:
      print self.value,
  ####################################################################

  def getParentValueOf(self, v):
    n = self
    while True:
      if n.value == v:
        if n.parent == None:
          return -1
        else:
          return n.parent.value
      elif v <= n.left.value:
        n = n.left
      else:
        n = n.right

def solution(h, q):
  tree = Node.makePerfectBinaryTree(h)
  result = []
  for i in q:
    result.append(tree.getParentValueOf(i))
  return result


print solution(1, [1, 1, 1])
print solution(2, [1, 2, 3])
print solution(3, [1, 4, 7])
print solution(5, [19, 14, 28])