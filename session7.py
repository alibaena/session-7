#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:48:57 2020

@author: pepe
"""

#%%

try:
    with open("hello.txt") as file:
        for line in file:
            print(line)
except:
    print("the file doesn't exist, try other file")
    
#%% 

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("try another number")
    except TypeError:
        print("please, make sure that both params are numbers")
        

print (divide(3, 4))
print (divide(3, 0))
print (divide("asdf", "qewr"))

#%%

name = input("Please, tell me your name: ")

if name == "":
    raise ValueError("name shouldn't be empty")
    
print ("contact added correctly")

#%%

def validate_email(email):
    if type(email) != str:
        raise TypeError("email should be a string")
        
    if "." not in email or "@" not in email:
        raise ValueError("email is incorrect")
    
    return email

print(validate_email("jgarciah@faculty.ie.edu"))
#validate_email("jgarciah")
validate_email(234234)
        










