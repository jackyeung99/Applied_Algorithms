import pytest 
from Assignment04_practical import *


def test_q1():
    s = 'aab'
    print(palin_break(s))


def test_q2():
    pass
def test_q3():
    pass

def test_q4():
    n = 3
    strings = ['ab', 'aa', 'abb']

    assert magical_recipe(n, strings) == [2,1,2]

    n = 2
    strings = ['aaaa', 'bbb']
    assert magical_recipe(n, strings) == [1,1]

    n = 1

    strings = [ "aababbab"]
    assert magical_recipe(n, strings) == [16]

    n = 1
    strings = [
        "ababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbabababababababababababababababbababababababababab"
    ]
    assert magical_recipe(n, strings) == [915793674]

    n = 1,
    strings = [
        "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
    ]
    assert magical_recipe(n, strings) == [956396364]


def test_q5():
    tasks = ['A','A','A','B','B','B']
    n = 2 
    assert lelouch_task_schedule(tasks, n) == 8

def test_q6():
    # orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
    
    # assert rajsTradingShowdown(orders) == 6
    
    orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
    assert rajsTradingShowdown(orders) == 999999984

def test_q7():
    matrix = [[1,2,3],
              [0,0,4],
              [7,6,5]]

    assert collect_items(matrix) == 6

    matrix = [
        [1, 2, 3, 4, 5 ],
        [0, 0, 0, 0, 6 ],
        [11,12,13,14, 7],
        [10, 0, 0, 0, 8],
        [9, 16, 15, 0,1 ]
    ]

    assert collect_items(matrix) == 27

    




def test_q8():
    s = 'tree'

    assert frequencySort(s) == 'eert'

def test_q9():

    arrivals_departures = [(1,2), (2,3), (4,4)]

    assert min_rooms_required(arrivals_departures) == 2



def test_q10():
    pass 
