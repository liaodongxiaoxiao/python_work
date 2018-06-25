# 字典，一系列键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
# 通过key 访问 value 
print(alien_0['color'])

# 添加键值
alien_0['x_position'] = 30
alien_0['y_position'] = 50

print(alien_0)
# 修改值
alien_0['points'] = 10

print(alien_0)

# 删除值
del alien_0['points']

print(alien_0)
print('-----------------------')
#遍历
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'jim': 'object c',
	'lucy':'python'
}

for key,value in favorite_languages.items():
	print(key.title()+"'s favarite language is "+ value.title()+".")
print('------------keys-----------')
# 遍历所有键
for key in favorite_languages.keys():
	print(key.title())

print('------------values-----------')
# 遍历所有值
for value in favorite_languages.values():
	print(value.title())
print('-----------set-values-----------')
for value in set(favorite_languages.values()):
	print(value.title())

# 列表中存字典
# 字典中存列表
# 字典中存字典