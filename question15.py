def insert_string_middle(str1, str2):
    length = len(str1)  
    return str1[0:int(length/2)] + str2 + str1[int(length/2):]

y = insert_string_middle('werd', 'wee')
print(y)

