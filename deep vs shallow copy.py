Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [1,2,3,4]
>>> list2 = list1.copy()
>>> list1
[1, 2, 3, 4]
>>> list2
[1, 2, 3, 4]
>>> id(list1)
140481492607360
>>> id(list2)
140481492833920
>>> list1.pop()
4
>>> list1
[1, 2, 3]
>>> list2
[1, 2, 3, 4]
>>> list1 = [1,2,3,4,5]
>>> list2 = list1
>>> id(list1)
140481489584384
>>> id(list2)
140481489584384
>>> list1.pop()
5
>>> list1
[1, 2, 3, 4]
>>> list2
[1, 2, 3, 4]
>>> #shalloW COpy
>>> import copy
>>> list1
[1, 2, 3, 4]
>>> list2 = list1.copy()
>>> id(list1)
140481489584384
>>> id(list2)
140481492834304
>>> list2 = Copy.copy(list1)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list2 = Copy.copy(list1)
NameError: name 'Copy' is not defined
>>> list2 = copy.copy(list1)
>>> list2
[1, 2, 3, 4]
>>> list2
[1, 2, 3, 4]
>>> id(list2)
140481489400576
>>> id(list1)
140481489584384
>>> import copy
>>> list1 = [[1,2,3],[4,5,6],[7,8,9]]
>>> list2 = copy.deepcopy(list1)
>>> id(list1)
140481489400448
>>> id(list2)
140481489400384
>>> id(list1[0])
140481492834304
>>> id(list2[0])
140481492833472
>>> list1
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> list2
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> list1 = [1,[2,[3,[4,[5,6,7,[8,9,[10,11],12],13],14],15],16],17]
>>> import copy
>>> list2 = copy.copy(list1)
>>> list1
[1, [2, [3, [4, [5, 6, 7, [8, 9, [10, 11], 12], 13], 14], 15], 16], 17]
>>> list2[1][0][0][3]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list2[1][0][0][3]
TypeError: 'int' object is not subscriptable
>>> list2
[1, [2, [3, [4, [5, 6, 7, [8, 9, [10, 11], 12], 13], 14], 15], 16], 17]
>>> list2[0]
1
>>> list2[1][0][0][0]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    list2[1][0][0][0]
TypeError: 'int' object is not subscriptable
>>> list2[1][1][1][1]
[5, 6, 7, [8, 9, [10, 11], 12], 13]
>>> list2[1][1][1][1][3]
[8, 9, [10, 11], 12]
>>> id(list2[1][1][1][1][3])
140481489576448
>>> id(list1[1][1][1][1][3])
140481489576448
>>> list1
[1, [2, [3, [4, [5, 6, 7, [8, 9, [10, 11], 12], 13], 14], 15], 16], 17]
>>> list2=copy.deepcopy(list1)
>>> list2
[1, [2, [3, [4, [5, 6, 7, [8, 9, [10, 11], 12], 13], 14], 15], 16], 17]
>>> id(list2[1][1][1][1][3])
140481492833664
>>> id(list1[1][1][1][1][3])
140481489576448
>>> 