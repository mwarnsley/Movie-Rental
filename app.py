from movie import Movie
from user import User

user = User("Marcus")

my_movie = Movie("The Matrix", "Sci-Fi", False)

user.movies.append(my_movie)

print(user.watched_movies())
