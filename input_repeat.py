'''
message = ''
while message!='Q':
	message = input("Enter the word, I will repeat it back to you:")
	if message !='Q':
		print(message)
'''

'''
active = True
while active:
	message= input("Enter the word, I will repeat it back to you:")

	if message == 'Q':
		active = False
	else:
		print(message)
'''


while True:
	message= input("Enter the word, I will repeat it back to you:")

	if message == 'Q':
		break
	else:
		print(message)
