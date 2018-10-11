#!/usr/bin/env python3

# print a string right justified like rjust(70)
def right_justify(s):
    l = len(s)
    r = 70 - l
    print (" "*r + s)

right_justify("asakhkashksahli")

def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")

do_twice(print_spam)

def do_twice2(f,v):
    f(v)
    f(v)

def do_four(f,v):
    do_twice2(f,v)
    do_twice2(f,v)

def print_spam2(val):
    print(val)

def print_twice(val):
    print(val)
    print(val)

do_twice2(print_spam2,"ala")

do_twice2(print_twice,"spam")

do_four(print_spam2,"ala")

def griddy():
    print("+" + 4*"-"+"+"+ 4*"-"+ "+")
    print("|" + 4*" "+"|"+ 4*" "+ "|")
    print("|" + 4*" "+"|"+ 4*" "+ "|")
    print("|" + 4*" "+"|"+ 4*" "+ "|")
    print("|" + 4*" "+"|"+ 4*" "+ "|")
    print("+" + 4*"-"+"+"+ 4*"-"+ "+")
    print("|" + 4*" "+"|"+ 4*" "+ "|")
    print("|" + 4*" "+"|"+ 4*" "+ "|")
    print("|" + 4*" "+"|"+ 4*" "+ "|")
    print("|" + 4*" "+"|"+ 4*" "+ "|")
    print("+" + 4*"-"+"+"+ 4*"-"+ "+")

griddy()
