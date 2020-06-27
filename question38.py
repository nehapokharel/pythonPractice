sample_dictionary = {'a':1,'b':2,'c':3,'d':4}

key = input("Enter key: ")

if key in sample_dictionary: 
    del sample_dictionary[key]
else:
    print('key not found')
print(sample_dictionary)