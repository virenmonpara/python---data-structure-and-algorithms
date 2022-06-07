def is_binary(s):
    return all(i in ['0', '1'] for i in s)

s = '010001010'
print(is_binary(s))
