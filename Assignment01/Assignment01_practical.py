from typing import List, Tuple, Union
import heapq 

# ============ Q1 ============
def processOperations(n: int, operations: List[Tuple[int, Union[str, Tuple[str, int]]]]): 
    output = []
    #keep movie name, rating, access count, and time
    movie_info = {}
  
    
    for idx, i in enumerate(operations):

        # check if in
        if i[0] == 1:
            movie = i[1]

            if movie in movie_info:
            
                output.append(movie_info[movie][0])
                movie_info[movie][1] += 1
       
            else:
                output.append(-1)             
            
        #update hard drive
        else:
            new_movie, rating = i[1]
            
            if new_movie in movie_info:
                movie_info[new_movie][0] = rating
                movie_info[new_movie][1] += 1
    
            else:

                if len(movie_info) >= n:
                    lowest_movie = min(movie_info, key = lambda x: (movie_info[x][1], movie_info[x][2]))
                    del movie_info[lowest_movie]

                movie_info[new_movie] = [rating, 1, idx]

    
    return output



# ============ Q3 ============
def combine_signals(signals):
    return [(signals[i-1] | signals[i]) for i in range(1, len(signals))]

# ============ Q4 ============
def numberOfTeams(ratings:List[int])->int:

    #brute force
    # teams = 0
    # for i in range(len(ratings)):
        
    #     for j in range(i + 1 , len(ratings)):
            
    #         for k in range(j + 1, len(ratings)):

    #             if (ratings[i] < ratings[j] < ratings[k]) or (ratings[i] > ratings[j] > ratings[k]):
    #                 teams += 1

    # return teams

    team_count = 0
    for j in range(len(ratings)):
        
        left_less = 0
        left_greater = 0
        right_less = 0
        right_greater = 0

        for i in range(j):
            if ratings[i] < ratings[j]:
                left_less += 1
            elif ratings[i] > ratings[j]:
                left_greater += 1

        for k in range(j+1, len(ratings)):
            if ratings[k] < ratings[j]:
                right_less += 1
            elif ratings[k] > ratings[j]:
                right_greater += 1

        team_count += (left_less * right_greater) + (left_greater * right_less)

    return team_count

# ============ Q5 ============
def findPowerLevels(powerLevels: list[int]) -> list[int]:
    final_powerLevels = [1] * len(powerLevels)

    left_product = 1
    for i in range(len(powerLevels)):
        final_powerLevels[i] = left_product
        left_product *= powerLevels[i]

    right_product = 1
    for i in range(len(powerLevels)-1, -1, -1):
        final_powerLevels[i] *= right_product
        right_product *= powerLevels[i]

    return final_powerLevels

# ============ Q6 ============
def decrypt(s:str)->int:
    if len(s) % 2 == 1:
        return -1 
    
    seen1 = {}
    seen2 = {}    

    halves = int(len(s)/2)
    for i in range(halves):
        char1 = s[i]
        if char1 in seen1:
            seen1[char1] += 1
        else:
            seen1[char1] = 1

        char2 = s[halves+i]
        if char2 in seen2:
            seen2[char2] += 1
        else:
            seen2[char2] = 1


    changes_needed = 0
    
    for c in seen2:
        if c in seen1:
            if seen2[c] > seen1[c]:
                changes_needed += abs(seen2[c] - seen1[c])
        else:
    
            changes_needed += seen2[c]
    
    return changes_needed

# ============ Q7 ============
def magicalScribe(n: int) -> str: 
    if n == 1:
        return '1'
    

    def decode_sequence(sequence):
        end_sequence = []
        count = 1
        
        for i in range(1, len(sequence)):

            if sequence[i] == sequence[i-1]:
                count += 1
            else:
                end_sequence.append(f"{count}{sequence[i-1]}")
                count = 1

        end_sequence.append(f"{count}{sequence[-1]}")
        return ''.join(end_sequence)
    

    str = '1'
    for i in range(1,n):
        str = decode_sequence(str)
      
    return str

# ============ Q8 ============
def sortVowels(code: str) -> str:
    str_vowels = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in code:
        if char.lower() in vowels:
            str_vowels.append(char)
    
    str_vowels.sort(key= lambda x:ascii(x))
    result = []
    for char in code:
        if char.lower() in vowels:
            result.append(str_vowels.pop(0))
        else:
            result.append(char)

    return ''.join(result)

# ============ Q9 ============
def helpElara(words: List[str], width: int) -> List[str]:
    results = []
    line = []
    buffer_length = 0
    for word in words[:-1]:
        print(word, len(word))
        if len(word) + 1 + buffer_length <= width:
            line.append(word)
            buffer_length += len(word) + 1
        else:

            filled_line = fill_spaces(line, width)
            results.append(filled_line)
            line = [word]
            buffer_length = len(word) +1 

    #clear last line   
    filled_line = fill_spaces(line, width)
    results.append(filled_line)
    # add last word
    final_word = words[-1] 
    filled_last = fill_spaces([final_word], width) 
    results.append(filled_last)

    print([len(x) for x in results])
    return results

def fill_spaces(line, width):

    word_lengths = sum([len(x) for x in line])
    spaces_needed = width - word_lengths
    gaps = len(line) -1 

    if gaps == 0:
        return ' '.join(line).ljust(width)
    
   
    spaces_per_gap = spaces_needed // gaps
    #left over spaces
    extra_spaces = spaces_needed % gaps

    result = ""
    for i in range(gaps):
        result += line[i] + ' ' * (spaces_per_gap + (1 if i < extra_spaces else 0))
     
    result += line[-1]
  
    return result

# ============ Q10 ============
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def findTreasure(head):
    fast = head
    while fast and fast.next: 
        head = head.next
        fast = fast.next.next

        if head is fast:
            return False

    return True