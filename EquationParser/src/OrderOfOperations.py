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
        copy = fnString.replace(self.SPACE, "")
        
        # Invoke order of operations
        copy = self.prioritiseOperationRightToLeft(copy, self.POWER)
        copy = self.prioritiseOperationsLeftToRight(copy, self.MULTIPLY, self.DIVIDE)
        copy = self.prioritiseOperationsLeftToRight(copy, self.PLUS, self.MINUS)
        
        return copy
                
################################################################################
                
    def prioritiseOperationRightToLeft(self, string, operationChar):
        while operationChar in string and self.needsMoreBracketsForOperation(string, [operationChar], [self.PLACE_HOLDER1]):
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
        while (operationChar1 in string or operationChar2 in string)\
                and self.needsMoreBracketsForOperation(string, [operationChar1, operationChar2], [self.PLACE_HOLDER1, self.PLACE_HOLDER2]):
            for x in range(len(string)):
                char = string[x]
                if char == operationChar1:
                    string = self.bracketiseString(string, x, self.PLACE_HOLDER1)
                    break
                elif char == operationChar2:
                    string = self.bracketiseString(string, x, self.PLACE_HOLDER2)
                    break
                
        return string.replace(self.PLACE_HOLDER1, operationChar1).replace(self.PLACE_HOLDER2, operationChar2)
                
################################################################################
                
    def bracketiseString(self, string, pos, placeHolderChar):
        start = self.getContainingBracketStart(string, pos - 1)
        end = self.getContainingBracketEnd(string, pos + 1)

        firstOperand = string[start : pos]
        secondOperand = string[pos + 1 : end]

        if (string[start] != self.OPEN_BRACKET or (end < len(string) and string[end] != self.CLOSE_BRACKET))\
                and not (start == 0 and end == len(string)):
            firstOperand = self.OPEN_BRACKET + firstOperand
            secondOperand = secondOperand + self.CLOSE_BRACKET
                
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
            elif bracketCount == 1:
                return x
        
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
            elif bracketCount == -1:
                return x
        
        return len(string)

################################################################################

    def needsMoreBracketsForOperation(self, string, operations, placeHolders):
        bracketCount = 0
        openBrackerCount = string.count(self.OPEN_BRACKET) + 1
        hasSeenAnyOperation = [False for x in range(openBrackerCount)]
        hasSeenTheseOperations = [False for x in range(openBrackerCount)]

        for char in string:
            if char == self.OPEN_BRACKET:
                bracketCount += 1
            elif char == self.CLOSE_BRACKET:
                hasSeenAnyOperation[bracketCount] = False
                hasSeenTheseOperations[bracketCount] = False
                bracketCount -= 1
            elif char in operations or char in placeHolders:
                if hasSeenTheseOperations[bracketCount]:
                    return True
                hasSeenTheseOperations[bracketCount] = True
            elif char in self.OPERATIONS:
                if hasSeenAnyOperation[bracketCount]:
                    return True
                hasSeenAnyOperation[bracketCount] = True

            if hasSeenTheseOperations[bracketCount] and hasSeenAnyOperation[bracketCount]:
                return True

        return False
