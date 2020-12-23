import random

def statgen(position, type, id='0'):
  pace = ''
  shooting = ''
  passing = ''
  dribbling = ''
  defence = ''
  physical = ''
  
  stats = ['Pace: '+pace, 'Shooting: '+shooting, 'Passing: '+passing, 'Dribbling: '+dribbling, 'Defence: '+defence, 'Physical: '+physical]
  if type = '1':
    if position = 'st':
        pace = str(random.randint(76, 91)
        shooting = str(random.randint(79, 93)
        passing = str(random.randint(74, 88)
        dribbling = str(random.randint(76, 89)
        defence = str(random.randint(30, 60)
        physical = str(random.randint(75, 94)
   return stats

def playergen(position, type, id='0')
  firstnamelist = ['super', 'diamond', 'cool', 'fire', 'water', 'ice', 'computer', 'party', 'peace', 'burger', 'party', "ryan's", 'new', 'cute', 'magma', 'plasma', 'nutty', 'cash', 'awesome', 'speedy', 'power', 'chocolate', 'purple', 'red', 'blue', 'snow', 'santa', 'pink', 'gold', 'silver', 'bronze', 'big', 'little', "alex's", 'poison', 'rose', 'zoom', 'nitro', 'lava', 'aqua', 'orange', 'strong', 'wind', 'earth', 'flame', 'psychic', 'wolf', 'steam']
  lastnamelist = ['Smallie', 'Clippy', 'Tsum', 'Biggie', 'Mouse', 'Jumb', 'Bumb']
  narwhalnamelist = ['Sleepy', 'Fuzzy', 'Mr', 'Norman', 'Pusheen', 'Pushane', 'Shane', 'Stress', 'Cute']
  stats = []
  #types: 1 = normal, 2 = icon, 3 = scream, 4 = totw1, 5 = totw2
  if type = '1':
    if position = 'st':
      stats = statgen('st', '1')
      print statgen                 
                       
      
