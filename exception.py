"""try-except 异常-else 异常捕获"""

try:
    print(5/0)
except ZeroDivisionError:
    # pass 关键字，什么也不处理
    print("You can't divide by zero.")
#else: 成功后执行