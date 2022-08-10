# print('o---o')
# print('||||')
# print('*' * 10)# * 10 times
# name = input('what is your name ? ')
# print('Hii '+ name)
# name=input('what is your name? ')
# color=input('what is your fav color')
# print(name + 'likes' +color)

# checking for the age
# birthyear = input('birth year : ')
# print(type(birthyear))
# age= 2022 - int(birthyear)
# print(type(age))
# print(age)

# strings in python 
# use singular or doulbe quotes 
# double quote is used if single quote is used within
#  for multiple line of string we use three single quotes
# detail = '''
# Hi john,

# Here is our first email to you.

# thank you , 
# the support team.
# '''
# print(detail)
# use index for fetching values at specific positions
# negative index valid
# -1 last character
# -2 last second character
# course='python for beginners'
# print(course[0:3])
# print from 0 to 2, 3 excluded.
# course[:5] form 0 to 5
# course[:] full string 

# name = 'Jennifer'
# print(name[1:-1]) #ennife gets printed


#formatted strings
# first='john'
# last='smith'
# message= first+ ' ['+last+'] is a coder.'
# msg= f'{first} [{last}] is a coder.'
# this is the use of the formatted string.
# print(msg)
# john [smith] is a coder.
# print(message)


# course='python for beginners'
# print(len(course))
# gives length of the string

# new = course.upper()
# print(new)#new string with upper variable...
# print(course)

# print(course.find('P'))#returns first index of the character.
#retuns -1 if not found.

# print(course.replace('beginners','absolute beginners'))
# changes beginners val in course string.

# if in order to check the existence of the particular order.
# print('Python' in course)
# 'in' checks within the given data type.
 
# arithmetic calculator
# print(10/3)#float value we get 3.3333
# print(10//3)#integral division


#use math module. 
# import math

# print(math.ceil(3.4))
# print(math.floor(3.4))


#if else statements

# is_hot =False
# is_cold=True
# if is_hot:
#     print("it's a hot day")
#     print("drink plenty of water")
# elif is_cold:
#     print("it's a cold day")
#     print("wear warm clothes")
# else:
#     print("it's a lovely day")

# weight conversion program.
# weight=int(input('Weight '))
# unit=input('(L)bs or (K)gs: ')
# if unit.upper()=='L':
#     converted=weight*0.45
#     print(f"you are {converted} kgs")
# elif unit.upper()=='K':
#     converted=weight/0.45
#     print(f"you are {converted} lbs ")
# else:
#     print("wrong input:")

# for loop
# for item in ['mosh','john','sarah']:
#     print(item)

# for item in range(5,101,5):
#     print(item)

# price=[10,20,30]
# total=0
# for i in price:
#     total+=i

# print(f"total : {total}")

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")


# printing F with stars 
# for x in range(5):
#     if x==0 or x==2:
#         print(5*'*')
#     else:
#         print(2*'*')


# lists
# names=['john','adarsh','adeesh','subhas','jeevan']
# print(names[0])
# print(names[:])#from 2 to 3 index values
# print(names)
# names[0]+=' snow'#altering the values
# print(names)

# largest no in the list

# num=[2,4,7,65,43,98,654,33,789,334,431]
# max=num[0]
# for x in num:
#     if(x>max):
#         max=x

# print(f'the highest no in the list is {max} ')











