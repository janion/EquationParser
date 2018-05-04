'''
Created on 7 May 2017

@author: Janion
'''

from eqn.EquationParser import Equation

if __name__ == '__main__':
    eqn = Equation("((sin((x+1)/t)) * (sin((x+1)/t))) + ((cos((x+1)/t)) * (cos((x+1)/t)))")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("sin((x+1)/t) * sin((x+1)/t)")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("cos((x+1)/t) * cos((x+1)/t)")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("(sin((x+1)/t) * sin((x+1)/t)) + (cos((x+1)/t) * cos((x+1)/t))")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("(1+x)/t")
    print eqn.evaluate(1., 2., 4.)
    
    eqn = Equation("(y-1)/t")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("1.12*x")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("(1.12*x)+y")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("sin(t)")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("sqrt(t)")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("sqrt((2*x) + y) / t")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("sqrt(4) + 2")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("0")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("tan(3.1415926535 / 2)")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("y + (x / 0)")
    print eqn.evaluate(1., 2., 4.)
             
    eqn = Equation("3 + sqrt( 1 - ( ( (x-3) * (x-3)) + ( (y-3) * (y-3) ) ) )")
    print eqn.evaluate(3., 3., 4.)
    print eqn.evaluate(2., 3., 4.)
    print eqn.evaluate(2., 2., 4.)
            
    eqn = Equation("sqrt(sqrt(x))")
    print eqn.evaluate(1., 2., 4.)
            
    eqn = Equation("((1 / 0) * 0) + 7")
    print eqn.evaluate(1., 2., 4.)
            
    eqn = Equation("((1 / 0) * 0) + 7")
#     eqn.setRange(Range(0, 5))
    print eqn.evaluate(1., 2., 4.)
            
    eqn = Equation("abs(0-7)")
    print eqn.evaluate(1., 2., 4.)
            
    eqn = Equation("exp(1)")
    print eqn.evaluate(1., 2., 4.)
    
    eqn = Equation("log(exp(1))")
    print eqn.evaluate(1., 2., 4.)
    
    eqn = Equation("11 % 7")
    print eqn.evaluate(1., 2., 4.)
    
    eqn = Equation("2 ^ 9")
    print eqn.evaluate(1., 2., 4.)