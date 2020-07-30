Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: /Users/brainmentors/Documents/problem-1.py =============
Total Marks of Student1 : 210
Total Marks of Student2 : 210
Total Marks of Student3 : 45
Total Marks of Student4 : 300
Total Marks of Student5 : 90
>>> 
============== RESTART: /Users/brainmentors/Documents/problem-1.py =============
Total Marks of Student1 : 210    |  Perc = 70.0%
Total Marks of Student2 : 210    |  Perc = 70.0%
Total Marks of Student3 : 45    |  Perc = 15.0%
Total Marks of Student4 : 300    |  Perc = 100.0%
Total Marks of Student5 : 90    |  Perc = 30.0%
>>> help(tuple)
Help on class tuple in module builtins:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> tup = (1,2,3,4,5,6,7,8,9,10)
>>> tup
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> tup[0]
1
>>> tup[-1]
10
>>> tup[::-1]
(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
>>> list1=[1,2,3,4]
>>> list1[0]=100
>>> list1
[100, 2, 3, 4]
>>> tup
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> tup[0]=100
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tup[0]=100
TypeError: 'tuple' object does not support item assignment
>>> tup = (0)*10
>>> tup
0
>>> tup  = [0,0,0,1,1,1,2]
>>> tup.count(0)
3
>>> tup.count(1)
3
>>> tup.count(-1)
0
>>> tup.index(0)
0
>>> tup.index(1)
3
>>> #Dictionary
>>> tup = 1,2,3,4,5
>>> list = 1,234
>>> list
(1, 234)
>>> list1 = 1,2,3,4
>>> type(list1)
<class 'tuple'>
>>> list1 = list("1234")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list1 = list("1234")
TypeError: 'tuple' object is not callable
>>> list5 = list("1234")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list5 = list("1234")
TypeError: 'tuple' object is not callable
>>> list5 = list(12345)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list5 = list(12345)
TypeError: 'tuple' object is not callable
>>> list5 = list(1,2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list5 = list(1,2)
TypeError: 'tuple' object is not callable
>>> x = 1,2,3,4,5
>>> type(x)
<class 'tuple'>
>>> #Dictionary
>>> x = {"key":"value"}
>>> type(x)
<class 'dict'>
>>> x = {"one":1,"two":2,"three":3,"four":4}
>>> x
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
>>> y ={}
>>> y["one"] = 1
>>> y
{'one': 1}
>>> y["two"] = 2
>>> y
{'one': 1, 'two': 2}
>>> del y["two"]
>>> y
{'one': 1}
>>> x
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
>>> x.keys()
dict_keys(['one', 'two', 'three', 'four'])
>>> x.values()
dict_values([1, 2, 3, 4])
>>> x.items()
dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
>>> x.update({"five",5})
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x.update({"five",5})
ValueError: dictionary update sequence element #0 has length 4; 2 is required
>>> x.update({"five":5})
>>> x
{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
>>> x.update({'two':'II'})
>>> x
{'one': 1, 'two': 'II', 'three': 3, 'four': 4, 'five': 5}
>>> x.get("three")
3
>>> x.popitem()
('five', 5)
>>> x
{'one': 1, 'two': 'II', 'three': 3, 'four': 4}
>>> x.pop("two")
'II'
>>> x
{'one': 1, 'three': 3, 'four': 4}
>>> y = x.copy()
>>> id(x)
140575747295936
>>> id(y)
140575747257408
>>> y
{'one': 1, 'three': 3, 'four': 4}
>>> y.clear()
>>> y
{}
>>> x.clear()
>>> x.clear()
>>> x
{}
>>> x = {"one":1,"two":2,"three":3,"four":4}
>>> y = 0
>>> x = {"one","two","three","four"}
>>> x
{'one', 'three', 'two', 'four'}
>>> y
0
>>> z = dict.fromkeys(x,y)
>>> z
{'one': 0, 'three': 0, 'two': 0, 'four': 0}
>>> z = dict.fromkeys(x,x)
>>> z
{'one': {'one', 'three', 'two', 'four'}, 'three': {'one', 'three', 'two', 'four'}, 'two': {'one', 'three', 'two', 'four'}, 'four': {'one', 'three', 'two', 'four'}}
>>> 