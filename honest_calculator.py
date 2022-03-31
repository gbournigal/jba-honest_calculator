# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:45:28 2022

@author: georg
"""

# write your code here
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

last_msgs = {
    0: msg_10,
    1: msg_11,
    2: msg_12
    }
memory = 0 

def main(memory): 
    print(msg_0)
    user_inp = str(input())
    x, oper, y = user_inp.split(" ")
    if x == 'M':
        x = memory
    else:
        x = float(x)
    
    if y == 'M':
        y = memory
    else:
        y = float(y)
        
    return x, oper, y
    
def calculation(x, oper, y):
    if oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    elif oper == '*':
        return x * y
    else:
        return x / y
        
def is_one_digit(v):
    if abs(v) < 10 and v - int(v) == 0:
        return True
    else:
        return False
    

def check_lazy(x, oper, y):
    msg = ''
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1 or y == 1) and oper == '*':
        msg = msg + msg_7
    if (x == 0 or y == 0) and (oper in ['+', '-', '*']):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
    print(msg) 
        
    
def recursive(memory):
    try:
        x, oper, y = main(memory)
    except ValueError:
        print(msg_1)
        recursive(memory)
    else:
        if oper in ['+','-','*','/']:
            check_lazy(x, oper, y)
            if oper == '/' and y == 0:
                print(msg_3)
                recursive(memory)
            else:
                result = calculation(x, oper, y)
                print(result)
                print(msg_4)
                ans = str(input())
                msg_idx = 0
                if ans == 'y':
                    if is_one_digit(result):
                        while msg_idx < 3:
                            print(last_msgs[msg_idx])
                            ans_ms = str(input())
                            if ans_ms == 'n':
                                msg_idx += 10
                            else:
                                msg_idx += 1
                        if msg_idx == 3:
                            memory = result
                    else:
                        memory = result
                else:
                    pass
                print(msg_5)
                ans = str(input())   
                if ans == 'y':
                    recursive(memory)
                else:
                    pass            
        else:
            print(msg_2)
            recursive(memory)

recursive(memory)