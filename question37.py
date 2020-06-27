sample_dictionary = {"a":10, "b":20, "c": 30}
value = sample_dictionary.values()

multiple = 1
for key in sample_dictionary:
    multiple = multiple * sample_dictionary[key]
print(multiple)