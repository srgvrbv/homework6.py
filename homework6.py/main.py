my_dict = {'Sergey' : 1971,'Natasha' : 1974,'Kseniya' : 2005}
print(my_dict)
print(my_dict['Natasha'])
print(my_dict.get('Elena'))
my_dict['Egor'] = 1990
my_dict['Ivan'] = 1997
a = my_dict.pop('Egor')
print(a)
print(my_dict)

my_set = {1,2,3,4,0,1,2,3,1,2,'lime',True,(3,3,2,1)}
print(my_set)
my_set.add(9)
my_set.add(99)
my_set.discard('lime')
print(my_set)