from re import S


value = None
a = 123
b = 1.23 
value = 12345
# print (type (a))
# print (type (b))
# print (type (value))
#print (type (s))
s = 'Hello \nWorld'
print (s) #Вывод строки
print (a, '-',b, '-', s) 
print ('{1} - {2} - {0}' .format(a, b, s))
print (f'{a} - {b} - {s}')

f = False
print (f)