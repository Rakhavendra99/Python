first = 78
second = 73.5
total = first + second
type(total)
#output <class'float'>
print(total)
#output 151.5
average = total/2
print(average)
#output 75.75
print(int(average))
#output 75

shirt_price = 659
pants_price = 345
total = shirt_price + pants_price
print(total)
#output 1004
print("your bill is :" +total)
#output Type error: can only cancatenate str(not "int") to str
print("your bill is ", total)
#output your bill is 1004
print("your bill is "+str(total))
#output your bill is 1004


a=1
bool(a)
#output True

a= 0
bool(a)
#output False

u= ' '
bool(u)
#output False

v=' '
bool(v)
#output True

value = 50
complex(value)
#output (50+0j)
complex(5,6)
#output (5+6J)

complex("5",6)
#output Type error: complex() can't take second arg if first is a string
