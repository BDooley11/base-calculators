def funct (a,b):
	number = a
	list = []
	while number >0:
		quotient = number//b
		remainder = number % b
		list += [remainder]
		number = quotient
		if list[-1] >9:
			if list[-1] ==10:
				list[-1] = "A"
			elif list[-1] ==11:
				list[-1] = "B"
			elif list[-1] ==12:
				list[-1] = "C"
			elif list[-1] ==13:
				list[-1] = "D"
			elif list[-1] ==14:
				list[-1] = "E"
			elif list[-1] ==15:
				list[-1] = "F"
	list.reverse()
	print(initialinput,"in base of 10 is ",end="")
	for x in list:
		print(x,end="")
	print(" in base of",base)
	return True
	

initialinput = int(input("Please enter a number:"))
base = int(input("Please enter the base(max 16):"))

if initialinput>0 and base >0:
	result = funct(initialinput,base)
else:
	print("number or base entered less than or equal to zero")


