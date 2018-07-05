def sayHello(name):
	print("Hello,"+name.title()+"!")

sayHello("Tom")

def describe_pet(animal_type,pet_name):
	print('\nI have a '+animal_type+'.')
	print('My '+animal_type+"'s name is "+pet_name.title()+'.')

describe_pet('dog','dahuang')

describe_pet(pet_name='dahuang',animal_type='dog')

#def describe_pets(animal_type='dog',pet_name):会报错
def describe_pets(pet_name,animal_type='dog'):
	print('\nI have a '+animal_type+'.')
	print('My '+animal_type+"'s name is "+pet_name.title()+'.')

describe_pets('dahuang')
describe_pets(pet_name='dahuang')
describe_pets('rabbit','honey')

def sum_int(a,b):
	return a+b

print(sum_int(2,5))

def build_person(first_name,last_name,age=''):
	person ={'first_name':first_name,'last_name':last_name}
	if age:
		person['age']= age
	return person

print(build_person('Jim','Green'))
print(build_person('Jim','Green',35))
# *参数 任意参数，函数体中接到会将其封装成一个元组
# **参数 函数体质中接到参数是一个字典
# 多个参数，任意参数应放到最后

def make_pizza(*toppings):
	""" 概述制作披萨"""
	print("\nMaking a pizza with the folling toppings:")
	for topping in toppings:
		print("- "+topping)

make_pizza('pepperoni')
print('------------')
make_pizza('mushrooms','gree peppers','extra cheese')