"""json 存储"""
import json

numbers =[1,3,5,9,2,4,6,8]
with open('tmp/numbers.json','w') as f_json:
    """
        json.dump(内容, 文件)
    """
    json.dump(numbers,f_json)