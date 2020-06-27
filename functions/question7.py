def check_upper_letters(string):
    upper_count = 0
    for letter in string:
        if letter.isupper():
            upper_count = upper_count + 1
        else:
            pass
    return upper_count

def check_lower_letters(string):
    lower_count = 0
    for letter in string:
        if letter.islower():
            lower_count = lower_count +1
        else:
            pass
    return lower_count 


word = input('Enter words: ')
y = check_upper_letters(word)
z = check_lower_letters(word)
print('No. of Upper case characters: ', y)
print('No of Lower case characyers:', z)