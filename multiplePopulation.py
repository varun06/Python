#Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

#What multiple of Romania's population is the population
#of China? Please print your result.
population_of_romania = countries[2][2]
population_of_china = countries[0][2]

print population_of_romania
print population_of_china

multiple_of_population = (population_of_romania/population_of_china)
print multiple_of_population



