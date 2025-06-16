
a = 10 
b = 5
c = a + b
print(a+b)

def add(a,b):
    print(a+b)
add(a,b)

def mul(a,b):
    print(a*b)

mul(a,b)

def sub(a,b):
    print(a-b)
sub(a,b)

def div(a,b):
    print(a/b)
div(a,b)

def mod(a,b):
    print(a%b)
mod(a,b)

def power(a,b):
    print(a**b)
power(a,b)

def floor(a,b):
    print(a//b)
floor(a,b)

def complexfun(a,b):
    print(a+b*b-a**b)
complexfun(a,b)

def square(a):
    print(a**2)
square(a)

def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a-1)
    
def gcd(a,b):
    while b:
        a,b = b, a % b
        return a