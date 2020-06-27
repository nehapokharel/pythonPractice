a = input('enter sentence: ')
word = a.split()
result={}

for i in word:
    if i not in result.keys():
        result[i]=0
    result[i] += 1

sorted_keys = sorted(result, key=result.get, reverse=True)
print({values:result[values] for values in sorted_keys})