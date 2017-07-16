i=0

numbers=[]
print ("AP=>a+b(n+1)=answer")
n= int(raw_input("\n>>Enter n.")) +1
b= int(raw_input("\n>>Enter b."))
if b==0:
	int(raw_input("\n>>b cannot be 0, reenter b."))

#for loop
for i in range(0,n):
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i+b
	print "Numbers now:", numbers
	print "At the bottom i is %d" %i

#While loop
'''
while i < n:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i+b
	print "Numbers now:", numbers
	print "At the bottom i is %d" %i
'''
print "The numbers: "

for num in numbers:
	print num