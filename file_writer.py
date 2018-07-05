# pen('path/filename','模式')
# 默认不写为只读模式
# r 读模式
# w 写模式
# a 附加模式
# r+ 读写模式
with open('tmp/programming.txt','w') as file_object:
    file_object.write('I love python.\n')
    file_object.write('I love Java too.')