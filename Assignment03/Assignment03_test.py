import pytest 
from Assignment03_practical import *

class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def buildTree(elements):
  if len(elements) == 0:
    return None

  root_node = TreeNode(elements[0])
  nodes = [root_node]

  for i, x in enumerate(elements[1:]):
    if x is None:
      continue
    parent_node = nodes[i // 2]
    is_left = (i % 2 == 0)
    node = TreeNode(x)
    if is_left:
      parent_node.left = node
    else:
      parent_node.right = node
    nodes.append(node)

  return root_node

def buildTree_stores(elements):
  if len(elements) == 0:
    return None

  root_node = Store(elements[0])
  nodes = [root_node]

  for i, x in enumerate(elements[1:]):
    if x is None:
      continue
    parent_node = nodes[i // 2]
    is_left = (i % 2 == 0)
    node = Store(x)
    if is_left:
      parent_node.left = node
    else:
      parent_node.right = node
    nodes.append(node)

  return root_node

def test_q1():
    root = buildTree_stores([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    s1 = 5
    s2 = 1
    assert find_nearest_common_facility(root, s1, s2) == 3

    s1 = 5
    s2 = 4
    assert find_nearest_common_facility(root, s1, s2) == 5


def test_q2():
    pass

def test_q3():
    pass

def test_q4():
    pass

def test_q5():
    pass

def test_q6():
    X = 4
    k = 3

    assert satisfyingOrders(X,k) == 6

    X = 5
    k = 3

    assert satisfyingOrders(X,k) == 35

    X = 6
    k = 3

    assert satisfyingOrders(X,k) == 225

def test_q7():
    pass

def test_q8():
    pass

def test_q9():
    pass

def test_q10():
    pass

def test_q11():
    
    root = buildTree([3,9,20,None,None,15,7])
    assert puzzleOfTheTrees(root) == [[9],[3,15],[20],[7]]

    root = buildTree([1,2,3,4,5,6,7])
    assert puzzleOfTheTrees(root) == [[4],[2],[1,5,6],[3],[7]]

    root = buildTree([1,2,3,4,6,5,7])
    assert puzzleOfTheTrees(root) == [[4],[2],[1,5,6],[3],[7]]