text = "X-DSPAM-Confidence:    0.8475";
ltext = len(text)
pos0 = text.find('0')
#print (pos0, type(pos0))
num = text[pos0:ltext+1]

fnum = float(num)
print(fnum)
