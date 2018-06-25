# 列表是由一系列按特定顺序排列的元素组成
bicycles =['trek',"cannondale",'redline','specialized']
print(bicycles)
# 通过索引访问元素
print(bicycles[0])
print(bicycles[3])
# -1 访问最后一个元素
print(bicycles[-1])

# 修改元素
bicycles[1]='xxx'
print(bicycles)

# 追加元素
bicycles.append("yyyy")
print(bicycles)
# 添加元素
bicycles.insert(1,"zzzz")
print(bicycles)

# del 删除某个原生
del bicycles[2]
print(bicycles)

# pop 弹出元素,并删除列表中的元素，默认为最后一个 pop(i) 第i个
b2 =bicycles.pop()
print(bicycles)
print(b2)

# remove(value),只移除第一个值
bicycles.append('zzzz');
print(bicycles)
bicycles.remove('zzzz');

print(bicycles)

##sort() 排序

bicycles.sort()
print(bicycles)

bicycles.sort(reverse=True)
print(bicycles)

#sorted() 临时排序
b1 = ['trek', 'zazz', 'redline', 'specialized', 'zzzz']
b3 = sorted(b1)
print(b1)
print(b3)
print(sorted(b1,reverse=True))

#倒队列，永久性
b1.reverse()
print(b1)

print(len(b1))

# for 循环遍历
for bicycle in bicycles:
	print(bicycle)
	print("---")
	
print("hehehe")

