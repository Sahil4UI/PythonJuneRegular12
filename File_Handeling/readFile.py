file = open('file01.txt','r')
# open(filepath,accessmode (r,w))
# data = file.read()
# data = file.read(10)
# data = file.readline()
# data = file.readline(4)
data = file.readlines()

print(data)
file.close()

