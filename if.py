'''
if 表达式：
	do something
elif 表达式：
	do something
else:
	do something
'''


cars =['audi','bmw','subaru','toyota']

for car in cars:
	if car=='bmw':
		print(car.upper())
	else:
		print(car.title())
print('-----------------------')
# if 多个条件用 and 或 or 连接
for car in cars:
	if car=='bmw' or car =='audi':
		print(car.upper())
	else:
		print(car.title())
# in / not in
print('bmw' in cars)

age = 24
message = ""

if age < 2:
	message = "你是一个婴儿"
elif age >= 2 and age < 4:
	message = "你正蹒跚学步"
elif age >= 4 and age < 13:
	message = "你是一个儿童"
elif age >= 13 and age < 20:
	message = "你是一个青年人"
elif age >= 20 and age <65:
	message = "你是一个中年人"
elif age >= 65:
	message = "你是一个老年人"

message = message.encode("utf-8")
print(message)

