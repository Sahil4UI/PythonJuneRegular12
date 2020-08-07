file = open('image1.jpg','rb')
data = file.read()
file.close()



file = open('image2.jpg','wb')
file.write(data)
file.close()