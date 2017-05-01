from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        # Gather the list of movies that are NOT equal to the one you want to delete
        return list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        # Gather list of movies that have been watched
        return list(filter(lambda movie: movie.watched, self.movies))
