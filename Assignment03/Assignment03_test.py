import pytest 
from Assignment03_practical import *
from boiler_plate_code import *

def test_q1():
    root = buildTree_stores([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    s1 = 5
    s2 = 1
    assert find_nearest_common_facility(root, s1, s2) == 3

    s1 = 5
    s2 = 4
    assert find_nearest_common_facility(root, s1, s2) == 5


def test_q2():
    pass

def test_q3():
    # n = 4
    # assert beautiful_formation(n) == [1, 3, 2, 4] 

    n = 5
    assert beautifulNinjaFormation(n) == [1, 5, 3, 2, 4] 

def test_q4():
    pass

def test_q5():
    points = [3, 99, 155, 8]
    assert endgameScores(points) == True

    points = [5, 1, 100, 1, 5]
    assert endgameScores(points) == False



def test_q6():
    X = 4
    k = 3

    assert satisfyingOrders(X,k) == 6

    X = 5
    k = 3

    assert satisfyingOrders(X,k) == 35

    X = 6
    k = 3

    assert satisfyingOrders(X,k) == 225

def test_q7():
    n = 3 
    assert batmanSignal(n) == ["yxy","yxx","xyx","xxy","xxx"]

def test_q8():
    n = 3
    k = 3
    assert sacred_sequence(n,k) == '213'

    n = 4
    k = 9
    assert sacred_sequence(n,k) == '2314'

def test_q9():
    head = array_to_list([1,2,6,3,4,5,6])
    assert removeElements(head, 6).val == 1

    head = array_to_list([7,7,7,7])
    assert removeElements(head, 7) == None
    


def test_q10():
    toys = [1, 5, 1, 1, 6, 4]
    assert rearrangeAllToys(toys) == [1, 6, 1, 5, 1, 4] 

    toys = [1, 3, 2, 2, 3, 1] 
    assert rearrangeAllToys(toys) == [2, 3, 1, 3, 1, 2] 

def test_q11():
    
    root = buildTree([3,9,20,None,None,15,7])
    assert puzzleOfTheTrees(root) == [[9],[3,15],[20],[7]]

    root = buildTree([1,2,3,4,5,6,7])
    assert puzzleOfTheTrees(root) == [[4],[2],[1,5,6],[3],[7]]

    root = buildTree([1,2,3,4,6,5,7])
    assert puzzleOfTheTrees(root) == [[4],[2],[1,5,6],[3],[7]]