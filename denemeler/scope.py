# Built-in Scope 
from math import pi 
# pi = 'Not defined in global pi'
def func_outer(): 
    # pi = 'Not defined in outer pi' 
    def inner(): 
        # pi = 'not defined in inner pi' 
        print(pi) 
    inner() 
func_outer() #pi in math



x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)



