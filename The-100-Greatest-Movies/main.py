from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
best_movies_of_all_time = response.text

soup = BeautifulSoup(best_movies_of_all_time, "html.parser")
# print(soup.prettify())

# movie_title = soup.find(name="h3")

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
movie_titles = [title.getText() for title in all_movies]

movies = movie_titles[::-1]

# for n in range(len(movie_titles)-1, -1, -1)
#     print(movie_titles[n])

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")