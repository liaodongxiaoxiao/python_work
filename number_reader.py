"""json读取"""
import json

with open('tmp/numbers.json','r') as f_json:
    numbers = json.load(f_json)
print(numbers)