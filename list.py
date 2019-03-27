#오늘은 주석부터 공부
#파이썬에서 주석은 #바ㅓ튼

import this
#The zen of python

print('\n\n')

#list 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

print('\n\n')

people = ['김', '서', '이', '윤', '양']
message = "내 성은 "+people[0]+"씨 입니다."
print(message)

print('\n\n')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[-1] = 'ducati'
print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)

print('\n\n')

car = []
car.append('kia')
car.append('hyundai')
car.append('benz')
car.append('audi')
print(car)
car.insert(2, 'chevrolet')
print(car)
del car[3]
print(car)
