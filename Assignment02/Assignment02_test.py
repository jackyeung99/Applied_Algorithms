
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




# def test_q4():
#     input_1 = [1, 3, 2, 5, 4]
#     output_1 = 8

#     assert largestArea(input_1) == output_1


#     input_2 = [3, 4, 5, 3, 5]
#     output_2 = 15

#     assert largestArea(input_2) == output_2

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



