#define funct (a,b):
#	var number equals a
#	create list = []
#	while number greater than 0 do
#		var quotient equals number divide by b
#		var remainder equals number modulo b
#		list append [remainder]
#		number equals quotient
#		if list[index -1] greater than 9 then
#			if list[index -1] equals 10 then
#				list[index -1] equals "A"
#			else if list[index -1] equals 11 then
#				list[index -1] equals "B"
#			else if list[index -1] equals 12 then
#				list[index -1] equals "C"
#			else iflist[index -1] equals 13 then
#				list[index -1] equals "D"
#			else if list[index -1] equals 14 then
#				list[index -1] equals "E"
#			else if list[index -1] equals 15 then
#				list[index -1] equals "F"
#	list.reverse() reverse list order
#	print(initialinput,"in base of 10 is ",end="")
#	for x in list:
#		print(x,end="")
#	print(" in base of",base)
#	return True
#	
#
#ask user to enter var initialinput 
#ask user to enter var base 
#
#if initialinput>0 and base >0:
#	result = call funct(initialinput,base)
#else:
#	print("number or base entered less than or equal to zero")

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


