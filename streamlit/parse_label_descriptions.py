with open("map_data.txt", 'r') as f:
    lines = f.readlines()

# create a dictionary that maps variable names to their descriptions
# The descriptions are present as python comments in the original code

# A map of variable names to their descriptions - use this in the streamlit app.
variable_description_map = {}

for line in lines:
    if '#' not in line or ':' not in line:
        continue

    line = line.strip()
    description = line.split('#')[1].strip()
    variable = line.split(':')[0].strip()
    # remove quotes from the variable name
    variable = variable.replace("'", "")
    variable = variable.replace('"', '')
    variable = variable.replace(',', '')

    variable_description_map[variable] = description

print(len(variable_description_map))
