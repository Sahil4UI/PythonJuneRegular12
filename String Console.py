Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> String1 = "harsh"
>>> String1[0]
'h'
>>> String1[-1]
'h'
>>> String1[-2]
's'
>>> String1[-3]
'r'
>>> string1 = 'Hello world'
>>> #string1[start index:stop index:step size]
>>> string1[6:10]
'worl'
>>> string1[6:11]
'world'
>>> string1[6:]
'world'
>>> string1[:]
'Hello world'
>>> #String Reverse ?
>>> string1
'Hello world'
>>> string1[::-1]
'dlrow olleH'
>>> string1[-3]
'r'
>>> string1
'Hello world'
>>> string1[::2]
'Hlowrd'
>>> string1[6:11]+string1[0:5]
'worldHello'
>>> #STring method
>>> #user -defined
>>> #pre define - function
>>> string1
'Hello world'
>>> string1.lower()
'hello world'
>>> string1.upper()
'HELLO WORLD'
>>> string1
'Hello world'
>>> string1 = string1.upper()
>>> string1
'HELLO WORLD'
>>> string1.capitalize()
'Hello world'
>>> string1
'HELLO WORLD'
>>> string1.title()
'Hello World'
>>> string1 = string1.title()
>>> string1
'Hello World'
>>> string1.swapcase()
'hELLO wORLD'
>>> string1
'Hello World'
>>> string1 = "हेलो  क्या  हाल  है भाई  ?"
>>> string1
'हेलो  क्या  हाल  है भाई  ?'
>>> string1.encode()
b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b  \xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe  \xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb2  \xe0\xa4\xb9\xe0\xa5\x88 \xe0\xa4\xad\xe0\xa4\xbe\xe0\xa4\x88  ?'
>>> "b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b  \xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe  \xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb2  \xe0\xa4\xb9\xe0\xa5\x88 \xe0\xa4\xad\xe0\xa4\xbe\xe0\xa4\x88  ?".decode()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    "b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b  \xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe  \xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb2  \xe0\xa4\xb9\xe0\xa5\x88 \xe0\xa4\xad\xe0\xa4\xbe\xe0\xa4\x88  ?".decode()
AttributeError: 'str' object has no attribute 'decode'
>>> b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b  \xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe  \xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb2  \xe0\xa4\xb9\xe0\xa5\x88 \xe0\xa4\xad\xe0\xa4\xbe\xe0\xa4\x88  ?'.decode()
'हेलो  क्या  हाल  है भाई  ?'
>>> string1
'हेलो  क्या  हाल  है भाई  ?'
>>> string1.count('ल')
2
>>> #count ->frequency of a character
>>> string1 ="Python Programming"
>>> string1.count('P')
2
>>> string.count("z")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    string.count("z")
NameError: name 'string' is not defined
>>> string1.count("Z")
0
>>> string1
'Python Programming'
>>> string1.find('P')
0
>>> string1.rfind('P')
7
>>> string1.rfind('Z')
-1
>>> string1 = "Python plus Project"
>>> string1.find('P')
0
>>> string1.rfind('P')
12
>>> string1 = "Python Plus Project"
>>> string1.find(1,"P")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    string1.find(1,"P")
TypeError: slice indices must be integers or None or have an __index__ method
>>> string1.find("P",1)
7
>>> string1
'Python Plus Project'
>>> string1.startswith('P')
True
>>> string1.startswith()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    string1.startswith()
TypeError: startswith() takes at least 1 argument (0 given)
>>> string1.startswith('Z')
False
>>> string1.endswith('t')
True
>>> len(string1)
19
>>> string1
'Python Plus Project'
>>> string1.index('P')
0
>>> string1.index('Z')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    string1.index('Z')
ValueError: substring not found
>>> string1= "hye EveryOne"
>>> string1.replace('h','B')
'Bye EveryOne'
>>> string1[0]='B'
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    string1[0]='B'
TypeError: 'str' object does not support item assignment
>>> string1= "Python is a General Purpose Programming Language"
>>> string1.split(' ')
['Python', 'is', 'a', 'General', 'Purpose', 'Programming', 'Language']
>>> string1= "SHASHWAT"
>>> string1.center(1)
'SHASHWAT'
>>> string1.center(5)
'SHASHWAT'
>>> len(string1)
8
>>> string1.center(9)
' SHASHWAT'
>>> string1.center(10)
' SHASHWAT '
>>> string1.center(20)
'      SHASHWAT      '
>>> string1.center(50,'*')
'*********************SHASHWAT*********************'
>>> string1=string1.center(50,'*')
>>> string1.replace('*','')
'SHASHWAT'
>>> string1
'*********************SHASHWAT*********************'
>>> string1.lstrip('*')
'SHASHWAT*********************'
>>> string1.rstrip("*")
'*********************SHASHWAT'
>>> string1.strip("*")
'SHASHWAT'
>>> 