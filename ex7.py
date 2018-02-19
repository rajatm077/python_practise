from sys import argv
script = argv[0]
filename = argv[1]

txt = open(filename)

print "Input file: %s" %filename
print "Here is the content:",
print txt.read()

print "\n\t----EOF----"

print "\n\t----ReadCeption----"
txt = open("ex7.py")
print txt.read()
print "yup2"
print "yup3"