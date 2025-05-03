'''Dictionary Operations: Given the dictionary student = {"name": "Alice", "age": 20, "major": "Computer Science"}, 
write code to:

- Add a new key-value pair: "city": "Austin".
- Update the value of the "age" key to 21.
- Print all the keys in the dictionary.'''

student = {"name": "Alice", "age": 20, "major": "Computer Science"}

student["city"]="Austin"
print(student)
student["age"]=21
print(student)
print(student.keys())