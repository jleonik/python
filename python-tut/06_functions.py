# Use "def" to define a new function
def example():
    print('Basic function')
    z = 2+2
    print(z)

example()

def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is',num1)
    print('num2 is',num2)
    print('num1 + num2 is',answer)

simple_addition(3,5)

def simple(num1,num2):
    pass

def simple2(num1,num2=5):
    print(num1,num2)

simple2(2) #Since one of the params has a default value, we need to provide only one param instead of two

def basic_window(width,height,font='TNR',bgc='w',scrollbar=True):
    print(width,height,font,bgc)

basic_window(480,240,bgc='b') #Font param is not being set so we have specifiy explicitly which param are we setting