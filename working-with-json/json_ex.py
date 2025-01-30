import json

def compute_average_mass(a_list_of_dicts, a_key_string):
    total_mass = 0.
    for i in range(len(a_list_of_dicts)):
        total_mass += float(a_list_of_dicts[i][a_key_string])
    return (total_mass / len(a_list_of_dicts))

def class_number(type, number):
    count_type = {}
    for item in type:
        if number in item:
            value = item[number]
            if value:
                count_type[value] = count_type.get(value, 0) + 1
    return(count_type)

def check_hemisphere(latitude: float, longitude: float) -> str: #type hints
    location = ''
    if (latitude > 0):
        location = 'Northern'
    else:
        location = 'Southern'
    if (longitude > 0):
        location = f'{location} & Eastern'
    else:
        location = f'{location} & Western'
    return(location)

with open ('Meteorite_Landings.json', 'r') as file:
    ml_data = json.load(file)

print(f"average mass: {compute_average_mass(ml_data['meteorite_landings'], 'mass (g)')}")
print(class_number(ml_data['meteorite_landings'], 'recclass'))

for row in ml_data['meteorite_landings']:
    print(check_hemisphere(float(row['reclat']), float(row['reclong'])))
