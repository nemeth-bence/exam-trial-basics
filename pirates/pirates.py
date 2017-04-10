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
    list_golds = []
    for i in range(0, len(list)):
        for key, value in list[i].items():
            if key == 'gold':
                if value > 15:
                    list_golds.append(list[i])
    for i in range(0, len(list_golds)):
        for key, value in list_golds[i].items():
            if key == 'name':
                print(value)

gold_filter(pirates)
