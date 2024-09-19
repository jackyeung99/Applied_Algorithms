

import pytest 
from Assignment01_practical import *

def test_q1():

    n = 2
    operations = [
        (1, "GOT"), # Check if "GOT" is present
        (2, ("GOT", 9)), # Add "GOT" with rating 9
        (1, "GOT"), # Check if "GOT" is present
        (2, ("NARUT", 10)), # Add "NARUT" with rating 10
        (1, "NARUT"), # Check if "NARUT" is present
        (2, ("BARUT", 6)), # Add "BARUT" with rating 6
        (1, "GOT"), # Check if "GOT" is present
        (1, "BARUT"), # Check if "BARUT" is present
        ]
    
    test_output = [-1, 9, 10, -1, 6]
    
    assert processOperations(n, operations) == test_output


    n_2 = 2
    operations_2 = [
        (2, ("GOT", 9)), # Add "GOT" with rating 9
        (2, ("NARUT", 10)), # Add "NARUT" with rating 8
        (1, "GOT"), # Check if "GOT" is present (increases access count)
        (2, ("BARUT", 6)), # Add "BARUT" with rating 6
        (1, "NARUT"), # Check if "NARUT" is present
        (2, ("GOT", 7)), # Update rating of "GOT" (increases access count)
        (2, ("BBAD", 9)), # Add "BBAD" with rating 9
        (1, "BARUT"), # Check if "BARUT" is present
        (1, "GOT"), # Check if "GOT" is present
        (1, "BBAD"), # Check if "BBAD" is present
        ]
    test_output_2 = [9, -1, -1, 7, 9]
    assert processOperations(n_2, operations_2) == test_output_2

def test_q3():

    signal_1 = [5, 4, 9, 11]
    test_1 = [5, 13, 11]


    assert combine_signals(signal_1) == test_1

    signal_2 = [8, 4, 2]
    test_2 = [12, 6 ]

    assert combine_signals(signal_2) == test_2

def test_q4():


    input_1 = [2, 5, 3, 4,1]
    output_1 = 3

    assert numberOfTeams(input_1) == output_1

    input_2 = [2, 1, 3]   
    output_2 = 0

    assert numberOfTeams(input_2) == output_2

def test_q5():

    input1 = [1,2,3,4]
    output1 = [24,12,8,6]


    assert findPowerLevels(input1) == output1

    input2 = [-1,1,0,-3,3]
    output2 = [0,0,9,0,0]

    assert findPowerLevels(input2) == output2

def test_q6():

    input1 = 'aaabbb'
    output1 = 3

    assert decrypt(input1) == output1

    input2 = 'xyyx'
    output2 = 0

    assert decrypt(input2) == output2


def test_q7():

    input1 = 1
    output1 = '1'

    assert magicalScribe(input1) == output1

    input2 = 5
    output2 = '111221'

    assert magicalScribe(input2) == output2

    input3 = 4
    output3 = '1211'

    assert magicalScribe(input3) == output3

def test_q8():

    input1 = 'BAtmAnCavE'
    output1 = 'BAtmAnCEva'

    assert sortVowels(input1) == output1

    input2 = 'bRucEwaYne'
    output2 = 'bREcaweYnu'

    assert sortVowels(input2) == output2

def test_q9():

    # words = ["To","be","or","no","question","answer","is","question"]
    # width = 13
    # output = [
    #         "To  be  or no",
    #         "question     ",
    #         "answer     is",
    #         "question     "
    #         ]
    # assert helpElara(words, width) == output


    words2 =  [
        "Hello",
        "world",
        "this",
        "is",
        "a",
        "test",
        "of",
        "help",
        "Elara"
    ],
    width2 = 15  
    output2 = [
    "Hello     world",
    "this  is a test",
    "of help Elara  "
    ]
   

    assert helpElara(words2, width2) == output2