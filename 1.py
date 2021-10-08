try:
    a = int(input ('Введие число - '))
    c = int(input ('Введие систему счисления - '))
    b = ' '
except ValueError:
    print('Ошибка')
else:
     if c==2 or c==8:
       def cc():
           global a
           global c
           global b
           while a > 0:
                 b = str(a % c) + b
                 a = a//c
           print(b)
       cc()
     else:
         print('Ошибка')

