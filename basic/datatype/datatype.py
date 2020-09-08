## 1) int
## 2) Float
## 3) complex
## 4) boolean
## 5) string
##python not support in character datatype

## 1) int 
value = 0b1111	#binary to decimal value
print(value)
#output 15

value1 = 0o113545	#octal to decimal value
print(value1)
#output 4837

karthi = 0x123abc	#hexa to decimal value
karthi
#output 1194684

print(bin(120))	#decimal to binary
#output 0b1111000

print(oct(10))	#decimal to octal
#output 0o12

print(hex(100))	#decimal to hexa
#output 0o64


## 2) Float
No = 0x123.11
#output syntax Error: invalid syntax	#float value default to set the decimal value not a binary, octal, hexa value

No = 5.6e3	# float to support the exponential value
No
#output 5600.0

## 3) Complex
5+3j
type(_)	#stored last printed value
#output <class'complex'>

value =5+6j
print(value.real)	#only show the real value
#output 5.0
print(value.imag)	#only show the image value
#output 6.0

1+3d
#output syntax Error: invalid syntax	#complex datatype only support for 'j' keyword olnly not a other 'keywords'


## 4) Boolean
#only True or False value 
mark1 = 95
mark2 = 80
print(mark1 < mark2)	#lessthen fuction
#output False

print(mark1 > mark2)	#greaterthan fuction
#output True

print(mark1 == mark2)		#comparition operation
#output False


## 5) String
name = 'rk'	#string value
name
#output 'rk'

doorno = 120/2	#divisition operation is to be performed but it is not a real value
doorno
#output 60.0

doorno = '120/2'	#it is a correct value in doorno
doorno
#output '120/2'

doorno = 120/2B	#string function is not to be used in any special character
#output syntax Error:invallid system
