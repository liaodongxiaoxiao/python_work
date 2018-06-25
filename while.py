current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1


cu = 0
while cu<20:
	cu += 1

	if cu % 2 ==0:
		continue

	print(str(cu))

print('--------------')
pets =['dog','cat','dog','rabbit','cat','fish']
print(pets)


while 'cat' in pets:
	pets.remove('cat')

print(pets)