word = input('Enter two strings: ')
a = word.split()
print(a[1][:2]+a[0][2:], a[0][:2]+a[1][2:])