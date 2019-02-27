
def tokenize(input_string):  
    outputlist = []
    x = ''
    for char in input_string:
        if char == ' ' and x != '' and x != ' ':
            outputlist.append(x)
            x = ''
            
        elif x == ' ':
            x = ''
            
        else:
            x = x + char
    
    if x != ' ' and x != '':
        outputlist.append(x)
    
    return outputlist


def number_check(x): 
    digits = ['0','1','2','3','4','5','6','7','8','9',]
    number = 0
    dec = 0
    for n in x:
        if n in digits:
            number = number
        
        elif n == '.':
            dec = dec + 1
            
        else:
            number = number + 1
    
    if number == 0  and dec <= 1:
        check = True
    else:
        check = False
    
    return check
    

def evaluate(expression, stack, binary_operations, unary_operations):
    
    for i in tokenize(expression):
        
        if number_check(i) == True:
            stack.append(float(i))
        
        if i in unary_operations:
            n1 = stack.pop()
            result = unary_operations[i](n1)
            stack.append(result)
        
        if i in binary_operations:
            n1 = stack.pop()
            n2 = stack.pop()
            result = binary_operations[i](n2,n1)
            stack.append(result)
            




"""
Created on Mon Jan 21 11:02:36 2019

@author: skylargordon 
"""
