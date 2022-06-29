#MVP Dating service
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    print ('Happy couples:')
    couples = list(zip(boys, girls))
    for boy, girl in couples:
        print (f'{boy} and {girl}')
else:
    print ('Ooops! There is someone without partner...')
print()

#cook book
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]
person = int(input('How many persons? '))
for name, dish in cook_book:
    print (f'{name.capitalize()}:')
    for reagent, mass, measure in dish:
        print (f'{reagent}, {mass * person}{measure}')
    print ()