def sort_dictionary(result):
    sorted_keys = sorted(result, key = lambda i: i['price'])
    return sorted_keys

fruits = [
    {"name" : "apple", "price" : 150},
    {"name" : "mango", "price" : 160},
    {"name" : "litchi", "price" : 120},
    {"name" : "banana", "price" : 200}
]

y = sort_dictionary(fruits)
print(y)
   