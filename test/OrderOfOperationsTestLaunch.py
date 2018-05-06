'''
Created on 8 May 2017

@author: Janion
'''
from eqn.OrderOfOperations import OrderOfOperations

failed = False


def assertEquals(expected, actual):
    global failed
    if expected != actual:
        failed = True
        print(expected + " != " + actual)

if __name__ == '__main__':
    o = OrderOfOperations()

    assertEquals("251",                                 o.addBrackets("251"))
    assertEquals("25+1",                                o.addBrackets("25 + 1"))
    assertEquals("(25/((7+1)^9))*(sin(t)-4)",           o.addBrackets("25 / (7 + 1) ^ 9 * (sin(t) - 4)"))
    assertEquals("((7*9)/7)*9",                         o.addBrackets("7 * 9 / 7 * 9"))
    assertEquals("((7/9)*7)/9",                         o.addBrackets("7 / 9 * 7 / 9"))
    assertEquals("2^(5^(6^4))",                         o.addBrackets("2 ^ 5 ^ 6 ^ 4"))
    assertEquals("(2^(5^(6^4)))+3",                     o.addBrackets("2 ^ 5 ^ 6 ^ 4 + 3"))
    assertEquals("(2+3)^(3*5)",                         o.addBrackets("(2 + 3) ^ (3 * 5)"))
    assertEquals("(((2+5)+6)+4)+3",                     o.addBrackets("2 + 5 + 6 + 4 + 3"))
    assertEquals("sin((2+5)+6)",                        o.addBrackets("sin(2 + 5 + 6)"))
    assertEquals("sin((2+5)+6)+4",                      o.addBrackets("sin(2 + 5 + 6) + 4"))
    assertEquals("(sin((2+5)+6)+4)+3",                  o.addBrackets("sin(2 + 5 + 6) + 4 + 3"))
    assertEquals("127*(sin((t+(x/5))+(6.243/1.5))+1)",  o.addBrackets("127 * (sin(t + (x / 5) + (6.243 / 1.5)) + 1)"))
    assertEquals("sin((t+(x/5))+(6.243/1.5))",          o.addBrackets("sin(t + (x / 5) + (6.243 / 1.5))"))
    assertEquals("sin(1^(2^3))",                        o.addBrackets("sin(1 ^ 2 ^ 3)"))
    assertEquals("sin(1^((2+1)^3))",                    o.addBrackets("sin(1 ^ (2 + 1) ^ 3)"))
    assertEquals("sin(1^((2+1)^(3*2)))",                o.addBrackets("sin(1 ^ (2 + 1) ^ (3 * 2))"))
    assertEquals("127*(sin(t^((x/5)^(6.243/1.5)))^1)",  o.addBrackets("127 * (sin(t ^ (x / 5) ^ (6.243 / 1.5)) ^ 1)"))
    assertEquals("(1+1)^((2+2)^(3+3))",                 o.addBrackets("(1+1) ^ (2+2) ^ (3+3)"))
    assertEquals("((1+1)^((2+2)^(3+3)))",               o.addBrackets("((1+1) ^ (2+2) ^ (3+3))"))
    assertEquals("2+(sin(x)^y)",                        o.addBrackets("2 + (sin(x) ^ y)"))

    assertEquals("sin(((1*(2+3))*2)*(2^1))+sin(((1*(2+3))*2)*(2^1))",
                 o.addBrackets("sin(1*(2+3)*2*2^1) + sin(1*(2+3)*2*2^1)"))

    if failed:
        print("\nFAIL")
