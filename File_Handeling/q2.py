vowelsList = 'aeiouAEIOU'
vcount=cCount=lowerCount=upperCount = 0

with open('file02.txt','r') as file:
    for line in file:
        for char in line:
            if (char >= 'a' and char <='z') or (char >='A' and char <='Z'):
                if char in vowelsList:
                    vcount += 1
                else:
                    cCount +=1
                
                if (char >= 'a' and char <='z'):
                    lowerCount +=1
                elif (char >='A' and char <='Z'):
                    upperCount+=1
                
print(f"Vowels Count = {vcount}\nConsonants Count ={cCount}\nLowe Case Count = {lowerCount}\nuppercase count = {upperCount}\n")
file.close()