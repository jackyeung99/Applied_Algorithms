from collections import Counter, defaultdict
from typing import List

# ============ Q1 ============
def longestUniformSegment(boxes: str, changes: int) -> int:

    def max_uniform_with_char(target_char):
        left = 0
        changes_left = changes
        max_len = 0

        for right in range(len(boxes)):
            if boxes[right] != target_char:
                changes_left -= 1

            while changes_left < 0:
                if boxes[left] != target_char:
                    changes_left += 1
                left += 1

            max_len = max(max_len, right - left+1)

        return max_len


    return max(max_uniform_with_char(c) for c in set(boxes))


# ============ Q2 ============

def treasureHunt(parchment1, parchment2):

    dp_matrix = [[0] * len(parchment1) for _ in range(len(parchment2))]


    max_len = 0
    for i in range(len(parchment1)):
        dp_matrix[0][i] = 1 if parchment1[i] == parchment2[0] else dp_matrix[0][i-1]
        max_len = max(max_len, dp_matrix[0][i])

    for j in range(len(parchment2)):
        dp_matrix[j][0] = 1 if parchment2[j] == parchment1[0] else dp_matrix[j-1][0]
        max_len = max(max_len, dp_matrix[0][i])

    for i in range(1, len(parchment2)):
        for j in range(1, len(parchment1)):
            if parchment2[i] == parchment1[j]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1
                max_len = max(max_len, dp_matrix[i][j])
            else: 
                dp_matrix[i][j] = 0
                # dp_matrix[i][j] = max(dp_matrix[i][j-1], dp_matrix[i-1][j])

    # for i in dp_matrix:
    #     print(i)

    return max_len

# ============ Q3 ============
def findMaxLength(nums:list[int]) -> int:
    max_len = 0
    prefix_map = {0: -1}
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum += nums[i] if nums[i] > 0 else -1
        if prefix_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum])
        else:
            prefix_map[prefix_sum] = i

    return max_len
# ============ Q4 ============

def breaches(levels : List[int]):
    results = []
    prefix_map = defaultdict(list)
    prefix_map[0].append(-1)
    prefix_sum = 0
    for i in range(len(levels)):
        prefix_sum += levels[i]

        if prefix_sum in prefix_map:
            for j in prefix_map[prefix_sum]:
                results.append((j+1, i))

        prefix_map[prefix_sum].append(i)  

        
    return results



# ============ Q5 ============

def deleteDuplicateItineraries(itineraries: List[List[str]]) -> List[List[str]]:

    pass