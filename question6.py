w = input('enter sentence: ')

if 'not' and  'poor' in w:   
    a = w.index('poor')
    b = w.index('not')
    c = w[b:a+len('poor')]
    w = w.replace(c,'good')
    print(w)


