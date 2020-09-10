## 1) Upper
## 2) Lower
## 3) Slice
## 4) Step operator
## 5) len 
## 6) in

## 1) Upper case
name = "kannan"
name.upper()
#output 'KANNAN'

name = "KuMaR"
name.upper()
#output 'KUMAR'

## 2) Lower
name = "Rakhav"
name.lower()
#output 'rakhav'

name = "MADURAI"
name.lower()
#output 'madurai'

## 3) Slice operator
alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets[1])
#output a
print(alphabets[25])
#output z
print(alphabets[-1])
#output z
print(alphabets[-20])
#output g

print(alphabets[True])
#output b
print(alphabets[False])
#output a

print(alphabets[0:5])
#output 'abcde'
print(alphabets[4:12])
#output 'defghijklmno'

print(alphabets[-5:-1])
#output 'vwxy'
print(alphabets[5:])
#output 'fghijklmnopqrstuvwxyz'
print(alphabets[-1:])
#output 'z'

## 4) Step operator
print(alphabets[::2])
#output 'acegikmoqsuwy'
print(alphabets[::3])
#output 'adgjmpsvy'

## 5) len
name ="rakhavendra"
name[0]
#output 'r'
name[0].upper()
#output 'R'
name[1:]
#output 'akhavendra'
print(name[0].upper + name[1:])
#output Rakhavendra
name = "rakhavendra"
len(name)
#output '11'

word = "lub dub" * 4
print(word)
#output lub dub lub dub lub dub lub dub

## 6) in
word = "Engineering"
'g' in word
#output True
'u' in word
#out False
