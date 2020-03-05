""" EXCERECISE 2 faulty calculator 
45*3=555,56+9=77 56/6=4
Design the calculator which will correctly solve all the problem except
The following ones
your program should take operator and two number as input from the user
and than enter the result 
"""
print("enter operator ")
o=input()
if(o=="*"):
    print("Enter two value ")
    x=int(input())
    y=int(input())
    if(x==45 and y==3):
        print("value is 555")
    else:
        print("result is",x*y)
elif(o=="+"):
    print("Enter two value ")
    x=int(input())
    y=int(input())
    if(x==56 and y==9):
        print("value is 77")
    else:
        print("result is",x+y)
elif(o=="/"):
    print("Enter two value ")
    x=int(input())
    y=int(input())
    if(x==56 and y==6):
        print("value is 4")
    else:
        print("result is",x/y)
else:
    print("you enter Right operator this operator is not available our calculator")