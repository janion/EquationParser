'''
Created on 8 May 2017

@author: Janion
'''
from eqn.NegativeNumberAdjuster import NegativeNumberAdjuster

if __name__ == '__main__':
    a = NegativeNumberAdjuster()

    print(a.adjust("-2"))
    print(a.adjust("2 * (-2 * 4)"))
    print(a.adjust("2 * (x^-2 * 4)"))
    print(a.adjust("sin(sqrt(((x - 4.5) * (x - 4.5)) + ((y - 4.5) * (y - 4.5))) - (2 * sin(t))) + 1"))
    print(a.adjust("2 * (x--2 * (4 / (3 + 2)) + 1)"))
    print(a.adjust("2 * (x+-(4 / (3 + 2)) + 1)"))