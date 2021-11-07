#len(): the number of items in a list
# max(): The biggest value in a list
# min(): The smallest value in a list



student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
print(student_names[0])

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
print(student_names[1])

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
print(student_names[2])

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
print(student_names[0:2])

student_names[1] = 'Joshua'
print(student_names)

clothes = ["shorts","shoes","t-shirt"]

clothes[2] = 'warm coat'
print(clothes)

# Solution

clothes = ["shorts","shoes","t-shirt",]
if clothes[0] == 'shorts':
    clothes[0] = 'warm coat'
print(clothes)

Game_scores = ['Highest score: 200','Lowest score: 3']

print(list(reversed(Game_scores)))

Game_scores = [1,2,5,4,6,8,7,9,0]

print(sorted(Game_scores))

Game_scores = [1,2,5,4,6,8,7,9,0]

print(sorted(Game_scores))

Game_scores = [1,2,5,4,6,8,7,9,0]

print(list(reversed(sorted(Game_scores))

Game_scores = [1,2,5,4,6,8,7,9,0]

min(s2)

s = 'charlotte'
print(s)
s[0]
s[-1]
s[0:5]
s[5]


student_name = input('Which student are you looking for? ')
students = [ 'Diedre', 'Hank', 'Helena', 'Salome',]
if student_name in students:
    print('{} is in the class'.format(student_name))
else:
    print('{} is not in the class'.format(student_name))

shopping_list = ['bread','cheese','pop tarts','carrots',]
if 'bread' in shopping_list: shopping_list.append('butter')


fridge = ['cheese','pizza','coke', ]
if 'milk' not in fridge:
    print('You have no milk in the fridge')

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
for student_name in student_names: print(student_name)


student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0
for student_name in student_names: count = count + 1
print(count)



student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0
for student_name in student_names: count = count + 2
print(count)