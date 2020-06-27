sample_dictionary = {"0": 10, "1": 20, "2": 30}

key = input("Enter key: ")

if key in sample_dictionary.keys():
    print("key already exist")
else:
    print("key does not exist")
