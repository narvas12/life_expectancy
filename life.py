"""
By Ezechukwu Emmanuel
"""
'''
Extra Creativity: I as able to Identify the year and country that has the largest drop from one year to the next.
'''
# Read the dataset
dataset = []
filename = 'life-expectancy.csv'


with open(filename, 'r') as file:
    for line_count, line in enumerate(file):
        line = line.strip()
        if line_count == 0:  # Skip the first line
            continue
        if line:
            data = line.split(',')
            country = data[0]
            year = int(data[2])
            life_expectancy = float(data[3])
            dataset.append({'country': country, 'year': year,
                           'life_expectancy': life_expectancy})

# Find the year and country with the lowest life expectancy
lowest_life_exp = dataset[0]
for data in dataset:
    if data['life_expectancy'] < lowest_life_exp['life_expectancy']:
        lowest_life_exp = data
print(f"The lowest life expectancy: {lowest_life_exp}")

# Find the year and country with the highest life expectancy
highest_life_exp = dataset[0]
for data in dataset:
    if data['life_expectancy'] > highest_life_exp['life_expectancy']:
        highest_life_exp = data
print("The highest life expectancy:".format(highest_life_exp))


lowest_year = lowest_life_exp['year']
lowest_country = lowest_life_exp['country']
highest_year = highest_life_exp['year']
highest_country = highest_life_exp['country']
print(f"The year and country with the lowest life expectancy: {lowest_country}, {lowest_year}")
print(f"The year and country with the highest life expectancy: {highest_country}", {highest_year})


# Allow the user to input a year
year_of_interest = int(input("Enter the year of interest: "))

# Calculate the average life expectancy for the given year
total_life_exp = 0
count = 0

for data in dataset:
    if data['year'] == year_of_interest:
        total_life_exp += data['life_expectancy']
        count += 1

if count > 0:
    average_life_exp = total_life_exp / count
    print("The average life expectancy for the Year",
        year_of_interest, ":", average_life_exp)

    # Find the country with the minimum and maximum life expectancies for the given year
    """min_country and max_country are variables used to store the country associated with the minimum and maximum life expectancy values, respectively. They are initially set to None to indicate that they haven't been assigned any specific country yet."""
    min_country = None
    max_country = None
    min_life_exp = float('inf')
    max_life_exp = float('-inf')

    for data in dataset:
        if data['year'] == year_of_interest:
            if data['life_expectancy'] < min_life_exp:
                min_life_exp = data['life_expectancy']
                min_country = data['country']
            if data['life_expectancy'] > max_life_exp:
                max_life_exp = data['life_expectancy']
                max_country = data['country']

    print("The country with the minimum life expectancy for",
        year_of_interest, ":", min_country)
    print("The country with the maximum life expectancy for",
        year_of_interest, ":", max_country)
else:
    print("No data available for the given year.")


# Initialize the largest drop variable
largest_drop = 0
drop_year = ''
drop_country = ''

# Iterate over the dataset starting from the second entry to sskip the first line of strings 
for i in range(1, len(dataset)):
    current_data = dataset[i]
    previous_data = dataset[i - 1]

    current_life_exp = current_data['life_expectancy']
    previous_life_exp = previous_data['life_expectancy']

    drop = previous_life_exp - current_life_exp

    if drop > largest_drop:
        largest_drop = drop
        drop_year = current_data['year']
        drop_country = current_data['country']

# Print the year and country with the largest drop
print("Year with the largest drop:", drop_year)
print("Country with the largest drop:", drop_country)
