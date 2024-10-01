from typing import List
from collections import deque


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
        if self.tail:  
            self.tail.next = node
        self.tail = node  
        if not self.head: 
            self.head = node


    def dequeue(self)->int:
        if self.head:  
            dequeued_value = self.head.val
            self.head = self.head.next 
            if not self.head: 
                self.tail = None

            return dequeued_value
    
        return None 


    # Convert the Queue into an Array and return it
    def QueueToList(self) -> list[int]:
        arr = []
        current = self.head
        while current:
            arr.append(current.val)
            current = current.next
        return arr





# ============ Q3 ============
def spiritualArithmetic(incantation: list[str]) -> int:

    finalAns = []
    operations = ["+", "-", "*", "/" ]

    for i in incantation:

        if i in operations:
            num2 = finalAns.pop()
            num1 = finalAns.pop()

            if i == "+":
                val = num1 + num2
            elif i == "-":
                val = num1 - num2
            elif i == "*":
                val = num1 * num2
            elif i == "/":
                val = num1 // num2 

            finalAns.append(val)

        else:
            finalAns.append(int(i))

    return finalAns.pop()



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


# ============ Q5 ============
def arrangePerformers(nums):
    sorted_nums = sorted(nums)
    halve = len(sorted_nums) // 2

    res = [sorted_nums.pop(0)]
    for i in range(halve):
        res.append(sorted_nums[halve+i])
        res.append(sorted_nums[i])

    
    return res



# ============ Q6 ============


# ============ Q7 ============



# ============ Q8 ============



# ============ Q9 ============



# ============ Q10 ============