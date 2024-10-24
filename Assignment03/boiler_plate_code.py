
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

class Store:
    def __init__(self, id, left=None, right=None):
        self.id = id
        self.left = left
        self.right = right


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

# linked list 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_end(root, item):
    temp = ListNode(item)
    if root is None:
        return temp
    
    last = root
    while last.next is not None:
        last = last.next
    
    last.next = temp
    return root

def array_to_list(arr):
    root = None
    for item in arr:
        root = insert_end(root, item)
    return root

def display(root):
    while root is not None:
        print(root.val, end=" ")
        root = root.next