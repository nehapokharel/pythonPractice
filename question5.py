word = input('Enter string: ')

if len(word)>2:
    if word[-3:]=='ing':
        print(word + 'ly')
    else:
        print(word + 'ing')
else:
    print(word)
