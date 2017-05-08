'''
Created on 8 May 2017

@author: Janion
'''
from OrderOfOperations import OrderOfOperations

if __name__ == '__main__':
    o = OrderOfOperations()
    
    fn = "251"
    print fn, " -> ", o.addBrackets(fn), "\n"
         
    fn = "25 + 1"
    print fn, " -> ", o.addBrackets(fn), "\n"
       
    fn = "25 / (7 + 1) ^ 9 * (sin(t) - 4)"
    print fn, " -> ", o.addBrackets(fn), "\n"
      
    fn = "7 * 9 / 7 * 9"
    print fn, " -> ", o.addBrackets(fn), "\n"
        
    fn = "7 / 9 * 7 / 9"
    print fn, " -> ", o.addBrackets(fn), "\n"
         
    fn = "2 * 5 / 6 * 4"
    print fn, " -> ", o.addBrackets(fn), "\n"
        
    fn = "2 ^ 5 ^ 6 ^ 4"
    print fn, " -> ", OrderOfOperations().addBrackets(fn), "\n"
       
    fn = "2 ^ 5 ^ 6 ^ 4 + 3"
    print fn, " -> ", o.addBrackets(fn), "\n"