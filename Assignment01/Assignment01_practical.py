from typing import List, Tuple, Union



def processOperations(n: int, operations: List[Tuple[int, Union[str, Tuple[str, int]]]]): 
    pass

def combine_signals(signals):
    return [(signals[i-1] | signals[i]) for i in range(1, len(signals))]


def numberOfTeams(ratings:List[int])->int:

    teams = 0
    for i in range(len(ratings)):
        
        for j in range(i + 1 , len(ratings)):
            
            for k in range(j + 1, len(ratings)):

                if (ratings[i] < ratings[j] < ratings[k]) or (ratings[i] > ratings[j] > ratings[k]):
                    teams += 1

    return teams
    


def findPowerLevels(powerLevels: list[int]) -> list[int]:
    pass
    # n = len(powerLevels)
    # newPower = [1] * n

    # left_product = 1
    # for i in range(n):
    #     newPower[i] = left_product
    #     left_product *= powerLevels[i]

    # right_product = 1
    # for i in range(n-1, -1, -1):
    #     newPower[i] *= right_product
    #     right_product *= powerLevels[i]

    # return newPower


def decrypt(s:str)->int:
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


def magicalScribe(n: int) -> str: 

    pass


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