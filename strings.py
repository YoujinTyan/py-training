# x = 'ß'
# print(x.casefold())


# e = 'groß'
# e.casefold() == 'gross'
# print(e.casefold())  # True


# print(' '.center(3, 'w') ) 
# print('1'.center(5, 'w')) 
# print('1'.center(8) )


# my_str = 'подстрока из строк'
# print(my_str.count('стр', 0, -1 )) 
# print(my_str.count('стр') )
# print(my_str.count('стр', 1, 5) ) 
# print(my_str.count('стр', 1, 6)  )


# from sys import getdefaultencoding
# getdefaultencoding()  # utf-8
# my_string = 'кот cat'
# type(my_string) 
 
# my_string.encode()

# print(my_string.encode('ascii'))
# print(my_string.encode('ascii', errors='ignore'))
# print(my_string.encode('ascii', errors='replace'))
# print(my_string.encode('ascii', errors='xmlcharrefreplace'))

# TODO = 'encode'



# my_str = 'Discworld'
# print(my_str.endswith('jockey') )
# print(my_str.endswith('world')  )
# print(my_str.endswith('jockey', 2)  )
# print(my_str.endswith('Di', 0, 2))

# TODO = 'expandtabs'
# my_str = '\t1\t10\t100\t1000\t10000'
# print(my_str.expandtabs())
# print(my_str.expandtabs(4))


# print('{}-{}-{}'.format(1, 2, 3))
# print('{one}-{two}-{three}'.format(**{'two': 2, 'one': 1, 'three': 3}) )


# right = 'Начало{0:20}Конец'.format(7)
# left = 'Начало{0:<20}Конец'.format(8)
# center = 'Начало{0:^20}Конец'.format(9)
# print(right)
# print(left)
# print(center)


# print('{0}'.format(4/3))
# print('{0:f}'.format(4/3))


# print('  '.isalnum()) 
# print('!@'.isalnum())  
# print('abc'.isalnum())
# print('123'.isalnum())  
# print('abc123'.isalnum())


# print('continue'.isidentifier())
# print('cat'.isidentifier()) 
# print('number1'.isidentifier())
# print('1st'.isidentifier())


# print('a'.isnumeric() )
# print('0'.isnumeric())
# print('⅓'.isnumeric() ) 
# print('Ⅻ'.isnumeric())


# print('1'.isprintable()) 
# print('a'.isprintable())
# print(''.isprintable() )


# print('\t'.isspace())
# print(' '.isspace())
# print('abc123'.isspace())


# print('S Text'.istitle())
# print('s Text'.istitle())


# print(''.ljust(3, 'w')) 
# print('1'.ljust(4, 'w') )
# print('1'.ljust(4))

# print(''.rjust(3, 'w'))
# print('1'.rjust(4, 'w'))
# print('1'.rjust(4))


# print('acbca'.lstrip('aca') )


# TODO = 'maketrans, trantab'

# intab = "abc" 
# outtab = "123" 
# trantab = str.maketrans(intab, outtab) 
# print(trantab)


# my_str = 'barbarian'
# print(my_str.rindex('bar'))  
# print(my_str.rindex('bar', 1))

# my_str = ''
# print(my_str.rpartition('.') )
# my_str = '12'
# print(my_str.rpartition('.'))


# print(('abca'.rstrip('ac')))  


# my_str = 'ab\n cd\n'
# print(my_str.splitlines() ) 
# print(my_str.split('\n') )

# my_str = 'Discworld'
# print(my_str.startswith('Mad'))
# print(my_str.startswith('world', 4, 9) )

# print('abca'.strip('ac'))

# print('Кот ОбОрмот!'.swapcase())

# print('1'.zfill(4))
# print('1'.zfill(0) )
# print('-1'.zfill(4) )