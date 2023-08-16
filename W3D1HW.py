
# 1) Filter out all of the empty strings from the list below

#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def filter_empty_strings(lst):
    return [place for place in lst if place.strip() != ""]

#places = [" ", "Argentina", " ", "San Diego", "", "  ", "", "Boston", "New York"]
filtered_places = filter_empty_strings(places)
print(filtered_places)


# 2) Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"

#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda author: author.split()[-1].lower()) #doesnt work without making everything lower case

print(author)

# 3) Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]


converted_places = list(map(lambda place: (place[0], (1.8) * place[1] + 32), places)) #change to multiplacation cause divison sucks

print(converted_places)



# 4) Create a generator function that individually returns each movie genre back from the list

genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]

def genre_generator(genres):
    for g in genres:
        yield g


genre2= genre_generator(genres)

for genre in range(len(genres)):
    genre = next(genre2)
    print(genre)  #why is my code spitting out all genres?


