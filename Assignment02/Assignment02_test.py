
import pytest 
from Assignment02_practical import *


def test_q1():
    target = [1, 3]
    n = 3 
    output = ["Push","Push","Pop","Push"]

    assert treasure_seq(target, n) == output


    target = [1,2,3]
    n = 3 
    output = ["Push","Push","Push"]

    assert treasure_seq(target, n) == output


    target = [1,2]
    n = 4
    output = ['Push', 'Push']

    assert treasure_seq(target, n) == output


    target = [2, 4]
    n = 4
    output = ["Push", "Pop", "Push", "Push", "Pop", "Push"]
    assert treasure_seq(target, n) == output



def test_q2():

    def run_operations(opearations):
        for i in operations:
            if len(i) > 1:
                queue.enqueue(i[1])
            else:
                queue.dequeue()

        return queue.QueueToList()

    queue = Queue_LL()
    operations = [["enqueue", 1], ["enqueue", 2], ["enqueue", 3], ["dequeue"], ["enqueue", 4], ["dequeue"], ["dequeue"], ["enqueue", 6]]
    assert run_operations(operations) == [4, 6]

    queue = Queue_LL()
    operations = [['enqueue', 1], ['dequeue'], ['dequeue'], ['enqueue', 6], ['dequeue']]    
    assert run_operations(operations) == []


def test_q3():

    operations = ["2","1","+","3","*"]
    expected = 9
    assert spiritualArithmetic(operations) == expected

    operations = ["4","13","5","/","+"]
    expected = 6
    assert spiritualArithmetic(operations) == expected

    operations = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    expected = 22
    assert spiritualArithmetic(operations) == expected

def test_q4():
    input_1 = [1, 3, 2, 5, 4]
    output_1 = 8

    assert largestArea(input_1) == output_1


    input_2 = [3, 4, 5, 3, 5]
    output_2 = 15

    assert largestArea(input_2) == output_2

def test_q5():

    input  = [17, 13, 11, 2, 3, 5, 7]
    output = [2, 13, 3, 11, 5, 17, 7]

    assert arrangePerformers(input) == output

    input = [1001, 1]
    output = [1, 1001]

    assert arrangePerformers(input) == output


def test_q6():

    input = "Mg(OH)2"   
    output = "H2MgO2"

    assert atom_counter(input) == output

    input = "H2O"
    output = "H2O"

    assert atom_counter(input) == output

    input = "H2SO4"
    output = "H2O4S"

    assert atom_counter(input) == output

    input = "((H2O)2)3"
    output = "H12O6"

    assert atom_counter(input) == output

def test_q7():
    input = [0,1,1,2,4]
    action = [0,1,0,0,1]
    output = [0,3,1,2,4]

    assert checkout_counter_times(input, action) == output

    input = [0,0,0]
    action = [1,0,1]
    output = [0,2,1]

    assert checkout_counter_times(input, action) == output

    input = [3, 3, 4, 5, 5, 5]
    action = [1, 0, 1, 0, 1, 0]
    output = [3, 6, 4, 7, 5, 8]

    assert checkout_counter_times(input, action) == output

    
    input = [0, 0, 0, 1, 2, 3, 4, 40]
    action = [0, 0, 1, 0, 1, 1, 0, 0]
    output = [1, 2, 0, 3, 5, 6, 4, 40]

    # 2, 0, 1, 3, 6, 4, 5 

    assert checkout_counter_times(input, action) == output

def test_q8():

    def test_helper(input):
        qp = quarryPieLine()
        operations =  {
            1: qp.joinInFront,
            2: qp.joinInMiddle,
            3: qp.joinInBack,
            4: qp.removeFromFront,
            5: qp.removeFromMiddle,
            6: qp.removeFromBack,
            7: qp.whoIsFront,
            8: qp.whoIsMiddle,
            9: qp.whoIsBack
        }

        result = []
        for i in input:
            # print(f"operation {i}")
            j = operations[i]()
            if j:
                result.append(j)
            # print(f"Line {qp.print_list()}")
            # print(f"result {result}")

        return result

    input = [1, 2, 2, 3, 5, 6, 7, 8, 9]
    assert test_helper(input) == [2,2,1]

    input = [2, 7, 8, 9, 1, 3, 2, 7, 8, 9, 2, 3, 5, 6, 7, 8, 9]
    assert test_helper(input) == [1, 1, 1, 2, 4, 3, 2, 4, 3]

    input = [1, 6, 2, 5, 3, 4, 2, 2, 2, 7, 8, 9, 3, 3, 3, 1, 2, 3, 1, 1, 2, 2, 2, 3, 7, 8, 9, 4, 6, 5, 4, 7, 8, 9, 5, 6, 6, 5, 4, 7, 8, 9]
    assert test_helper(input) == [ 5, 6, 4, 14, 16, 18, 10, 11, 12, 5, 17, 8]


def test_q9():
    ad = amor_dict([23, 12, 24, 42])
    assert ad.print() ==  [[], [], [12, 23, 24, 42]]
    ad.insert(11)
    assert ad.print() ==  [[11], [], [12, 23, 24, 42]]
    ad.insert(74)
    assert ad.print() == [[], [11, 74], [12, 23, 24, 42]]
    assert ad.search(74) == 1
    assert ad.search(77) == -1

    ad = amor_dict([1, 5, 2, 7, 8, 4, 3])
    assert ad.print()  == [[3], [4, 8], [1, 2, 5, 7]]
    assert ad.search(1) == 2
    ad.insert(11)
    print(ad.print())
    assert ad.print() == [[], [], [], [1, 2, 3, 4, 5, 7, 8, 11]]
    assert ad.search(1) == 3


def test_q10():
    sl = SkipList()
    sl.insert(1) # None
    sl.insert(2) # None
    sl.insert(3) # None
 
    print(sl.search(4)) # False
    sl.insert(4) # None
    print(sl.search(4)) # True
    print(sl.search(1)) # True



   