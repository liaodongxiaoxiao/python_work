# with 在不需要访问文件后将其关闭
with open('tmp/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# with open(文件夹/文件名) as file_object:
# linux osx / windows \

# 逐行读
with open('tmp/pi_digits.txt') as file_object:
    for content in file_object:
        print(content.rstrip())

# 文件读到list中，遍历拼接
with open('tmp/pi_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string=''
for line in lines:
    pi_string += line.strip()
print(pi_string)
