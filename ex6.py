from sys import argv

# script, first, second, third = argv
print "This is the name of the script argv[0]", argv[0]
print "This is the argv[1]", argv[1]
print "This is the argv[2]", argv[2]
print "This is the argv[3]", argv[3]
print argv.count('3')
print len(argv)