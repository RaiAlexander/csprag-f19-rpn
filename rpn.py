#!/usr/bin/env python3

import operator
import readline
from termcolor import colored


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '<': operator.lt,
    '>': operator.gt,
    '==': operator.eq,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            num1color = 'green'
            num2color = 'green'
            arg2 = stack.pop()
            arg1 = stack.pop()
            if arg1 < 0:
                num1color = 'red'
            else:
                num1color = 'cyan'
            if arg2 < 0:
                num2color = 'red'
            else:
                num2color = 'blue'
            # Added to show coverage difference
            # if arg1 == 2:
            #     print("I am here")
            # if arg2 == 2:
            #     print("I am now here")
            result = function(arg1, arg2)
            stack.append(result)
            print(colored(arg1, num1color, attrs=['bold']), colored(token, 'yellow'), colored(arg2, num2color, attrs=['bold']), 
                colored('=', 'white'), colored(result, 'magenta', attrs=['underline']))
        print(stack)
        
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
