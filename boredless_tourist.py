# Name: Salman Ahmed
# Date: 05/21/2025

# Course: Computer Science Career Path
# Language: Python 3
# Project: The Boredless Tourist

#This project is a simple travel recommendation system that suggests attractions based on the traveler's interests and destination.
#The project uses lists and functions to manage destinations and attractions, and to find suitable recommendations for travelers.
#The project is designed to be simple and easy to understand, making it a good starting point for beginners in Python programming.

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  for place in destinations:
    if place == destination:
      return destinations.index(place)
  
#print(get_destination_index("Los Angeles, USA"))

#print(get_destination_index("Paris, France"))

#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

attractions = [[] for destination in destinations]
#print(attractions)

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
#print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_name = traveler[0]
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]

  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interests_string = "Hi " + traveler_name + ", we think you'll like these places around " + traveler_destination + ": "

  for attraction in traveler_attractions:
    if attraction != traveler_attractions[-1]:
      interests_string += attraction + ", "
    else:
      interests_string += attraction + "."
  
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
#print(smills_france)

