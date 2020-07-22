names = ['Peter Parker','Clark Kent', 'Wade Wilson','Bruce Wayne']
heroes = ['Spiderman','Superman','Deadpool', 'Batman' ]

# original
index= 0
for name in names:
    print(index, name)
    index += 1
    
for ind, name in enumerate(names):
    print(ind, name)
    print(f'{name} is actually {heroes[ind]}')

for name, hero in zip(names, heroes):
     print(f'{name} is actually {hero}')
     
for value in zip(names, heroes):
     print(f'{value[0]} is actually {value[1]}')
     
# unpacking
a,b,*c = (1,2,3,4,5)
print(a)
print(b)
print(c)

a, b ,*_ = [1,2,3,4,5]
a,b,*c,d = [1,2,3,4,5]