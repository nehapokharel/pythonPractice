def filter_integers(result):
    filter_list = filter(lambda x: isinstance(x,int), result)
    return list(filter_list)

y = ['r', 1, 7, 'x']
z = filter_integers(y)
print(z)