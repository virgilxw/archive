try:
	age = int(raw_input("Please enter your age: "))
except ValueError:
	print("Sorry, I didn't understand that.")