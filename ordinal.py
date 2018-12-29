def ordinal(num):
    l = {1:'st',2:'nd',3:'rd'}
    
    num2 = num if num < 20 else  (num % 10)
    #print(num, num % 10, num2)
    return '{}{}'.format(num,l.get(num2, 'th'))
