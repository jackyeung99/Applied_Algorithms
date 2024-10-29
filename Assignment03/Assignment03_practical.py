from typing import List, Optional
from collections import deque
from math import factorial

# ============ Q1 ============
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(inorder: List[int], postorder: List[int]):
    """
    :rtype: TreeNode
    """
    # Your code goes here

    if not inorder:
        return None

    root = TreeNode(postorder.pop())
    root_id = inorder.index(root.val)

    left_subtree = inorder[:root_id]
    right_subtree = inorder[root_id+1:]
    
    root.right = construct_tree(right_subtree, postorder)
    root.left = construct_tree(left_subtree,postorder)

    return root




# ============ Q2 ============
class Store:
    def __init__(self, id, left=None, right=None):
        self.id = id
        self.left = left
        self.right = right

def find_nearest_common_facility(root, storeId1, storeId2):
    # recurse both sides if both stores are on one side go down that side
    # find common ancestor
    
    def find_path(root, store):
        if not root:
            return None

        # return back location of store up the recursion call
        if root.id == store:
            return [root.id]
        
        # recursively search both sides of the call
        left_sub = find_path(root.left, store)
        right_sub = find_path(root.right ,store)

        # return node path up the recursive call
        if left_sub: 
            return [root.id] + left_sub
        if right_sub:
            return [root.id] + right_sub

        return None
    
    path1 = find_path(root, storeId1)
    path2 = find_path(root, storeId2)
 
    common_ancestor = None
    for i in range(min(len(path1), len(path2))):
        if path1[i] == path2[i]:
            common_ancestor = path1[i]
        else:
            break  

    return common_ancestor




# ============ Q3 ============

def beautifulNinjaFormation(n):

    def find_ninjas(n):
        if n == 1:
            return [1]
        elif n == 2:
            return [1,2]
    
        return [2 * x -1  for x in find_ninjas((n+1)//2)] + [2 * x  for x in find_ninjas(n//2)]

    return find_ninjas(n)


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
    # two pointer 
    # calculate all recursive variations
    # see if highest score differential is greater than 0 

    def recurse_scores(points, l, r, ronaldo_turn):
        # Base case: If there is only one game left
        if l == r:
            if ronaldo_turn:
                return points[l]
            else:
                return -points[l]


        # calculate the highest score differntial for every score permutation

        # Ronaldo's turn
        if ronaldo_turn:
            return max(
                points[l] + recurse_scores(points, l + 1, r, False),
                points[r] + recurse_scores(points, l, r - 1, False)
            )
        # Messi's turn
        else:
            return min(
                -points[l] + recurse_scores(points, l + 1, r, True),
                -points[r] + recurse_scores(points, l, r - 1, True)
            )


    return recurse_scores(points, 0, len(points) - 1, True) >= 0
 

    
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
    ans = []

    def find_all_comb(str=''):

        if len(str) == n:
            ans.append(str)
            return

        # add x and y if previous was x 
        if len(str) == 0 or  str[-1] == 'x':
            find_all_comb(str + 'x')
            find_all_comb(str + 'y')
        
        # only add x if y was previous
        elif str[-1] == 'y':
            find_all_comb(str + 'x')
        
    find_all_comb()
    return sorted(ans, reverse=True) 

# ============ Q8 ============
def sacred_sequence(keys:int, position:int) -> str:
# Write your code here

    def find_digit(digits, k): 

        if len(digits) == 1:
            output_str.append(str(digits[0]))
            return 
        
        
        size = len(digits)
        # same as n! / n
        block = factorial(size-1)
        # find what the first digit is 
        location =  k // block
               
        output_str.append(str(digits.pop(location)))

        # update k for recursion into next digit permutaitons
        k %= block

        find_digit(digits, k)

        
    output_str = []
    # zero index and input list of integers to n 
    find_digit([x for x in range(1,keys+1)], position-1)
    return ''.join(output_str)


# ============ Q9 ============\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    
    def recurse_ll(head, val):

        if not head:
            return None
        
        head.next = recurse_ll(head.next, val)
            
        if head.val == val:
            return head.next
        else:
            return head


    result = recurse_ll(head, val)
    return result if result else None

# ============ Q10 ============
def rearrangeAllToys(toys):
    results = []
    toys.sort()
        
    if len(toys) % 2 == 0:
        halve = len(toys) // 2
        left = toys[:halve]
        right = toys[halve:]
    else:
        halve = (len(toys) // 2) + 1
        left = toys[:halve]
        right = toys[halve:]

    while left and right: 
        results.append(left.pop())   
        results.append(right.pop())

    while left:
        results.append(left.pop())
    
    while right:
        results.append(right.pop())

    return results





# ============ Q11 ============
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def puzzleOfTheTrees(root: TreeNode) -> List[List[int]]:

    # use a BFS to keep track of rows and column of node
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

        



            


