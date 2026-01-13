marks = [3, 5, 10, "Harry", True]
print(marks)
print(type(marks))
print(marks[0])
# negative indexing
print(marks[-2])
# if-else in list
if 7 in marks:
	print("yes 7 is in list marks")
else:
	print("No 7 is not in marks list")
# print the list three ways
print(marks)
print(marks[:])
print(marks[1:4])
# jumpindex 
print(marks[1:4:2])

# list comprehension
lst = [i for i in range(5)]
print(lst)
lst1 = [i*i for i in range(5)]
print(lst1)
lst2= [i*i for i in range(5) if i%2==0]
print(lst2)
# list methods l.append add a element to a list
marks.append(89)
print(marks)
# l.sort
#marks.sort()
#marks.sort(reverse =True)
# above two sort syntax throughs error bcoz str and int both present in marks list

# return index
print(marks.index(10))
print(marks.index("Harry"))
# count
print(marks.count(10))
# insert
marks.insert(1, 50)
print(marks)
# join the two list
student = ["Ashish", "Mohini", "Trividha"]
marks.extend(student)
print(marks)
# concant list
other_students = ['A', 'B']
clas = marks + student + other_students
print(clas)




