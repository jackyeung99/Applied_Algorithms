from typing import List
from collections import deque
import random

# ============ Q1 ============
def treasure_seq(target : List, n : int) -> List:
    operations = []
    stack = []
    l = 0
    for i in range(1, n+1):
        if stack == target:
            break
            
        if i == int(target[l]):
            # append if i is in target location
            stack.append(i)
            operations.append('Push')

            # move pointer to find next target value 
            l += 1
        else:
            # simulate push and pop if not desired num 
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
            # perform operation on last two items
            # use heap for FILO
            num2 = finalAns.pop()
            num1 = finalAns.pop()

            if i == "+":
                val = num1 + num2
            elif i == "-":
                val = num1 - num2
            elif i == "*":
                val = num1 * num2
            elif i == "/":
                val = num1 / num2 

            # reappend item
            finalAns.append(int(val))

        else:
            finalAns.append(int(i))

    return finalAns.pop()



# ============ Q4 ============

def largestArea(blocks: list[int]) -> int:
    
    max_area = 0

    for i in range(len(blocks)):
        min_height = blocks[i]
    
        for j in range(i, len(blocks)):
            min_height = min(min_height, blocks[j])
            area = min_height * (j - i + 1)
            max_area = max(max_area, area)
    
    return max_area


# ============ Q5 ============
def arrangePerformers(nums):
    sorted_nums = sorted(nums)

    # flip
    flipped = sorted_nums[::-1]

    queue = deque()
    
    # repeat the line process in reverse
    for i in flipped:
        if queue:
            # bring back to front
            queue.appendleft(queue.pop())

        queue.appendleft(i)
  
            
    return list(queue) 



# ============ Q6 ============

def atom_counter(formula: str) -> str:
    stack = [{}]  
    i = 0
    n = len(formula)

    while i < n:
        print(stack)
        if formula[i] == '(':
            stack.append({})
            i += 1
        elif formula[i] == ')':
            # retrieve number after parenthesis
            i += 1
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            multiplier = int(formula[start:i] or 1)

            # multipy all elements in nested parenthesis
            top = stack.pop()
            # apply multiplier to nested and add to next outer parenthesis
            for elem, count in top.items():
                stack[-1][elem] = stack[-1].get(elem, 0) + count * multiplier
        else:
            # Read the element name
            start = i
            i += 1
            while i < n and formula[i].islower():
                i += 1
            elem = formula[start:i] 
    
            # Read the number
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            count = int(formula[start:i] or 1)
            
            # Add the count to the current level
            stack[-1][elem] = stack[-1].get(elem, 0) + count



    # handle output
    result = stack.pop()
    sorted_elements = sorted(result.items())
    output = []
    for elem, count in sorted_elements:
        output.append(elem)
        if count > 1:
            output.append(str(count))

    return ''.join(output)


# ============ Q7 ============
def checkout_counter_times(arrival, action):


    # Notes     
    # use queue 
   
    # arrival time 
        # time that each customer arrives 
        # non -decreasing order 
        # can have duplicates 

    # action 
        # 0 for pay 
        # 1 for return 

    # double queue for each action type    
    # start at first arrival time 
    # check that both items are there
    # check that both queue heads are there at the time
        # if only one process that one
        # if two are there 
            # check last item 
        # if none last_seen = None 

    # iterate time 


    n = len(arrival)
    return_stack = []
    pay_stack = []
    result = [-1] * n 
    cashier_stack = []
    last_seen = None


    # process items into seperate queues 
    for customer in range(n):
        arrival_time = arrival[customer]
        if action[customer] == 1:
            return_stack.append((customer, arrival_time))
        else: 
            pay_stack.append((customer, arrival_time))

    # print(return_stack, pay_stack)
    
    
    # queue management logic
    current_time = min(arrival)
    while len(return_stack) > 0 or len(pay_stack) > 0:

        # check both stacks have people
        if return_stack and pay_stack:

            # both people at the queues have arrived
            if return_stack[0][1] <= current_time and pay_stack[0][1] <= current_time:

                if last_seen == 1 or last_seen is None:  
                    cashier_stack.append((return_stack.pop(0)[0], current_time))
                    last_seen = 1   
                else:
                    cashier_stack.append((pay_stack.pop(0)[0], current_time))
                    last_seen = 0
                
            # only one person has arrived 
            elif return_stack[0][1] <= current_time:
                cashier_stack.append((return_stack.pop(0)[0], current_time))
                last_seen = 1
            elif pay_stack[0][1] <= current_time: 
                cashier_stack.append((pay_stack.pop(0)[0], current_time))
                last_seen = 0
            else:
                last_seen = None

        # handle one empty list 
        # handle current time such that if there is only one queue and a large gap between current time and the arrival time of next person in that queue
        elif return_stack and return_stack[0][1] <= current_time:
            cashier_stack.append((return_stack.pop(0)[0], current_time))
        elif pay_stack and pay_stack[0][1] <= current_time:
            cashier_stack.append((pay_stack.pop(0)[0], current_time))


        current_time += 1

    # proccess end results 
    for customer, processed_time in cashier_stack: 
        result[customer] =  processed_time

    return result

    

