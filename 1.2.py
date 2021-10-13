try:
    a = int(input ('Введие число - '))
    c = int(input ('Введие систему счисления - '))
    b = ' '
except ValueError:
    print('Ошибка')
else:
     if a < 0:
       print('Ошибка')
     else:
       if c==2 or c==8:
         def cc(a, b, c):
             while a > 0:
                   b = str(a % c) + b
                   a = a//c
             print(b)
             return a, b, c
         cc(a, b, c)
       else:
           print('Ошибка')
