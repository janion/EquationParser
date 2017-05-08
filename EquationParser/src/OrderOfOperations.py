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
    
    PLACE_HOLDER1 = "|"
    PLACE_HOLDER2 = "&"
    SPACE = " "

    def addBrackets(self, fnString):
        copy = self.OPEN_BRACKET + fnString.replace(self.SPACE, "") + self.CLOSE_BRACKET
        
        # Invoke order of operations
        copy = self.prioritiseOperationRightToLeft(copy, self.POWER)
        copy = self.prioritiseOperationsLeftToRight(copy, self.MULTIPLY, self.DIVIDE)
        copy = self.prioritiseOperationsLeftToRight(copy, self.PLUS, self.MINUS)
        
        return copy[1 : -1]
                
################################################################################
                
    def prioritiseOperationRightToLeft(self, string, operationChar):
        while operationChar in string:
            for x in range(len(string)):
                if string[x] == operationChar:
                    start = self.getContainingBracketStart(string, x)
                    end = self.getContainingBracketEnd(string, x)
                    
                    firstOperand = self.bracketiseOperand(string[start : x])
                    secondOperand = self.bracketiseOperand(string[x + 1 : end])
                            
                    string = (string[ : start]
                              + firstOperand
                              + self.PLACE_HOLDER1
                              + secondOperand
                              + string[end : ]
                              )
                    break
                
        return string.replace(self.PLACE_HOLDER1, operationChar)
                
################################################################################
                
    def prioritiseOperationsLeftToRight(self, string, operationChar1, operationChar2):
        while operationChar1 in string or operationChar2 in string:
            for x in range(len(string) - 1, -1, -1):
#             for x in range(len(string)):
                if string[x] == operationChar1:
                    string = self.bracketiseOperation(string, x, operationChar1, self.PLACE_HOLDER1)
                    break
                elif string[x] == operationChar2:
                    string = self.bracketiseOperation(string, x, operationChar2, self.PLACE_HOLDER2)
                    break
                
        return string.replace(self.PLACE_HOLDER1, operationChar1).replace(self.PLACE_HOLDER2, operationChar2)
                
################################################################################
                
    def bracketiseOperation(self, string, pos, operationChar, placeHolderChar):
        start = self.getContainingBracketStart(string, pos)
        end = self.getContainingBracketEnd(string, pos)
#         end = self.getContainingBracketEnd(string, pos + 1, operationChar)
        
        firstOperand = self.bracketiseOperand(string[start : pos])
        secondOperand = self.bracketiseOperand(string[pos + 1 : end])
                
        return (string[ : start]
                + firstOperand
                + placeHolderChar
                + secondOperand
                + string[end : ]
                )
                
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
                
#     def getContainingBracketEnd(self, string, pos, operationChar):
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
#             elif string[x] == operationChar and bracketCount == 0:
#                 end = x
#                 break
        
        return end

fn = "25 / (x + 1) + y * (sin(t) - 4)"
o = OrderOfOperations()
print fn, " -> ", o.addBrackets(fn)

print ""

fn = "x * y / x * y"
o = OrderOfOperations()
print fn, " -> ", o.addBrackets(fn)

print ""

fn = "x / y * x / y"
o = OrderOfOperations()
print fn, " -> ", o.addBrackets(fn)

print ""

fn = "2 * 5 / 6 * 4"
o = OrderOfOperations()
print fn, " -> ", o.addBrackets(fn)

print ""

fn = "2 ^ 5 ^ 6 ^ 4"
o = OrderOfOperations()
print fn, " -> ", o.addBrackets(fn)
    