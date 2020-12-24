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
    elif position == 'cf':
        pace = str(random.randint(73, 91))
        shot = str(random.randint(77, 93))   
        passing = str(random.randint(77, 92))
        dribbling = str(random.randint(78, 93))
        defence = str(random.randint(33, 66))
        physical = str(random.randint(75, 94))
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']   
    elif position == 'rw' or position == 'lw':
        pace = str(random.randint(79, 92))
        shot = str(random.randint(74, 86))   
        passing = str(random.randint(79, 91))
        dribbling = str(random.randint(85, 93))
        defence = str(random.randint(30, 59))
        physical = str(random.randint(65, 83))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']  
    elif position == 'rm' or position == 'lm':
        pace = str(random.randint(78, 90))
        shot = str(random.randint(75, 84))   
        passing = str(random.randint(81, 93))
        dribbling = str(random.randint(84, 92))
        defence = str(random.randint(41, 59))
        physical = str(random.randint(70, 85))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']   
    elif position == 'cam':
        pace = str(random.randint(70, 85))
        shot = str(random.randint(78, 86))   
        passing = str(random.randint(84, 91))
        dribbling = str(random.randint(86, 92))
        defence = str(random.randint(63, 74))
        physical = str(random.randint(70, 85))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'cm': 
        pace = str(random.randint(69, 84))
        shot = str(random.randint(70, 84))   
        passing = str(random.randint(82, 90))
        dribbling = str(random.randint(84, 90))
        defence = str(random.randint(70, 83))
        physical = str(random.randint(72, 88))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']  
    elif position == 'cdm': 
        pace = str(random.randint(65, 80))
        shot = str(random.randint(70, 80))   
        passing = str(random.randint(80, 87))
        dribbling = str(random.randint(81, 88))
        defence = str(random.randint(79, 89))
        physical = str(random.randint(80, 94))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'lwb' or position == 'rwb': 
        pace = str(random.randint(75, 86))
        shot = str(random.randint(70, 80))   
        passing = str(random.randint(77, 86))
        dribbling = str(random.randint(75, 84))
        defence = str(random.randint(75, 86))
        physical = str(random.randint(76, 85))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'lb' or position == 'rb': 
        pace = str(random.randint(80, 92))
        shot = str(random.randint(50, 67))   
        passing = str(random.randint(70, 81))
        dribbling = str(random.randint(73, 83))
        defence = str(random.randint(74, 83))
        physical = str(random.randint(77, 87))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']   
    elif position == 'cb': 
        pace = str(random.randint(60, 80))
        shot = str(random.randint(35, 60))   
        passing = str(random.randint(60, 74))
        dribbling = str(random.randint(61, 72))
        defence = str(random.randint(84, 90))
        physical = str(random.randint(82, 93))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']  
    elif position == 'gk': 
        pace = str(random.randint(77, 95))
        shot = str(random.randint(76, 90))   
        passing = str(random.randint(78, 89))
        dribbling = str(random.randint(75, 94))
        defence = str(random.randint(45, 72))
        physical = str(random.randint(81, 93))             
        stats = ['Diving: '+pace+'', 'Handling: '+shot+'', 'Kicking: '+passing+'', 'Reflexes: '+dribbling+'', 'Speed: '+defence+'', 'Positioning: '+physical+'']                
  elif kind == '2':
    if position == 'st':
        pace = str(random.randint(81, 95))
        shot = str(random.randint(85, 97))   
        passing = str(random.randint(80, 91))
        dribbling = str(random.randint(83, 91))
        defence = str(random.randint(40, 70))
        physical = str(random.randint(76, 94))
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'cf':
        pace = str(random.randint(80, 95))
        shot = str(random.randint(83, 97))   
        passing = str(random.randint(85, 94))
        dribbling = str(random.randint(82, 98))
        defence = str(random.randint(43, 76))
        physical = str(random.randint(80, 94))
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+''] 
    elif position == 'rw' or position == 'lw':
        pace = str(random.randint(85, 97))
        shot = str(random.randint(80, 90))   
        passing = str(random.randint(84, 93))
        dribbling = str(random.randint(88, 96))
        defence = str(random.randint(40, 69))
        physical = str(random.randint(70, 88))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'rm' or position == 'lm':
        pace = str(random.randint(83, 94))
        shot = str(random.randint(79, 88))   
        passing = str(random.randint(87, 96))
        dribbling = str(random.randint(88, 95))
        defence = str(random.randint(60, 74))
        physical = str(random.randint(75, 90))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'cam':
        pace = str(random.randint(80, 90))
        shot = str(random.randint(82, 91))   
        passing = str(random.randint(88, 96))
        dribbling = str(random.randint(89, 97))
        defence = str(random.randint(73, 84))
        physical = str(random.randint(74, 88))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'cm': 
        pace = str(random.randint(75, 88))
        shot = str(random.randint(78, 87))   
        passing = str(random.randint(88, 95))
        dribbling = str(random.randint(87, 94))
        defence = str(random.randint(75, 86))
        physical = str(random.randint(80, 91))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'cdm': 
        pace = str(random.randint(70, 84))
        shot = str(random.randint(75, 83))   
        passing = str(random.randint(87, 94))
        dribbling = str(random.randint(83, 91))
        defence = str(random.randint(85, 93))
        physical = str(random.randint(85, 97))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'lwb' or position == 'rwb': 
        pace = str(random.randint(80, 92))
        shot = str(random.randint(75, 84))   
        passing = str(random.randint(80, 89))
        dribbling = str(random.randint(79, 86))
        defence = str(random.randint(80, 88))
        physical = str(random.randint(79, 87))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'lb' or position == 'rb': 
        pace = str(random.randint(85, 97))
        shot = str(random.randint(60, 72))   
        passing = str(random.randint(74, 83))
        dribbling = str(random.randint(77, 86))
        defence = str(random.randint(80, 87))
        physical = str(random.randint(81, 89))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
    elif position == 'cb': 
        pace = str(random.randint(67, 86))
        shot = str(random.randint(40, 65))   
        passing = str(random.randint(71, 82))
        dribbling = str(random.randint(65, 75))
        defence = str(random.randint(86, 97))
        physical = str(random.randint(84, 96))             
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']   
    elif position == 'gk': 
        pace = str(random.randint(82, 97))
        shot = str(random.randint(82, 93))   
        passing = str(random.randint(81, 92))
        dribbling = str(random.randint(83, 94))
        defence = str(random.randint(65, 79))
        physical = str(random.randint(84, 95))             
        stats = ['Diving: '+pace+'', 'Handling: '+shot+'', 'Kicking: '+passing+'', 'Reflexes: '+dribbling+'', 'Speed: '+defence+'', 'Positioning: '+physical+'']                                                  
                                 

  elif kind == '6':
    if position == 'st':
      if id == '1':
        pace = '75 to 84'
        shot = ''   
        passing = str(random.randint(74, 88))
        dribbling = str(random.randint(76, 89))
        defence = str(random.randint(30, 60))
        physical = str(random.randint(75, 94))
        stats = ['Pace: '+pace+'', 'Shooting: '+shot+'', 'Passing: '+passing+'', 'Dribbling: '+dribbling+'', 'Defence: '+defence+'', 'Physical: '+physical+'']
      
    else: print('u messed up')

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
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'cf':
      stats = statgen('cf', kind)
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'rw' or position == 'lw':
      stats = statgen(position, kind)
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'lm' or position == 'rm':
      stats = statgen(position, kind)
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'cam':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'cm':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'cdm':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'lwb' or position == 'rwb':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'lb' or position == 'rb':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'cb':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'gk':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Normal')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)                                          
  elif kind == '2':
    #icons
    if position == 'st':
      stats = statgen(position, kind, id)
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'cf':
      stats = statgen(position, kind, id)
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'lw' or position == 'rw':
      stats = statgen(position, kind, id)
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'lm' or position == 'rm':
      stats = statgen(position, kind, id)
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)                
    elif position == 'cam':
      stats = statgen(position, kind, id)
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'cm':
      stats = statgen(position, kind, id)
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats) 
    elif position == 'cdm':
      stats = statgen(position, kind, id)
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'lwb' or position == 'rwb':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)                             
    elif position == 'lb' or position == 'rb':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'cb':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)
    elif position == 'gk':
      stats = statgen(position, kind)                     
      stats.append(position.upper())
      stats.append('Type: Icon')
      if random.randint(0, 11) == 7:
        stats.append(random.choice(narwhalnamelist)+ ' Narwhal')
      else:
        stats.append(random.choice(firstnamelist)+' '+random.choice(lastnamelist))
      print(stats)            
  elif kind == '6':
    if position == 'st':
      if id == '1':
        stats = statgen(position, kind, id)
        stats.append(position.upper())
        stats.append('Bean Biggie')
        print(stats)
        
                       
