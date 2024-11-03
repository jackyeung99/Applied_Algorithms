from typing import List, Tuple
from collections import deque

import heapq

# ============ Q1 ============
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Wavelet_Tree:
    def __init__(self, A:list[int]=[]):
        pass

    def get_wavelet_level_order(self):
        # Return level order traversal of the tree.
        pass

    def rank(self, character, position):
        # Return the rank of the given character in the given position range.
        pass



# ============ Q2 ============
def palin_break(s: str):
  
    def is_palindrome(s):
        return s == s[::-1]

    # Recursive backtracking function with memoization
    def recursive_back_track(s, start=0, path=[]):

        if start == len(s):
            results.append(path[:])  
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)  
                recursive_back_track(s, end, path) 
                path.pop() 

    results = []
    recursive_back_track(s)
    return results
 



# ============ Q3 ============
def heavenGates(scroll1, scroll2, scroll3):
    # step 1 check if the digits are the same length and containt the same counts

    # recursive solution 
    # def find_all_splits(i1, i2):
            



    ans = []
    return ans

# ============ Q4 ============

def magical_recipe(T: int, cases: list[str]) -> list[int]:
    # Implement the logic here to return the result for each test case
    
    def count_permutations(string):
        i=0
        transformations = 1
        while i < len(string)-1:
            if i < len(string) - 2 and (string[i:i+2] == "ab" or string[i:i+2] == "ba"):
                transformations  *= 2 

                            
            i += 1

        return transformations


    result = []

    for i in range(T):
        string = cases[i]
        result.append(count_permutations(string) % 998244353)

    # print(result)
    return result

# ============ Q5 ============

def lelouch_task_schedule(tasks: list[str], n: int) -> int:

    # keep track of frequencies  
    task_counts = {}
    for item in tasks:
        if item in task_counts:
            task_counts[item] += 1
        else: 
            task_counts[item] = 1

    
    # construct max-heap 
    heap = []
    for node, freq in task_counts.items():
        heapq.heappush(heap, (-freq, node))

    
    # CPU cycling
    timer = 0
    cooldown = deque()
    while heap or cooldown:
        timer += 1
        
        if heap:
            # pop the most frequently used item first
            freq, task = heapq.heappop(heap)
            freq = -freq

            # add recently processed to a cooldown queue 
            if freq > 1:
                cooldown.append((freq-1, task, timer + n))
             
        # if cooldown for last timer is expired re add to heap 
        if cooldown and cooldown[0][2] == timer:
            freq, task, _ = cooldown.popleft()
            heapq.heappush(heap, (-freq, task))
            
        

    return timer


# ============ Q6 ============
def rajsTradingShowdown(orders: List[List[int]]) -> int:
    # Your Code Here...
    

    buy_heap = []
    sell_heap = []

    for price, quantity, type in orders:

        # process buy order 
        if type == 0:
            while quantity > 0 and sell_heap and sell_heap[0][0] <= price:
         
                sell_price, sell_quantity = heapq.heappop(sell_heap) 
                
                if sell_quantity > quantity:
                    heapq.heappush(sell_heap, (sell_price, sell_quantity - quantity))
                    quantity = 0
                else:
                    quantity -= sell_quantity
               
            
            if quantity > 0:
                # max heap for buyers
                heapq.heappush(buy_heap, (-price, quantity))


        # sell order 
        else:
            while quantity > 0 and buy_heap and -buy_heap[0][0] >= price:
                buy_price, buy_quantity = heapq.heappop(buy_heap)
                if buy_quantity > quantity:
                    heapq.heappush(buy_heap, (buy_price, buy_quantity - quantity))
                    quantity = 0
                else:
                    quantity -= buy_quantity
            
            if quantity > 0:
                # min heap for sellers
                heapq.heappush(sell_heap, (price, quantity))

    print(buy_heap)
    print(sell_heap)
    total_orders = sum([x for _, x  in buy_heap]) + sum([x for _, x  in sell_heap]) 
    print(total_orders)
    return total_orders % (10**9 + 7)





# ============ Q7 ============

def collect_items(matrix: list[list[int]]) -> int: 

    # precompute largest item
    max_item = max([max([col for col in row]) for row in matrix])
    row_size = len(matrix)
    col_size = len(matrix[0])


    # Find shortest distance from each node to the other
    def bfs(start, target):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(start[0], start[1], 0)]) 
        visited = [[False] * col_size for _ in range(row_size)]
        visited[start[0]][start[1]] = True

        while queue:
            x, y, distance = queue.popleft()

            # Check if we have reached the target item
            if matrix[x][y] == target and (x, y) != start:
                return distance, (x, y)

            # Explore neighbors in all 4 directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                # Check if the new position is within bounds and not an obstacle
                if 0 <= new_x < row_size and 0 <= new_y < col_size and not visited[new_x][new_y] and matrix[new_x][new_y] != 0:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, distance + 1))

        return -1, None


    # find shortest path between consecutive numbers
    path_length = 0
    start = (0,0)
    last = 1
    for target in range(2, max_item+1):
        distance, location = bfs(start, target)
        if distance == -1:
            return -1 
        
        path_length += distance

        start = location
        print(f"{last} to {target} shortest path = {distance} ")
        last = target
    return path_length



# ============ Q8 ============
def frequencySort(s: str) -> str:
    result = {}

    for item in s:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1


    return ''.join([k * v for k,v in sorted(result.items(), key= lambda x: (-x[1] , ascii(x[0]) ))   ])

# ============ Q9 ============
def min_rooms_required(arrivals_departures: List[Tuple[int, int]]) -> int:
    # heap 
    # similar to minimum machiens problem
    
    # use min heap to keep track of the person closest to their move out day
    rooms = []

    for arrive, depart in sorted(arrivals_departures):

        # check if next arrival comes after the earliest leaves 
        if rooms and rooms[0] < arrive:
            # vacate room, put new person in this room 
            heapq.heappop(rooms)

        # push departure date of this person to heap 
        heapq.heappush(rooms, depart)

    return len(rooms)


# ============ Q10 ============

class Huffman():
    def __init__(self):
        self.huffman_codes = {}
        self.source_string = ""

    def set_source_string(self, src_str):
        self.source_string = src_str
   
    def generate_codes(self):
        huffman_codes = {}
        # Code to generate Huffman codes needs to be written here
        self.huffman_codes = huffman_codes

    def encode_message(self, message_to_encode):
        encoded_msg = ""
        # Code to encode the message needs to be written here
        return encoded_msg
    
    def decode_message(self, encoded_msg):
        decoded_msg = ""
        # Code to decode the message needs to be written here
        return decoded_msg