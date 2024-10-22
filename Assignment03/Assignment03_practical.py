from typing import List, Optional
from collections import deque

# ============ Q1 ============
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def consturct_tree(self, inorder: List[int], postorder: List[int]):
    """
    :rtype: TreeNode
    """
    # Your code goes here
    pass


# ============ Q2 ============
class Store:
    def __init__(self, id, left=None, right=None):
        self.id = id
        self.left = left
        self.right = right

def find_nearest_common_facility(root, storeId1, storeId2):
    # recurse both sides if both stores are on one side go down that side
    # find common ancestor
    
    def find_common_ancestor(root, storeId1, storeId2):
        if not root:
            return None

        # return back location of store up the recursion call
        if root.id == storeId1 or root.id == storeId2:
            return root
        
        left = find_common_ancestor(root.left, storeId1, storeId2 )
        right = find_common_ancestor(root.right ,storeId1, storeId2 )

        # assuming that each store is on opposite sides of the subtree meaning this is the closest
        if left and right:
            return root

        # move direction of where both stores are located
        return left if left else right

    return find_common_ancestor(root, storeId1, storeId2).id





# ============ Q3 ============
def beautifulNinjaFormation(n: int) -> list[int]:
    pass
    # return ans

# ============ Q4 ============
class NodeWithBuddies:
    def __init__(self, val, left=None, right=None, next=None, prev=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        self.prev = prev

def findBuddies(root: NodeWithBuddies) -> None:
    # level order traversal using BFS
    # keep track of previous nodes in level

    queue = deque([root])
    while queue:
        previous = None
        # process all nodes in a level
        for _ in range(len(queue)):
            node = queue.popleft()
            
            if previous:
                previous.next = node
                node.prev = previous
            
            previous = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# ============ Q5 ============
def endgameScores(points: list[int]) -> bool:
    pass

# ============ Q6 ============
def satisfyingOrders(X: int, k: int) -> int:
    # approach through Dynamic Programmming 
    # columns are K, unique orders
    # rows are X people in group
        # cells are unique orders 

    # initialize dp array with M+1, m+1 array including 0 indexs for both column and row 
    dp_array = [[0] * (X+1) for i in range(X+1)]

    for j in range(X):
        dp_array[j][j] = 1


    for person in range(1,X+1):
        for groups in range(1,person+1):
            # recurrance relation 
            # can add n different ways of arr[i-1, j] where the new element is not being included
            not_included = (person-1) * dp_array[person-1][groups]
        
            # can add arr[i-1, j-1] ways were new M is being included as the last happy person
            included = dp_array[person-1][groups-1]

            dp_array[person][groups] = not_included + included 

            if person == X and groups == k:
                return dp_array[person][groups] % (10**9 + 7)


    for arr in dp_array:
        print(arr)


    

# ============ Q7 ============
def batmanSignal(n):
    ans = None
    return ans 

# ============ Q8 ============
def sacred_seqeunce(keys:int, position:int) -> str:
# Write your code here
    pass

# ============ Q9 ============\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    result = None
    return result

# ============ Q10 ============
def rearrangeAllToys(toys):
    pass

# ============ Q11 ============
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def puzzleOfTheTrees(root: TreeNode) -> List[List[int]]:

    # BFS will keep track of row, adding a hyperparement to keep track of columns
    def bfs(root, col=0, row=0):

        if not root:
            return 
        
        queue = deque([(root, col, row)])

        while queue:
            node, col, row = queue.popleft()
            
            if col in levels:
                levels[col].append((row, node.val))
            else:
                levels[col] = [(row, node.val)]

            if node.left:
                queue.append((node.left, col-1, row+1))
            if node.right:
                queue.append((node.right, col+1, row+1))

    levels = {}
    bfs(root)

    # convert to list of list 
    result = []
    for col in sorted(levels.keys()):  
        column_nodes = sorted(levels[col], key=lambda x: (x[0], x[1]))
        result.append([val for row, val in column_nodes]) 
    
    return result

        



            


