largest = None
smallest = None

while True :
    sval = input ('Enter Number:')
    if sval == 'done':
        break
    try :
        ival = int (sval)
    except :
        print ('Invalid input')
        continue

    if smallest is None :
        smallest = ival
        largest = ival
    elif ival < smallest :
        smallest = ival
    elif ival > largest :
        largest = ival

print ('Maximum is',largest)
print ('Minimum is',smallest)
