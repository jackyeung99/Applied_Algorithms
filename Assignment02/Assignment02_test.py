
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



def test_q3():
    queue = Queue_LL

    operations = [['enqueue', 1], ['dequeue'], ['dequeue'], ['enqueue', 6], ['dequeue']]


    for i in operations:
        if len(i) > 1:
            queue.enqueue(i[1])
        else:
            queue.dequeue()


        print(queue.QueueToList)




def test_q4():
    input_1 = [1, 3, 2, 5, 4]
    output_1 = 8

    assert largestArea(input_1) == output_1


    input_2 = [3, 4, 5, 3, 5]
    output_2 = 15

    assert largestArea(input_2) == output_2