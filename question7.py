def longest_length(list):
    longestlength = list[0]
    for index in list:
        if index > longestlength:
            longestlength = index
    return longestlength

word = input('Enter string: ')
a = word.split()
li=[]

for i in a:
    li.append(len(i))
    len = longest_length(li)
print(len)
    