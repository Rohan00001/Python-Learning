# Python iteration behind the scene

## readline() method

```python
PS C:\Users\HP\Desktop\Python\loops_behind_the_scene> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> f = open('file.py')
>>> f.readline()
'print("hello")\n'
>>> f.readline()
'test= "world"\n'
>>> f.readline()
'print(test)\n'
>>> f.readline()
'x = 5\n'
>>> f.readline()
'print(x)\n'
>>> f.readline()
''
>>> 
>>> f.readline()
''
>>> 
```

readline() method is used to read the file line by line. It reads the file line by line and returns a string. It returns an empty string when it reaches the end of the file.

This method is very musch optimized and efficient. It reads the file line by line and does not load the whole file in the memory. It is very useful when you have a large file and you want to read it line by line.

## __next__() method

```bash
>>> f = open('file.py')
>>> f.__next__()
'print("hello")\n'
>>> f.__next__()
'test= "world"\n'
>>> f.__next__()
'print(test)\n'
>>> f.__next__()
'x = 5\n'
>>> f.__next__()
'print(x)\n'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

__next__() is the row method of file or iterator. It is used to read the file line by line. It reads the file line by line and returns a string. It raises StopIteration when it reaches the end of the file.

### Note: File object is an iterator.

readlines() method previously used but it is not efficient. It reads the whole file and loads it into the memory. It is not efficient when you have a large file.

## Using for loop to read the file line by line

```bash
>>> for lines in open('file.py'):
...     print(lines,end='')
...
print("hello")
test= "world"
print(test)
x = 5
print(x)
>>> 
```

We can use for loop to read the file line by line. It is very efficient and optimized. It reads the file line by line and does not load the whole file in the memory. It is very useful when you have a large file and you want to read it line by line.


## Using while loop to read the file line by line

```bash
f = open('file.py')           
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line,end='')
...
print("hello")
test= "world"
print(test)
x = 5
print(x)
>>>
```

We can use while loop to read the file line by line. It is very efficient and optimized. It reads the file line by line and does not load the whole file in the memory. It is very useful when you have a large file and you want to read it line by line.


## iter() method

```bash
>>> mylist =[1,2,3,4,5]
>>> I = iter(mylist)
>>> I
<list_iterator object at 0x000001730A0A2170>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x000001730A0A2170>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
5
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

iter() method is used to convert an iterable to an iterator. It returns an iterator object. It is used to read the file line by line. It reads the file line by line and returns a string. It raises StopIteration when it reaches the end of the file.

iter() points the memory location to the first element of the list. It always points to the first element of the list. It does not change the memory location.

In the above example, we have converted the list to an iterator using iter() method. 

We can use __next__() method to read the list element by element. But the memory location is not changing. It is the same memory location. It is because the list is an iterable and not an iterator. We have converted the list to an iterator using iter() method.

```bash
>>> f = open('file.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__() 
True
>>>
```
The file object is already comes with an iterator. We can use __next__() method to read the file line by line.

## Dictonary is an iterable but not an iterator

```bash
>>> D = { 'a':1, 'b':2 }
>>> for key in D.keys(): 
...     print(key)
...
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x0000017309F4D5D0>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

Dictionary is an iterable but not an iterator. We can use iter() method to convert the dictionary to an iterator. It returns an iterator object. It is used to read the dictionary element by element. It raises StopIteration when it reaches the end of the dictionary.

## range() is an iterable but not an iterator

```bash
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>>
```

range() is an iterable but not an iterator. We can use iter() method to convert the range to an iterator. It returns an iterator object. It is used to read the range element by element. It raises StopIteration when it reaches the end of the range.
