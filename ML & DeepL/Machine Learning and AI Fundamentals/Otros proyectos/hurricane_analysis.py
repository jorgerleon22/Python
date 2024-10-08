# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']
 
# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']
 
# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]
 
# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]
 
# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]
 
# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']
 
# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
 
# write your update damages function here:
#Convert numerical entries to floats
def update_damages(damages):
  updated_damages = []
  for damage in damages:
    if damage == 'Damages not recorded':
      updated_damages.append(damage)
    elif damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*1000000000)
    else:
      updated_damages.append(float(damage.strip('M'))*1000000)
  return updated_damages
 
updated_damages = update_damages(damages)
 
# write your construct hurricane dictionary function here:
def construct_hurricane(names, months, years, maxwind, areas, damage, death):
  values = []
  for i in range(len(names)):
    #create a new dictionary for each hurricane and add corresponding key:values from each list
    hurricane = {}
    hurricane.update({'Name':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind':maxwind[i], 'Areas Affected':areas[i], 'Damage':updated_damages[i], 'Deaths':deaths[i]})
    values.append(hurricane)
  #create finalised dictionary - key = name, value = dictionary of hurricane info
  hurr_data = {key:value for key,value in zip(names, values)}
  return hurr_data
 
hurricane_dictionary = construct_hurricane(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
 
# write your construct hurricane by year dictionary function here:
 
def hurricane_by_year(hurricanes):
  hurricane_years = {}
  unique_years = []
  #identify unique years as keys, then add dictionaries of hurricanes that occurred that year as values
  for key in hurricanes:
    working = [hurricanes.get(key)]
    year = hurricanes[key].get('Year')
    if year not in unique_years:
      unique_years.append(year)
      hurricane_years.update({year:working})
    else:
      hurricane_years[year].append(hurricanes.get(key))
  return hurricane_years
 
hurricanes_by_year = hurricane_by_year(hurricane_dictionary)
#print(hurricanes_by_year[1932])
 
# write your count affected areas function here:
def area_count(dictionary):
  unique = []
  counts = []
  #maintain a list of areas as each is encountered, and a corresponding list of counts that can be zipped and returned as a dictionary
  for key in dictionary:
    areas = dictionary[key].get('Areas Affected')
    for area in areas:
      if area not in unique:
        unique.append(area)
        counts.append(1)
      else:
        x = unique.index(area)
        counts[x] += 1
  area_counts = {key:value for key, value in zip(unique,counts)}
  return area_counts
 
area_count = area_count(hurricane_dictionary)
 
# write your find most affected area function here:
def most_affected(dictionary):
  highest = 0
  area = ''
  #maintain variables containing the highest count and area encountered so far as we iterate through
  for key in dictionary:
    if dictionary[key] > highest:
      highest = dictionary[key]
      area = key
  print('{loc} is the most affected area, with {count} hurricanes.'.format(loc=area, count=highest))
 
#most_affected(area_count)
 
# write your greatest number of deaths function here:
 
def most_deadly(dictionary):
  highest = 0
  name = ''
  #logic virtually identical to the most affected function
  for key in dictionary:
    if dictionary[key].get('Deaths') > highest:
      highest = dictionary[key].get('Deaths')
      name = key
  print('The most deadly hurricane was {hurricane}, causing {deaths} deaths.'.format(hurricane=name,deaths=highest))
 
#most_deadly(hurricane_dictionary)
 
# write your catgeorize by mortality function here:
def hurricane_mortality_rating(dictionary):
  mort_rates = {0:[], 1:[], 2:[], 3:[], 4:[]}
  mort_scale = {0: 0, 1: 100, 2: 500, 3:1000, 4:10000}
  for hurr in dictionary:
    death = dictionary[hurr].get('Deaths')
    for x in range(len(mort_scale)):
      #check if deaths are in the currently iterated band, if so update the rate dictionary and break
      if death <= mort_scale[x]:
        mort_rates[x].append(dictionary[hurr])
        break
      else:
        continue
  return mort_rates
 
hurricane_by_mortality_rating = hurricane_mortality_rating(hurricane_dictionary)
 
# write your greatest damage function here:
def greatest_damage(dictionary):
  highest = 0
  name = ''
  #logic similar to most deadly but need to catch the strings!
  for key in dictionary:
    if dictionary[key].get('Damage') == 'Damages not recorded':
      continue
    elif dictionary[key].get('Damage') > highest:
      highest = dictionary[key].get('Damage')
      name = key
  print('The most damaging hurricane was {name}, costing ${cost}.'.format(name=name, cost=highest))
 
#greatest_damage(hurricane_dictionary)
 
# write your catgeorize by damage function here:
def hurricane_damage_rating(dictionary):
  dam_rates = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 'Not Recorded':[]}
  dam_scale = {0: 0, 1: 100000000, 2: 1000000000, 3:10000000000, 4:50000000000, 5:1000000000000}
  #same as mortality rating function, but extra line to catch the strings 
  for hurr in dictionary:
    damage = dictionary[hurr].get('Damage')
    if type(damage)== str:
      dam_rates['Not Recorded'].append(dictionary[hurr])
      continue
    for x in range(len(dam_scale)):
      if damage <= dam_scale[x]:
        dam_rates[x].append(dictionary[hurr])
        break
      else:
        continue
  return dam_rates
 
hurricane_by_damage_rating = hurricane_damage_rating(hurricane_dictionary)