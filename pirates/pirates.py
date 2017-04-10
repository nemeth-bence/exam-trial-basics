pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that
# - have wooden leg and
# - have more than 15 gold

def gold_filter(list):
   for i in range(0, len(list)):
       if list[i]['gold'] > 15:
           print(list[i]['Name'] + " have more than 15 gold")

       if list[i]['has_wooden_leg'] is True:
           print(list[i]['Name'] + " have wooden leg")

gold_filter(pirates)
