import math

def add (a,b):
    return a + b
    
def subtract (a,b):
    return a - b

def multiply (a,b):
    return a * b

def divide (a,b):
    return a / b

def square (a):
    return a * a

def log (a):
    return math.log(a)

def sin (a):
    return math.sin(math.radians(a))

def cos (a):
    return math.cos(math.radians(a))

def square_root (a):
    return math.sqrt(a)

def percentage (a,b):
    return ((divide(a,b)) * 100)