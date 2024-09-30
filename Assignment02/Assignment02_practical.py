from typing import List

# ============ Q1 ============
def treasure_seq(target : List, n : int) -> List:
    operations = ["Push"]

    stack = [1]
    l = 1
    for i in range(2, n+1):
        if stack == target:
            break
            
        if i == target[l]:
            stack.append(i)
            operations.append('Push')
            l += 1
        else:
            operations.append('Push')
            operations.append('Pop')

    return operations

# ============ Q2 ============

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue_LL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, val:int)->None:

        node = Node(val)
    
        if self.head:
            self.head.next = node
        else:
            self.head = node

    def dequeue(self)->int:
        if self.head:
            tmp_node = self.head.next.val
            self.head = tmp_node



    # Convert the Queue into an Array and return it
    def QueueToList(self)->list[int]:
        
        arr = []
        while self.tail:
            arr.append(self.head)
            self.head = self.head.tail





# ============ Q3 ============



# ============ Q4 ============

def largestArea(blocks: list[int]) -> int:
    l = 0
    r = len(blocks)-1
    max_vol = 0

    while l < r:

        vol = min(blocks[l] , blocks[r]) * (r-l+1)
        max_vol = max(vol, max_vol)

        if blocks[l] < blocks[r]:
            l += 1
        else:
            r -= 1


    return max_vol


# ============ Q6 ============


# ============ Q7 ============



# ============ Q8 ============



# ============ Q9 ============



# ============ Q10 ============