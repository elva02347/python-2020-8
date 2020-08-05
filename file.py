'''
file = open('filetest.txt','w')
file.write('this is a test')
readfile = open('filetest.txt','r')
save = readfile.read()
print(save)
readfile.close()
'''
f = open('filetest.txt','a')
f.write("I'm a high school student.")


f.close()