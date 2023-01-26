import requests # Making web request
import json # Handling data (json)
from sys import argv
from urllib.parse import quote
ask = "no"
# The API key of omdbapi
API_KEY = "261001aa"

# The URL for movie search
URL = "http://www.omdbapi.com/?apikey="+API_KEY+"&t="
if len(argv) > 1:
    movie_name = " ".join(argv[1:])
    # encoded_movie_name = quote(movie_name.replace(" ", "+"))
    response = requests.get(URL+movie_name)
else:
# Ask for a movie name
    movie = input("Enter a movie name: ")
    response = requests.get(URL+movie)
# Find th movie

# Load results in json format
movies_data = response.json()
if 'Plot' in movies_data:
    story = movies_data['Plot']
    title = movies_data['Title']
    Released = movies_data['Released']
    Actors = movies_data['Actors']
    Poster = movies_data['Poster']
    Ratings = movies_data['Ratings']
    Genre = movies_data['Genre']
    Awards = movies_data['Awards']
    # Get the movie exist or not
else:
    print("[!] Movie Not found")
    quit()

# print(movies_data)
result = movies_data['Response']
if result == 'True':
    print(f"Title : {title}\nStory: {story}\nReleased Date: {Released}\nActors: {Actors}\nPoster: {Poster}\nGenre: {Genre}\nRatings: {Ratings}\nAwards: {Awards}")
    if ask == 'no':
        print("[!] ignoring favorate")
    else:
        favs = input("Adds to Favorate ?")
        if favs == "y" or 'yes' or 'Y':
            file = open('favors','a')
            file.write('Name: ' + movie_name + ' Desc: ' + story + '\n')
            file.close()
            print("Added Succefull")
else:
    print(result)
    print("No,Movie doesn't exist")
