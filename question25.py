list=[{},{},{}]
#list=[{1,2},{2},{4}]

if(all(not x for x in list)):
    print('empty')
else:
    print('not empty')
