# 1.	What is the difference between a list, tuple, set and dictionary in Python? Give one example of each. [4 Marks]

#list :- Mutable
list1 = [1 ,2, "Aditya" , True]
print(list1)

#tuple :- immutable
tup1 = (1 , 2, "Aditya" , False)
print(tup1)

#dictionary :- mutable
dict1 = {"name": "Aditya" ,
         "course": "Btech",
         "age": 25
         }
#accesing DIct1
print(dict1.values())
print(dict1.keys())
print(dict1)
dict1["course"] = "BBA"
print(dict1)



