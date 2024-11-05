from typing import List, Tuple
from collections import deque, Counter, defaultdict

import heapq


# ============ Q1 ============
class Node:
    def __init__(self, data, val=None, left = None, right = None):
        self.data = data
        self.val = val
        self.left = left
        self.right = right

class Wavelet_Tree:
    def __init__(self, A:list[int]=[]):
        self.A = A
        self.char_bitmap = defaultdict(str)
        self.root = self.build_tree(A, min(A), max(A))

    def build_tree(self, A, low, high):
        
        # found individual item
        if low == high:
            freq = ''.join(['X'] * len(A)) 
            node = Node(freq)
            node.val = A[0]
            return node


        mid = int((low + high) / 2)

        left_sub_tree, right_sub_tree, bit_vec = [], [], []

        processed = set()

        for num in A:
            if num <= mid:
                left_sub_tree.append(num)
                bit_vec.append('0')

                if num not in processed:
                    processed.add(num) 
                    self.char_bitmap[num] += '0'
            else:
                right_sub_tree.append(num)
                bit_vec.append('1')

                if num not in processed:
                    processed.add(num) 
                    self.char_bitmap[num] += '1'
    
        node = Node(''.join(bit_vec))
        node.left = self.build_tree(left_sub_tree, low, mid)
        node.right = self.build_tree(right_sub_tree, mid + 1, high)
        
        return node

    def get_wavelet_level_order(self):
        # Return level order traversal of the tree.
        if not self.root:
            return []

        level_order = []
        queue = deque([self.root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            level_order.append(level)
            
        # for level in level_order:
        #     print(level)
   
        return level_order

    def rank(self, character, position):
    
        path = self.char_bitmap[character] 

        node = self.root
        rank = position

        for char in path:
            bitmap = node.data
            if char == '0':
                node = node.left
            else:
                node = node.right

            rank = sum(1 for i in range(rank) if bitmap[i]==char)
            
        return rank

            






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
    if len(scroll1) + len(scroll2) != len(scroll3):
        return False

    # dynamic programming approach 
    # Similar to subset sum and approximate string matching 

    dp_arr = [[False for _ in range(len(scroll1)+1)] for _ in range(len(scroll2)+1)]
    dp_arr[0][0] = True

    # initialize how many elements each scroll independly can cover scroll3
    for j in range(1, len(scroll1) + 1):
        dp_arr[0][j] = dp_arr[0][j - 1] and scroll1[j - 1] == scroll3[j - 1]

    for i in range(1, len(scroll2) + 1):
        dp_arr[i][0] = dp_arr[i - 1][0] and scroll2[i - 1] == scroll3[i - 1]

    for i in range(1, len(scroll2)+1):
        for j in range(1, len(scroll1)+1):
            

            # check that next element in each scroll is the same as last element in scroll 3
            # check that all previous elements match as well
            if dp_arr[i][j-1] and scroll1[j-1] == scroll3[i+j-1]:
                dp_arr[i][j] = True

            if dp_arr[i-1][j] and scroll2[i-1] == scroll3[i+j-1]:
                dp_arr[i][j] = True



    for arr in dp_arr:
        print(arr)
    return dp_arr[-1][-1]

# ============ Q4 ============

def magical_recipe(T: int, cases: list[str]) -> list[int]:
    # Implement the logic here to return the result for each test case
    

    def count_paths(string):
        dp_arr = [0] * (len(string) + 1)
        dp_arr[0] = 1
        
        for i in range(len(string)):
            # kind of a base cases where we assume step size of 1
            dp_arr[i + 1] += dp_arr[i] 

            # simulate a recyursive split 
            # one path jumps two indexes
            if i < len(string) - 1 and string[i] == 'a' and string[i + 1] == 'b':
                # add results to all of the paths from one step
                dp_arr[i + 2] += dp_arr[i]

            if i < len(string) - 1 and string[i] == 'b' and string[i + 1] == 'a':
                dp_arr[i + 2] +=  dp_arr[i]

        # print(dp_arr)
        return dp_arr[-1]

    result = []
    for i in range(T):
        string = cases[i]
        result.append(count_paths(string) % 998244353)

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


    items = sorted({cell for row in matrix for cell in row if cell > 0})[1:]
    # find shortest path between consecutive numbers
    path_length = 0
    start = (0,0)
    last = 1
    for target in items:
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
        frequency = Counter(list(self.source_string)) 

        huffman_codes = {k: [] for k, v in frequency.items()}
        heap = [(freq, char) for char, freq in frequency.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)

            for char in char1:
                huffman_codes[char] = ['0'] + huffman_codes.get(char, [])
            for char in char2:
                huffman_codes[char] = ['1'] + huffman_codes.get(char, [])

            combined_freq = freq1 + freq2
            combined_elem = char1 + char2
            heapq.heappush(heap, (combined_freq, combined_elem))


        print({k: ''.join(v) for k,v in huffman_codes.items()})
        self.huffman_codes = {k: ''.join(v) for k,v in huffman_codes.items()}

    def encode_message(self, message_to_encode):
        encoded_msg = ""
        
        for char in message_to_encode:
            encoded_msg += self.huffman_codes[char]


        return encoded_msg
    
    def decode_message(self, encoded_msg):
        reverse_codes = {v: k for k, v in self.huffman_codes.items()}
        
        decoded_string = ""
        current_code = ""
        
        for bit in encoded_msg:
            current_code += bit
            if current_code in reverse_codes:
                decoded_string += reverse_codes[current_code]
                current_code = ""  
        
        return decoded_string