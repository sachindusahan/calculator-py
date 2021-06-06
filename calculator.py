from os import system

i = 1 
while i < 10:
	calculator = input('Open Calculator > open  Exit > exit :')
	if calculator == 'open':
		try:
			num_1 = float(input("FIRST Number >: "))
			Op = input("Condition >: ")
			num_2 = float(input("SECOND Number >: "))

			def Condition(number_1,number_2):
				if Op =='+':
					print ((int(number_1)) + (int(number_2)))
				elif Op == "-":
					print ((int(number_1)) - (int(number_2)))
				elif Op == "×":
					print (int(number_1) * int(number_2))
				elif Op == "÷":
					print (int(number_1) / int(number_2))
			Condition(num_1,num_2)
		except ValueError as err:
			print (err)
	elif calculator == 'exit':
		break
		system('exit()')
	else:
		system('clear')

	i +=1
