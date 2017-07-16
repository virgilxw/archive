print "Let's practice everything"
print 'You\'d need to know\'bout escapes with \\ that do \n newlines and \t tabs.'

poem="""
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires anj explanation
\n\t\twhere there is none.
"""

print "----------"
print poem
print "----------"

five= 10 - 2 + 3 -6
print "This should be five :%s" %five

def secret_formula (started):
#number of jelly beans
	jelly_beans= started*500
#number of jelly beans when divided 1000/jar
	jars= jelly_beans/1000
#100 jars/crate
	crates= jars/100
	hello=1000
	return jelly_beans, jars, crates, hello
	
	
start_point = 10000
beans, jars, crates, hello= secret_formula(start_point)

print "With a starting point of : %d" %start_point
print "We'd have %d beans, %d jars and % crates." % (beans, jars, crates)

start_point = start_point/10

print "We can also do that this way:"
print "We'd have %d beans, %d jars and %d crates. %d" %secret_formula(start_point)