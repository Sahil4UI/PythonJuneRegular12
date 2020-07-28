Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = []
>>> #EMPTY LIST
>>> list2 = list("1,2,3,4,5,6,7,8,9,10")
>>> list2
['1', ',', '2', ',', '3', ',', '4', ',', '5', ',', '6', ',', '7', ',', '8', ',', '9', ',', '1', '0']
>>> list1
[]
>>> list1 = [1,2,3,4,5]
>>> list1[-1]
5
>>> list1[-4]
2
>>> list1 = [1,[2,[3,4,5,6,[7,8,9],10],11],12]
>>> list1
[1, [2, [3, 4, 5, 6, [7, 8, 9], 10], 11], 12]
>>> 
>>> 
>>> list1[1][1][4][1]
8
>>> #slicing
>>> list1 = [i for i in range(1,11)]
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list1[3:7]
[4, 5, 6, 7]
>>> list1[-1:-5:-1]
[10, 9, 8, 7]
>>> list1[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> list1 = []
>>> list1.append(5)
>>> list1.append(4)
>>> list1.append(6)
>>> list1
[5, 4, 6]
>>> list1.append(100)
>>> list1
[5, 4, 6, 100]
>>> list1.insert(2,5)
>>> list1
[5, 4, 5, 6, 100]
>>> list1
[5, 4, 5, 6, 100]
>>> list1.pop()
100
>>> list1.pop()
6
>>> list1
[5, 4, 5]
>>> list1.pop(1)
4
>>> list1
[5, 5]
>>> list1= [i for i in range(1,11)]
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list1.remove(5)
>>> list1
[1, 2, 3, 4, 6, 7, 8, 9, 10]
>>> list1.remove(10)
>>> list1
[1, 2, 3, 4, 6, 7, 8, 9]
>>> del list1[2]
>>> list1
[1, 2, 4, 6, 7, 8, 9]
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list1= [1,2,3,4]
>>> list2 = [5,6,7,8]
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8]
>>> list1.index(5)
4
>>> list1.count(8)
1
>>> list2.count(0)
0
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8]
>>> list1.clear()
>>> list1
[]
>>> list2
[5, 6, 7, 8]
>>> list2.reverse()
>>> list2
[8, 7, 6, 5]
>>> list2.sort()
>>> list2
[5, 6, 7, 8]
>>> list2.sort(reverse=True)
>>> list2
[8, 7, 6, 5]
>>> 
>>> 
>>> 
>>> list1 =[1,2,3,4]
>>> list2 = list1.copy()
>>> list1
[1, 2, 3, 4]
>>> list2
[1, 2, 3, 4]
>>> list2.append(5)
>>> list2
[1, 2, 3, 4, 5]
>>> list1
[1, 2, 3, 4]
>>> #shallow copy
>>> #deep  copy
>>> list1 = [1,2,3,4]
>>> list2 = list2.copy(list1)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    list2 = list2.copy(list1)
TypeError: copy() takes no arguments (1 given)
>>> list2 = list2.copy()
>>> 
>>> 
>>> #how to make deep copy
>>> list1 = [1,2,3,4,5,6]
>>> import copy
>>> list2 = copy.deepcopy(list1)
>>> list1
[1, 2, 3, 4, 5, 6]
>>> list2
[1, 2, 3, 4, 5, 6]
>>> list1.append(7)
>>> list1
[1, 2, 3, 4, 5, 6, 7]
>>> list2
[1, 2, 3, 4, 5, 6]
>>> list2.append(10)
>>> list1
[1, 2, 3, 4, 5, 6, 7]
>>> list2
[1, 2, 3, 4, 5, 6, 10]
>>> 