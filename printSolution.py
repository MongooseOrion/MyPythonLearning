# If have '' ,will output with no calculating, or calculating
print(3+5)
print('3+5')

# Put the operator output to the file"TEXT.txt", with no ''
fp=open('D:/TEXT.txt','a+')
print(3+2, file=fp)
fp.close()

# Character string in a signal line output
print('master','output','fork')
