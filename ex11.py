
#Entering age
print "How old are you?, in years\n",
age = int(raw_input())

if age > 90:
	print "It is unlikely you are so old but still using my program, reenter your age\n"
	age2 = int(raw_input())
	
	if age2 > 90 or age2 == age:
		print "If you insist..."

while age < 5:
	print "You entered an age less than 5, please reenter your age.\n"
	age = int(raw_input())
	
#Entering Height
print "\n\n\n\nHow tall are you, in cm?\n",
height = int(raw_input())

while height > 250:
	print "You entered an height more than 250, please reenter your height.\n"
	height = int(raw_input())
	
while height < 10:
	print "You entered a number less than 10. Could you have accidently used feets as your form of measurement? If yes, enter '1'. If no, reenter your height in metric CM."
	a = int(raw_input())
	
	if a == 1:
		heightcm = height * 30.48
		print "Your height of %r feet has been converted and entered into the system as a height of %rcm" %(height, heightcm)
		height = heightcm
	
	else:
		Height = a

#Entering Weight
print "\n\n\nHow much do you weigh, in Kgs?\n",
weight = int(raw_input())

if weight > 280:
	print "You entered a number greater than 280. Could you have accidently used pounds as your form of measurement? If yes, enter '1'. If no, reenter your weight in metric kg."
	a = int(raw_input())
	
	if a == 1:
		weightkg = weight * 0.453
		print "Your weight of %r pounds has been converted and entered into the system as a weight of %rkg" %(weight, weightkg)
		weight = weightkg
	
	else:
		weight = a

#Final output

print "\n\n\nSUMMARY:\n Age = %r Years Old\n Height = %rcm\n Weight = %rkg\n------Report Complete------" % (age, height, weight)
"""
#Comfirmation

answer = raw_input("\n\n\n Comfirmation:\n Correct=Y Wrong=F")
if answer in ('y', 'n'):
	break
	print 'Invalid input.'
if answer == 'y':
        print "Your input has been finalised, Thank You."
else:
	print 'Goodbye'
	break"
"""