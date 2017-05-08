'''
Created on 14 Oct 2016

@author: Janion

Project to parse functions of x, y & t using operators:
+, -, *, /, sin, cos, tan, exp, log, abs & sqrt.
Each individual operation much be surrounded by a pair of brackets
such that a chain of operations such as:
"x + y * t - 2"
would be written as:
"x + ((y * t) - 2)"
'''

import abc
import math
from src.OrderOfOperations import OrderOfOperations

class Operator(object):
    __metaclass__  = abc.ABCMeta
    
    def __init__(self, equation):
        self.equation = equation
        
################################################################################
 
    @abc.abstractmethod
    def evaluate(self):
        raise NotImplementedError()
        
################################################################################
    
    def setVar1(self, var1):
        self.var1 = var1
        
################################################################################
    
    def setVar2(self, var2):
        self.var2 = var2
        
################################################################################
################################################################################

class Add(Operator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        eval2 = self.var2.evaluate()
        
        for x in eval1:
            for y in eval2:
                answer.append(x + y)
        return answer
        
################################################################################
################################################################################

class Minus(Operator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        eval2 = self.var2.evaluate()
        
        for x in eval1:
            for y in eval2:
                answer.append(x - y)
        return answer
        
################################################################################
################################################################################

class Multiply(Operator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        eval2 = self.var2.evaluate()
        
        for x in eval1:
            for y in eval2:
                answer.append(x * y)
        return answer
        
################################################################################
################################################################################

class Divide(Operator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        eval2 = self.var2.evaluate()
        
        for x in eval1:
            for y in eval2:
                if y != 0:
                    answer.append(x / y)
                else:
                    answer.append(self.equation.INF)
        return answer
        
################################################################################
################################################################################

class Modulo(Operator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        eval2 = self.var2.evaluate()
        
        for x in eval1:
            for y in eval2:
                if y != 0:
                    answer.append(x % y)
                else:
                    answer.append(self.equation.INF)
        return answer
        
################################################################################
################################################################################

class Power(Operator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        eval2 = self.var2.evaluate()
        
        for x in eval1:
            for y in eval2:
                answer.append(math.pow(x, y))
        return answer
        
################################################################################
################################################################################
    
class SingleArgumentOperator(Operator):
    @abc.abstractmethod
    def evaluate(self):
        raise NotImplementedError()
        
################################################################################
################################################################################

class NullOperation(SingleArgumentOperator):
    def evaluate(self):
        return self.var1.evaluate()
        
################################################################################
################################################################################

class Sin(SingleArgumentOperator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        
        for x in eval1:
            answer.append(math.sin(x))
        return answer
        
################################################################################
################################################################################

class Cos(SingleArgumentOperator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        
        for x in eval1:
            answer.append(math.cos(x))
        return answer
        
################################################################################
################################################################################

class Tan(SingleArgumentOperator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        
        for x in eval1:
            answer.append(math.tan(x))
        return answer
        
################################################################################
################################################################################

class Sqrt(SingleArgumentOperator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        
        for x in eval1:
            if x >= 0:
                result = math.sqrt(x)
                answer.append(result)
                answer.append(-result)
        return answer
        
################################################################################
################################################################################

class Exp(SingleArgumentOperator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        
        for x in eval1:
            answer.append(math.exp(x))
        return answer
        
################################################################################
################################################################################

class Log(SingleArgumentOperator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        
        for x in eval1:
            answer.append(math.log(x))
        return answer
        
################################################################################
################################################################################

class Abs(SingleArgumentOperator):
    def evaluate(self):
        answer = []
        eval1 = self.var1.evaluate()
        
        for x in eval1:
            answer.append(abs(x))
        return answer
        
################################################################################
################################################################################

class Constant(SingleArgumentOperator):
    def evaluate(self):
        return [self.var1]
        
################################################################################
################################################################################

class X(Operator):
    def evaluate(self):
        return [self.equation.getX()]
        
################################################################################
################################################################################

class Y(Operator):
    def evaluate(self):
        return [self.equation.getY()]
        
################################################################################
################################################################################

class T(Operator):
    def evaluate(self):
        return [self.equation.getT()]
        
################################################################################
################################################################################

class Equation():
    
    INF = float("inf")
    NUMERALS = ".0123456789"
    
    SIN = "sin"
    COS = "cos"
    TAN = "tan"
    SQRT = "sqrt"
    EXP = "exp"
    LOG = "log"
    ABS = "abs"
    
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULO = "%"
    POWER = "^"
    OPERATIONS = PLUS + MINUS + MULTIPLY + DIVIDE + MODULO + POWER
    
    X = "x"
    Y = "y"
    T = "t"
    VARIABLES = X + Y + T
    
    SPACE = " "
    OPEN_BRACKET = "("
    CLOSE_BRACKET = ")"
    
    def __init__(self, string):
        order = OrderOfOperations()
        orderedString = order.addBrackets(string)
        self.operation = self.parseEquation(orderedString)
        
################################################################################
        
    def getX(self):
        return self.x
        
################################################################################
        
    def getY(self):
        return self.y
        
################################################################################
        
    def getT(self):
        return self.t
        
################################################################################
    
    def evaluate(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t
        
        if self.operation != None:
            return self.operation.evaluate()
        
################################################################################
    
    def makeVariable(self, char):
        if char == self.X:
            return X(self)
        elif char == self.Y:
            return Y(self)
        elif char == self.T:
            return T(self)
        
################################################################################
    
    def makeOperator(self, char):
        if char == self.PLUS:
            return Add(self)
        elif char == self.MINUS:
            return Minus(self)
        elif char == self.MULTIPLY:
            return Multiply(self)
        elif char == self.DIVIDE:
            return Divide(self)
        elif char == self.MODULO:
            return Modulo(self)
        elif char == self.POWER:
            return Power(self)
        
################################################################################
    
    def parseEquation(self, string):
        pos = 0
        v1 = None
        v2 = None
        operation = NullOperation(self)
        while pos < len(string):
            char = string[pos]
            variable = None
            
            if char in self.OPERATIONS:
                operation = self.makeOperator(char)
                pos += 1
            elif char == self.OPEN_BRACKET:
                substr = self.getBracketContents(string[pos:len(string)])
                variable = self.parseEquation(substr)
                pos += len(substr) + 2
            elif string[pos : pos + 3] == self.SIN:
                variable = Sin(self)
                arg = self.getBracketContents(string[pos + 3 : len(string)])
                variable.setVar1(self.parseEquation(arg))
                pos += 3 + len(arg) + 2
            elif string[pos : pos + 3] == self.COS:
                variable = Cos(self)
                arg = self.getBracketContents(string[pos + 3 : len(string)])
                variable.setVar1(self.parseEquation(arg))
                pos += 3 + len(arg) + 2
            elif string[pos : pos + 3] == self.TAN:
                variable = Tan(self)
                arg = self.getBracketContents(string[pos + 3 : len(string)])
                variable.setVar1(self.parseEquation(arg))
                pos += 3 + len(arg) + 2
            elif string[pos : pos + 3] == self.EXP:
                variable = Exp(self)
                arg = self.getBracketContents(string[pos + 3 : len(string)])
                variable.setVar1(self.parseEquation(arg))
                pos += 3 + len(arg) + 2
            elif string[pos : pos + 3] == self.LOG:
                variable = Log(self)
                arg = self.getBracketContents(string[pos + 3 : len(string)])
                variable.setVar1(self.parseEquation(arg))
                pos += 3 + len(arg) + 2
            elif string[pos : pos + 3] == self.ABS:
                variable = Abs(self)
                arg = self.getBracketContents(string[pos + 3 : len(string)])
                variable.setVar1(self.parseEquation(arg))
                pos += 3 + len(arg) + 2
            elif string[pos : pos + 4] == self.SQRT:
                variable = Sqrt(self)
                arg = self.getBracketContents(string[pos + 4 : len(string)])
                variable.setVar1(self.parseEquation(arg))
                pos += 4 + len(arg) + 2
            elif char in self.NUMERALS:
                numStr = self.parseNumber(string[pos : len(string)])
                variable = Constant(self)
                variable.setVar1(float(numStr))
                pos += len(numStr)
            elif char in self.VARIABLES:
                variable = self.makeVariable(char)
                pos += 1
            elif char == self.SPACE:
                pos += 1
            else:
                raise RuntimeError("Unrecognised character: \"%s\" in equation:\n\"%s\"" %(char, string))
            
            if v1 == None and variable != None:
                v1 = variable
            elif v2 == None and variable != None:
                v2 = variable
        
        operation.setVar1(v1)
        operation.setVar2(v2)
        
        return operation
        
################################################################################
    
    def parseNumber(self, string):
        copy = ""
        for pos in xrange(len(string)):
            char = string[pos]
            if char in self.NUMERALS:
                copy += char
            else:
                break
        
        return copy
        
################################################################################
            
    def getBracketContents(self, string):
        contents = string[0] # Should always be "("
        bracketCount = 1
        
        pos = 1
        while bracketCount > 0:
            char = string[pos]
            if char == self.OPEN_BRACKET:
                bracketCount += 1
            elif char == self.CLOSE_BRACKET:
                bracketCount -= 1
            contents += char
            pos += 1
        
        return contents[1 : len(contents) - 1]
        
################################################################################
################################################################################
        
        
        