# ============ Q8 ============
class quarryPieLine:
    def __init__(self):
        self.counter = 1
        self.stack1= []
        self.stack2 = []

        self.result = []

    def print_list(self):
        return self.result

    def joinInFront(self):
        
        self.stack1.append(self.counter)
        while self.result:
            self.stack1.append(self.result.pop(0)) 

        self.result = self.stack1.copy()
        self.stack1.clear()
        self.counter += 1 

    def joinInMiddle(self):
        if len(self.result) < 1:
            self.result.append(self.counter)
        else:
            halve = len(self.result) // 2 

            for i in range(len(self.result)): 
                if i == halve:
                    self.stack1.append(self.counter)
                    
                self.stack1.append(self.result[i])

            self.result = self.stack1.copy()
            self.stack1.clear()

        self.counter +=1

    def joinInBack(self):
        self.result.append(self.counter)
        self.counter += 1

    def removeFromFront(self):
        if len(self.result) > 0:
            self.result.pop(0)
        

    def removeFromMiddle(self):
        if len(self.result)> 0:
                
            if len(self.result) % 2 == 0:
                halve = len(self.result) // 2 - 1
            else:
                halve = len(self.result) // 2
            
            for i in range(len(self.result)): 
                if i == halve:
                    self.result.pop(i)
        

    def removeFromBack(self):
        if len(self.result) > 0:
            self.result.pop(-1)

    def whoIsFront(self) -> int:
        if len(self.result) > 0:
            return self.result[0] 
        return -1

    def whoIsMiddle(self) -> int:
        if len(self.result) > 0:
            if len(self.result) % 2 == 0:
                halve = len(self.result) // 2 - 1
            else:
                halve = len(self.result) // 2

            return self.result[halve]
        else:
            return -1
        
    
    def whoIsBack(self) -> int:
        if len(self.result) > 0: 
            return self.result[-1]
        return -1

# ============ Q9 ============

class amor_dict():
    def __init__(self, num_list = []):
        self.amor_dict = {}
        for i in num_list:
            self.insert(i)

    # merge approach as listted on slides 
    def merge_sorted_arr(self, arr1, arr2):
        merged_array = []
        i, j = 0, 0  
        while i < len(arr1) or j < len(arr2):
            if i < len(arr1) and (j >= len(arr2) or arr1[i] <= arr2[j]):
                merged_array.append(arr1[i])
                i += 1
            else:
                merged_array.append(arr2[j])
                j += 1

        return merged_array
    

    def insert(self, num):
        # loop through levels 
        # check if level is full 
            # if full combine list into temp 
            # else add temp to array 

        tmp = [num]
        level = 0
        while level in self.amor_dict:
            arr = self.amor_dict[level]
            # check if level is full
            if len(arr) == 2 ** level:
                tmp = self.merge_sorted_arr(arr, tmp)
                self.amor_dict[level] = []
            else:
                self.amor_dict[level] = self.merge_sorted_arr(arr, tmp)
                break 

            level += 1

        if level not in self.amor_dict:
            self.amor_dict[level] = tmp 


    def search(self, num):
        # your code here
        for level in range(len(self.amor_dict)):
            if num in self.amor_dict[level]:
                return level
        return -1
    
    # Returns a list of all levels under a list
    # ex [[x],[t,y]...]
    def print(self):
        combined = []
        for _, arr in self.amor_dict.items():
            combined.append(arr)

        return combined


# ============ Q10 ============


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

class SkipList:
    # Any variables for intialization
    def __init__(self):
        self.head = None
        self.max_level = 16

    # Returns True if the element is present in skip list else False
    def search(self, target: int) -> bool:
        p = self.head 
        while p:            
            # Move right as far as possible on the current level
            while p.next and p.next.val < target:
                p = p.next
     
            if p.next and p.next.val == target:
                return True

            # drop down 
            p = p.down

        return False

    # create default traversal column for all levels 
    def create_sentinals(self, head_val):
        self.head = Node(head_val)
        current = self.head
    
        for i in range(self.max_level - 1):
            node = Node(head_val) 
            current.down = node  
            current = node

    # simulate the coin flip repeated 
    def generate_random_height(self):
        count = 1
        while random.random() < 0.5 and count < self.max_level:
            count += 1

        return count


    # Inserts the element into the skip list
    def insert(self, num: int) -> None:
        
        if not self.head:
            self.create_sentinals(-1)


        update = []  
        p = self.head

        # start at bottom 
        while p:         
            while p.next and p.next.val < num:
                p = p.next
            
            update.append(p)
            if p.down is not None:
                p = p.down  
            else:
                break            

        # assuming were at lowest level add node  and traverse right
        node = Node(num)
        p.next = node
        p = node

        # generate random height
        column_height = self.generate_random_height()        
        
        # Build upward from the new node that was added to the right 
        # connecting each layer/ last node to right
        for i in range(column_height):
            if i < len(update):
                # one up from the bottom 
                prev_node = update.pop()

                node = Node(num) 
                node.next = prev_node.next 
                prev_node.next = node  
                node.down = p  
                # move up column 
                p = node  