sample_list = [1,2,3,4]
val = input("Enter string: ")
result = []

for value in sample_list:
    result.append(val + str(value))
print(result)