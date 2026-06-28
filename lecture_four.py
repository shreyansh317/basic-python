'''# dictonary and set
dict ={
"name": "John",
"age": 30,
"cgpa":6.5,
"marks": [98,95,96]
}
dict["name"] = "Doe brawins"
dict["surname"] = "brawins"
print(dict)
null_dict = {}
null_dict["name"] = "shreyansh"
print(null_dict)
#nested dictionary
student = {
    "name": "shreyansh",
    "subjects": {
        "phy": 65,
        "chem": 70,
        "maths": 59
    }
}

#dictionary methods
print(list(student.keys()))
print(student.values())
print(student.items())
print(student.get("name"))
new_dict = {"city": "delhi", "age": 17}
student.update(new_dict)
print(student)
#sets
collection = {1, 2, 3, 4, 5}
print(collection)
print(type(collection))

collection = {1, 2, 1,4,4,2,"hello","hello"}
print(collection)
print(len(collection))
#duplicates value are not allowed in sets
# empty set
collection = set()
print(collection)
#add elements to set
collection = set()
print(collection)
collection.add(1)
collection.add(2)
collection.add(3)
print(collection)
# set.union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

#store the following word meaning in the python dictionary table and catand its meaning

dict = {
    "table": "a peice of furniture with a flat top ",
    "cat": "a small animal",
}
print(dict)'''
# you are giving a list of subjects for students.assume one classroom required for one subject. how many class room needed byall student
# "python"'"java","c++","python","javascript","java","c++","python","c++",

subjects = {
    "python","java","c++","python","javascript","java","c++","python","c++"
    }
print(subjects)
print(len(subjects)) #4
#wap to enter a marks of 3 subjects from the user and store them in a dict.  and start with an empty dict.and add one by one use subject name as a key and mark as a value.
marks = {}
x= int(input("enter the marks physics: "))
marks.update({"physics": x})
x= int(input("enter the marks chemistry: "))
marks.update({"chemistry": x})
x= int(input("enter the marks mathematics: "))
marks.update({"mathematics": x})

print(marks)
