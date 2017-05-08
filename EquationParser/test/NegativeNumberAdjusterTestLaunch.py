'''
Created on 8 May 2017

@author: Janion
'''
from src.NegativeNumberAdjuster import NegativeNumberAdjuster

if __name__ == '__main__':
    a = NegativeNumberAdjuster()
    
    print a.adjust("-2")
    print a.adjust("2 * (-2 * 4)")
    print a.adjust("2 * (x^-2 * 4)")
    print a.adjust("sin(sqrt(((x - 4.5) * (x - 4.5)) + ((y - 4.5) * (y - 4.5))) - (2 * sin(t))) + 1")