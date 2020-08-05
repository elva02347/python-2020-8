file = open('image.jpg','rb')
img = file.read()

file.close()
copy = open('copy1.jpg','wb')
copy.write(img)
copy.close()