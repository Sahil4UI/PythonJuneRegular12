data = '''Python is a great language for the beginner-level programmers.'''

# file = open('file01.txt','w')
# file.write(data)

with open('file02.txt','w') as file:
    file.write(data) 
    # data = file.read()

file.close()