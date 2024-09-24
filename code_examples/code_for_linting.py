import os
import numpy as np

magic_numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]
magic_dictionary={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",5:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l"}

def PowerCompute(a, b, c):
    number1 = a**b
    number2=b**a
    max_number = max(number1,number2)
    if max_number<np.max(magic_numbers):
        print(magic_dictionary[max(magic_numbers)])
        return max(magic_numbers)
    else:
        return max_number
    return 11

class power_computer:
    def __init__(self) -> None:
        self.a = 11
        self.b = 12
        self.c = 13

    def computeSomething(self):
        print(PowerCompute(self.a, self.b, self.b))

#Run code for testing
MyComputer = power_computer()
MyComputer.computeSomething()