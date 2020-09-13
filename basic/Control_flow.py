## Control flow statement:
#program 1
mark1 = 80
mark2 = 70
if mark1 == mark2:
    print("same")
elif mark1 > mark2:
    print("mark1 is greater")
else:
    print("mark2 is greater")
#output mark1 is greater

# if statement should end with : True
# if needs elif part compulsourily : False
# if needs else part compulsourily : False
# elif needs if part compulsourily : True
# else needs if part compulsourily : True

#program 2
mark1 = int(input("enter mark1"))
mark2 = int (input("enter mark2"))
if mark1 == mark2:
    print("same")
elif mark1 > mark2:
    print("mark1 is greater")
else:
    print("mark2 is greater")
#output Enter mark1 90
#	Enter mark2 89
#	mark1 is greater
