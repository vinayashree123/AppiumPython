"""list1 = ['a','b','c']
list2 = [1,2,3]
dict1 = {k:v for (k,v) in zip(list1,list2)}
print(dict1)
print(dict(zip(list1,list2)))

dict1 = {i:i**2 for i in range(1,5)}
print(dict1)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {i : j*2 for i, j in dict1.items()}
print(dict2)

dict1 = {k:v for (v,k) in dict1.items()}
print(dict1)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {i : j for i,j in dict1.items() if j % 2!=0}
print(dict2)"""

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd':4}
dict2 = {i : dict1[i] for i in dict1.keys()-{'a','b'}}
print(dict2)

dict1 = {i : i **i for i in range(5)}
print(dict1)

