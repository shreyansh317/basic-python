'''#list and tuple
marks = [10, 20, 30, 40, 50]
print(marks)
print(len(marks))
print(marks[0])
print(marks[2])
student = ["john",92.3,18,"male" ]
print(student)
# if we wanna change the value of a list we can do it
student = ["karan",76.3,17.3,"uttar pradesh"]
print(student[0])
student[0] = "arjun"
print(student[0])
# list slicing
marks=[12,23,45,56,78,12]
print(marks[2:4])
print(marks[-3:-1])
#list methods
list =[3,2,4,5]
list.append(6)
print(list)
#sorting a list
list =[3,2,4,5]
list.sort()
print(list)
#sort reverse
list =[3,2,4,5]
list.sort(reverse=True)
print(list)
#insert
list =[2,1,3]
list.insert(1,5)
print(list)
# remove
list =[2,1,3]
list.remove(1)
print(list)
#pop
list =[2,1,3]
list.pop(2)
print(list)
#tuple
tup =(2,1,3,1)
print(tup[0])
print(tup[2])
#tuple methods
tup =(2,1,3,1)
print(tup.index(3))
tup =(2,3,1,5,6,2,2,6,2,)
print(tup.count(2))

#wap to ask the user to enter name of three movies and store them in a list
movies =[]

mov1 =input("enter 1st movie : ")
mov2 =input("enter 2nd movie : ")
mov3 =input("enter 3rd movie : ")

movies.append(mov1 )
movies.append(mov2 )
movies.append(mov3 )
print(movies)
# wap to check if the list contains a palindrome of elements

list1 = ["m","a","a","m","p"]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
# wap to cont the nummber of student with the a grade in the following tuple
grade = ("a","b","c","a","d","a")
count = grade.count("a")
print(count)
grade = ["a","b","c","a","d","a"]
grade.sort()
print(grade)'''
end
