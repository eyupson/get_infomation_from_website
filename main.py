import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(URL)
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")

titles=soup.find_all(name="h3",class_="title")
movie_title=[title.getText() for title in titles] 
movies=movie_title[::-1]

with open("movies.txt",mode="w",errors="ignore") as file:
    for movie in movies:
        file.write(f"{movie}\n")


