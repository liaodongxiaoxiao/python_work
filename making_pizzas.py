# 导入整个模块 import + module_name
#import pizza
#pizza.make_pizza('pepperoni')
#pizza.make_pizza('mushrooms','green peppers','extra cheese')


# from +module_name import function_1,function_2
#from pizza import make_pizza
#make_pizza('pepperoni')
#make_pizza('mushrooms','green peppers','extra cheese')

# as 给函数指定别名

#from pizza import make_pizza as mp
#mp('pepperoni')
#mp('mushrooms','green peppers','extra cheese')

# as 给模块指定别名 
#import pizza as p
#p.make_pizza('pepperoni')
#p.make_pizza('mushrooms','green peppers','extra cheese')

# 导入模块中所有函数
from pizza import *
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
