a = "a"
b = "a"
print a == b #true

int_val = 3
str_val = "this is a string"
float_val = 5.67898

print "string %s" %str_val
print "%d" %int_val
print "%f" %float_val
print "%0.2f" %float_val
# just like printf statement
# can also perform maths in prin
print "%d multiply %f is %f" % (
    int_val, float_val, int_val * float_val
)

print "%d,%d" %(int_val, int_val)
print "%r" %int_val
print "%r" %str_val
print "%r" %float_val
print round(6.5)
print round(6.4)
print round(6.9)
