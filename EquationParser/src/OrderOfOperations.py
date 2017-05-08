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
#         copy = fnString.replace(self.SPACE, "")
        
        # Invoke order of operations
        copy = self.prioritiseOperationRightToLeft(copy, self.POWER)
        copy = self.prioritiseOperationsLeftToRight(copy, self.MULTIPLY, self.DIVIDE)
        copy = self.prioritiseOperationsLeftToRight(copy, self.PLUS, self.MINUS)
        
        return copy[1 : -1]
#         return copy
                
################################################################################
                
    def prioritiseOperationRightToLeft(self, string, operationChar):
        while operationChar in string and self.needsMoreBrackets(string):
            for x in range(len(string) - 1, -1, -1):
                if string[x] == operationChar:
                    start = self.getContainingBracketStart(string, x-1)
                    end = self.getContainingBracketEnd(string, x+1)
                    
                    firstOperand = self.OPEN_BRACKET + string[start : x]
                    secondOperand = string[x + 1 : end] + self.CLOSE_BRACKET
                            
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
        while (operationChar1 in string or operationChar2 in string) and self.needsMoreBrackets(string):
            for x in range(len(string)):
                if string[x] == operationChar1:
                    string = self.bracketiseString(string, x, self.PLACE_HOLDER1)
                    break
                elif string[x] == operationChar2:
                    string = self.bracketiseString(string, x, self.PLACE_HOLDER2)
                    break
                
        return string.replace(self.PLACE_HOLDER1, operationChar1).replace(self.PLACE_HOLDER2, operationChar2)
                
################################################################################
                
    def bracketiseString(self, string, pos, placeHolderChar):
        start = self.getContainingBracketStart(string, pos - 1)
        end = self.getContainingBracketEnd(string, pos + 1)
        
        firstOperand = self.OPEN_BRACKET + string[start : pos]
        secondOperand = string[pos + 1 : end] + self.CLOSE_BRACKET
                
        return (string[ : start]
                + firstOperand
                + placeHolderChar
                + secondOperand
                + string[end : ]
                )
                
################################################################################
                
    def getContainingBracketStart(self, string, pos):
        bracketCount = 0
        for x in range(pos, -1, -1):
            char = string[x]
            if char == self.OPEN_BRACKET:
                bracketCount += 1
            elif char == self.CLOSE_BRACKET:
                bracketCount -= 1
            if char in self.OPERATIONS and bracketCount == 0:
                return x + 1
        
        return 0
                
################################################################################
                
    def getContainingBracketEnd(self, string, pos):
        bracketCount = 0
        for x in range(pos, len(string)):
            char = string[x]
            if char == self.OPEN_BRACKET:
                bracketCount += 1
            elif char == self.CLOSE_BRACKET:
                bracketCount -= 1
            if char in self.OPERATIONS and bracketCount == 0:
                return x
        
        return len(string) - 1
                
################################################################################
                
    def needsMoreBrackets(self, string):
        bracketCount = 0
        hasSeenOperation = False
        for char in string:
            if char == self.OPEN_BRACKET:
                bracketCount += 1
            elif char == self.CLOSE_BRACKET:
                bracketCount -= 1
            elif char in self.OPERATIONS:
                if hasSeenOperation and bracketCount == 1:
                        return True
                hasSeenOperation = True
        
        return False
                
################################################################################
                
#     def needsMoreBrackets(self, string):
#         hasSeenOperation = False
#         for char in string:
#             if char in self.OPERATIONS:
#                 if hasSeenOperation:
#                     return True
#                 hasSeenOperation = True
#             elif char == self.OPEN_BRACKET or char == self.CLOSE_BRACKET:
#                 hasSeenOperation = False
#         
#         return False
                
################################################################################
################################################################################

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
    