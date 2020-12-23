import random

def statgen(position, kind, id='0'):
  pace = ''
  shot = ''
  passing = ''
  dribbling = ''
  defence = ''
  physical = ''

  if kind == '1':
    if position == 'st':
        pace = str(random.randint(76, 91))
        shot = str(random.randint(79, 93))   
        passing = str(random.randint(74, 88))
        dribbling = str(random.randint(76, 89))
        defence = str(random.randint(30, 60))
        physical = str(random.randint(75, 94))
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
  else:
    print('u messed up')

  return stats

def playergen(position, kind, id='0'):
  firstnamelist = ['Super', 'Diamond', 'Cool', 'Fire', 'Water', 'Ice', 'Computer', 'Party', 'Peace', 'Burger', 'Party', "Ryan's", 'New', 'Cute', 'Magma', 'Plasma', 'Nutty', 'Cash', 'Awesome', 'Speedy', 'Power', 'Chocolate', 'Purple', 'Red', 'Blue', 'Snow', 'Winter', 'Pink', 'Gold', 'Silver', 'Bronze', 'Big', 'Little', "Alex's", 'Poison', 'Rose', 'Zoom', 'Nitro', 'Lava', 'Aqua', 'Orange', 'Strong', 'Wind', 'Earth', 'Flame', 'Psychic', 'Wolf', 'Steam']
  lastnamelist = ['Smallie', 'Clippy', 'Tsum', 'Biggie', 'Mouse', 'Jumb', 'Bumb', 'Cheb', 'Mouse']
  narwhalnamelist = ['Sleepy', 'Fuzzy', 'Mr', 'Norman', 'Pusheen', 'Pushane', 'Shane', 'Stress', 'Cute']
  stats = []
  #types: 1 = normal, 2 = icon, 3 = scream, 4 = totw1, 5 = totw2
  if kind == '1':
    if position == 'st':
      stats = statgen('st', '1', '0')
      stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)                 
                       
      
playergen('st', '1')
