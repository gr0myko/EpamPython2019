pizza = {'ground pepper', 'salt', 'cheese', 'dough', 'sweet basil',
         'oregano', 'pepperoni', 'garlic', 'tomatoes', 'onion'}
shaverma = {'cabbage', 'fried chicken', 'cucumbers', 'lavash',
            'sause', 'onion', 'tomatoes'}

print('Do pizza and shaverma include totally different ingredients?:',
      pizza.isdisjoint(shaverma))

print('Can we make shaverma out of pizza ingredients?:',
      shaverma.issubset(pizza))

print('You need to buy this ingredients for cooking pizza and shaverma:',
      set.union(pizza, shaverma))

print('What ingredients are in both dishes? Buy twice more of them!:',
      set.intersection(pizza, shaverma))

print('Unique ingredients for pizza:', pizza.difference(shaverma))

pizza.add('parmesan')
print('Pizza is better with extra cheese - parmesan:', pizza)

shaverma.remove('fried chicken')
print('Vegetarian shaverma:', shaverma)


