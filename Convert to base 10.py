#define function(a,b):
#	list equals  []
#	for x in a:
#		append x to list
#
#	if list[index 0] equals "a" or list[index 0] equals "A" then
#		list[index 0] equals 10
#	else if list[index 0] equals "b" or list[index 0] equals "B" then
#		list[index 0] equals 11
#	else if list[index 0] equals "c" or list[index 0] equals "C" then
#		list[index 0] equals 12
#	else if list[index 0] equals "d" or list[index 0] equals "D" then
#		list[index 0] equals 13
#	else if list[index 0] equals "e" or list[index 0] equals "E" then
#		list[index 0] equals 14
#	else if list[index 0] equals "f" or list[index 0] equals "F" then
#		list[index 0] equals 15
#
#	var length equals length(list)
#
#	var number equals 0
#
#	for i in range(length(list)):
#		number equals number plus (int(list[index i]) multiply(b power(length-1)))
#		length plus 1
#
#	return number
#
#user input var initialinput
#user input var base
#
#if initialinput not blank and base greater than zero then
#	var result equals call funct(initialinput,base)
#	print(initialinput,"in base",base,"is",result,"in base of 10")
#else:
#	print("Number or base entered is less than zero")


def funct(a,b):
	list =  []
	for x in a:
		list += x

	if list[0] == "a" or list[0] == "A" :
		list[0] = 10
	elif list[0] == "b" or list[0] == "B" :
		list[0] = 11
	elif list[0] == "c" or list[0] == "C" :
		list[0] = 12
	elif list[0] == "d" or list[0] == "D" :
		list[0] = 13
	elif list[0] == "e" or list[0] == "E" :
		list[0] = 14
	elif list[0] == "f" or list[0] == "F" :
		list[0] = 15

	length = len(list)

	number = 0

	for i in range(len(list)):
		number = number+(int(list[i])*(b**(length-1)))
		length -=1

	return number

initialinput = input("Please enter a number to be converted to base 10:")
base = int(input("enter base of number entered(max16)"))

if initialinput !="" and base >0:
	result = funct(initialinput,base)
	print(initialinput,"in base",base,"is",result,"in base of 10")
else:
	print("Number or base entered is less than zero")
