list = []

while(True):

	c = raw_input("Enter a char : ")
	if c != "/":
		list.append(c)

	elif len(list) > 0:
		list.pop(len(list) - 1)

	print(list)