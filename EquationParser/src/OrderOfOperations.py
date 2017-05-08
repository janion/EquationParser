'''
Created on 8 May 2017

@author: Janion
'''

class OrderOfOperations(object):
    
    OPEN_BRACKET = "("
    CLOSE_BRACKET = ")"
    
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULO = "%"
    POWER = "^"
    OPERATIONS = [PLUS, MINUS, MULTIPLY, DIVIDE, POWER]
    
    PLACE_HOLDER = "|"
    SPACE = " "

    def addBrackets(self, fnString):
        copy = self.OPEN_BRACKET + fnString.replace(self.SPACE, "") + self.CLOSE_BRACKET
        
        # Invoke order of operations
        copy = self.prioritiseOperation(copy, self.POWER)
        copy = self.prioritiseOperation(copy, self.MULTIPLY)
        copy = self.prioritiseOperation(copy, self.DIVIDE)
        copy = self.prioritiseOperation(copy, self.PLUS)
        copy = self.prioritiseOperation(copy, self.MINUS)
        
        return copy[1 : -1]
                
################################################################################
                
    def prioritiseOperation(self, string, operationChar):
        
        while operationChar in string:
            for x in range(len(string)):
                if string[x] == operationChar:
                    start = self.getContainingBracketStart(string, x)
                    end = self.getContainingBracketEnd(string, x)
                    
                    firstOperand = self.bracketiseOperand(string[start : x])
                    secondOperand = self.bracketiseOperand(string[x + 1 : end])
                            
                    string = (string[ : start]
                              + firstOperand
                              + self.PLACE_HOLDER
                              + secondOperand
                              + string[end : ]
                              )
                    break
                
        return string.replace(self.PLACE_HOLDER, operationChar)
                
################################################################################
                
    def bracketiseOperand(self, operand):
        if not (operand.startswith(self.OPEN_BRACKET) and operand.endswith(self.CLOSE_BRACKET)):
            for operation in self.OPERATIONS:
                if operation in operand:
                    operand = self.OPEN_BRACKET + operand + self.CLOSE_BRACKET
                    break
        return operand
                
################################################################################
                
    def getContainingBracketStart(self, string, pos):
        bracketCount = 0
        for x in range(pos, -1, -1):
            if string[x] == self.OPEN_BRACKET:
                if bracketCount == 0:
                    start = x + 1
                    break
                bracketCount += 1
            elif string[x] == self.CLOSE_BRACKET:
                bracketCount -= 1
        
        return start
                
################################################################################
                
    def getContainingBracketEnd(self, string, pos):
        bracketCount = 0
        for x in range(pos, len(string)):
            if string[x] == self.OPEN_BRACKET:
                bracketCount += 1
            elif string[x] == self.CLOSE_BRACKET:
                if bracketCount == 0:
                    end = x
                    break
                bracketCount -= 1
        
        return end

fn = "25 * (x + 1) ^ y * (sin(t) - 4)"
o = OrderOfOperations()
print fn
print o.addBrackets(fn)
    