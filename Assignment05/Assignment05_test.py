import pytest 
from Assignment05_practical import *

def test_q1():
    v = 3
    routes = [[0, 1], [1, 2], [2, 0]]
    home = 0
    target = 2

    assert princeJourney(v, routes, home, target) 

    v = 6
    routes = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    home = 0
    target = 4

    assert not princeJourney(v, routes, home, target) 


def test_q2():
    checkpoints = 5
    paths = 6
    network = [(1, 2, 3), (2, 3, 2), (3, 5, 1), (1, 4, 4), (4, 5, 3), (2, 4, 1)]

    assert constrainedNetwork(checkpoints, paths, network) == 6

    checkpoints = 5
    paths = 3
    network = [(1, 2, 1), (2, 3, 2), (4, 5, 3)]
    assert constrainedNetwork(checkpoints, paths, network) == -1

def test_q3():
    n = 4
    highways = [(1,2), (1, 3), (1, 4)]
    IsDiwali = [0, 0, 1, 0]

    assert MostFestiveExperience(n, highways, IsDiwali) ==  [0, -1, 1, -1]


    n = 5
    highways = [(1,2),(2,3),(3,4),(3,5)]
    IsDiwali = [0, 1, 0, 1, 0]
    assert MostFestiveExperience(n, highways, IsDiwali) == [0, 1, 1, 1, 0]

def test_q4():
    dominion = [[1,1,0],[1,1,0],[0,0,1]]
    assert findDominion(dominion) == 2

    dominion = [[1,0,0],[0,1,0],[0,0,1]]
    assert findDominion(dominion) == 3

def test_q5():
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    assert not Rangipur_Network(graph)

    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert Rangipur_Network(graph)

def test_q6():
    points = [[3,12],[-2,5],[-4,1]]
    assert minCostConnectPoints(points) == 18

    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    assert minCostConnectPoints(points) == 20

def test_q7():
    n = 4
    routes = [[0, 1, 100, 'bus'], [1, 2, 100, 'train'], [2, 3, 100, 'train'],
    [0, 3, 500, 'bus']]
    src = 0
    dst = 3
    K = 1

    assert findCheapestLandTransport(n, routes, src, dst, K) == 500

    n = 3
    routes = [[0, 1, 300, 'bus'], [1, 2, 300, 'bus'], [0, 2, 700, 'train']]
    src = 0
    dst = 2
    K = 1

    assert findCheapestLandTransport(n, routes, src, dst, K) == 600

    n = 3
    routes = [[0, 1, 100, 'train'], [1, 0, 100, 'bus']]
    src = 0
    dst = 2
    K = 1
    assert findCheapestLandTransport(n, routes, src, dst, K) == -1

def test_q8():
    n = 8
    connections = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    assert influencer_network(n, connections) == [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]

    n = 5
    connections = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert influencer_network(n, connections) == [[],[0],[0,1],[0,1,2],[0,1,2,3]]

def test_q9():
    n = 1
    s = '()'

    assert GraphInGokuldham(n, s) == 1

    n = 3
    s = '()(())'

    assert GraphInGokuldham(n, s) == 2

def test_q10():
    n = 6
    streets = [[0, 1], [1, 2], [2, 3], [3, 0], [3, 4], [4, 5]]
    assert festiveWalkPath(n, streets) == 4

    n = 6
    streets = [[1, 2], [2, 3], [4, 5]]
    assert festiveWalkPath(n, streets) == -1

    n = 100
    streets = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,0],[5, 11], [6,12], [7,13], [8,14], [9,5], [10,6], [11,7], [12,8], [13,9], [14,10]]
    assert festiveWalkPath(n, streets) == 4
    

def test_q11():
    n= 6
    edges=[[0,1], [1,2], [2,3], [4,5]]

    assert countComponents(n, edges) == 2

    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    assert countComponents(n, edges) == 2