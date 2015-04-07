__author__ = 'Agnieszka'

largest = None
smallest = None
largest = None
smallest = None
while True:
    n = raw_input("Enter a number: ")
    if n == "done":  break
    try:
        ni = int(n)
    except:
        print "Invalid input"
        continue

    if largest is None:
        largest = int(ni)
    elif largest > ni:
        largest = ni

    if smallest is None:
        smallest = int(ni)
    elif smallest < ni:
        largest = ni


print "Maximum is", largest
print "Minimum is", smallest
