import pickle
student1={"id":101,"Name":"Ram","Address":"NJF"}
student2={"id":102,"Name":"Shyam","Address":"Dwarka"}

db={}
db["student1"] = student1
db["student2"] = student2

file = open('binfile','ab')
pickle.dump(db,file)
file.close()
# print(db)

file = open('binfile','rb')
x = pickle.load(file)
for keys in x:
    print(keys , "=",x[keys])
file.close()


