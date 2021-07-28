fname = input('Enter file name: ')
try :
    fh = open(fname)
except :
    print('Can\'t not open the ' + fname + ' file.')
    quit()
fc = fh.read()
fc = fc.upper()
print(fc)
