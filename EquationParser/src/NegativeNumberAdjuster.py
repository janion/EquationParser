'''
Created on 8 May 2017

@author: Janion
'''

class NegativeNumberAdjuster(object):
    
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
    ZERO = "0"
    
    def adjust(self, fnString):
        fnString = fnString.replace(self.SPACE, "")
        while self.MINUS in fnString:
            for x in range(len(fnString)):
                if fnString[x] == self.MINUS:
                    if (x == 0 or fnString[x - 1] in self.OPERATIONS or fnString[x - 1] == self.OPEN_BRACKET or fnString[x - 1] == self.PLACE_HOLDER or x == 0):
                        followingOperand = self.findFollowingOperand(fnString, x + 1)
                        fnString = (fnString[ : x]
                                    + self.OPEN_BRACKET
                                    + self.ZERO
                                    + self.PLACE_HOLDER
                                    + followingOperand
                                    + self.CLOSE_BRACKET
                                    + fnString[x + 1 + len(followingOperand) : ]
                                    )
                        break
                    else:fnString = (fnString[ : x]
                                    + self.PLACE_HOLDER
                                    + fnString[x + 1 : ]
                                    )
                
        return fnString.replace(self.PLACE_HOLDER, self.MINUS)
    
################################################################################
    
    def findFollowingOperand(self, string, pos):
        bracketCount = 0
        for x in range(pos, len(string)):
            char = string[x]
            if char == self.OPEN_BRACKET:
                bracketCount += 1
            elif char == self.CLOSE_BRACKET:
                bracketCount -= 1
            if char in self.OPERATIONS and bracketCount == 0:
                return string[pos : x]
        
        return string[pos : ]
        
    
            