class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def watched_movies(self):
        # Calculate gather list of movies that have been watched
        return list(filter(lambda movie: movie.watched, self.movies))
