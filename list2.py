# rang(a,b) a~b-1
for value in range(1,5):
	print(value)
#以上打印1~4

# 使用list 和 rang 创建数字列表
number = list(range(1,6))
print(number)

# 从2开始，不断加3直到超过13
mumber1 = list(range(2,13,3))
print(mumber1)

squares =[]
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares2 = [x**3 for x in range(1,10)]
print(squares2)

# 切片：列表的一部分
players =["Messi","C Ronaldo","Diego Costa","Neymar","David SILVA"]
print(players)
print(players[1:3])
#从0开始
print(players[:4])
#从第三个元素到最后
print(players[2:])
#倒数3个
print(players[-3:])

for player in players[:3]:
	print("Hi :"+player)

# 复制列表
vplayers =players[:]

print(players)
print(vplayers)
vplayers.append("Torres")
print(players)
print(vplayers)