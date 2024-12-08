import pytest
from Assignment06_practical import *

def test_q1():
    boxes = "aabbcc"
    changes = 6
    assert longestUniformSegment(boxes, changes) == 6

    boxes = "abcbbab"
    changes = 2
    assert longestUniformSegment(boxes, changes) == 6

    boxes = "abcde"
    changes = 0
    assert longestUniformSegment(boxes, changes) == 1

    boxes = "hasgdjgug"
    changes = 1
    assert longestUniformSegment(boxes, changes) == 3

    boxes  = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    changes = 10
    assert longestUniformSegment(boxes, changes) == 11

def test_q2():
    parchment1 = [5, 7, 8, 7, 5, 6]
    parchment2 = [8, 7, 5, 3, 9]

    assert treasureHunt(parchment1, parchment2) == 3

    parchment1 = [1, 1, 1, 1, 1]
    parchment2 = [1, 1, 1, 1, 1]
    assert treasureHunt(parchment1, parchment2) == 5

    parchment1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    parchment2 = [ 1, 2, 3, 5, 6, 7, 8, 10 ]
    assert treasureHunt(parchment1, parchment2) == 4

def test_q3():

    nums = [0,1]
    assert findMaxLength(nums) == 2

    nums = [0,1,0]
    assert findMaxLength(nums) == 2



def test_q4():
    levels = [3, 4, -7, 1, 2, -6, 4, -1]
    assert breaches(levels) == [(0, 2), (1, 4), (4, 6), (0, 7), (3, 7)]

    levels = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    assert breaches(levels) == [(2, 4), (2, 6), (5, 6), (6, 9), (0, 10)]


def test_q5():
    itin = [["John"], ["Priya"], ["Vikram"], ["John", "Chicago"], ["Priya", "Chicago"]]

    assert deleteDuplicateItineraries(itin)

