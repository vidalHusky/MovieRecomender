class Movie:
    def __init__(self, title, genre, year, score, rating):
        """
        :param title: title of movie
        :param genre: genre of movie
        :param year:  year of movie
        :param score: user score of movie
        :param rating: rating of movie, ie PG, G, R, etc
        """
        self.title = title
        self.rating = rating
        self.score = score
        self.genre = genre
        self.year = year

    def get_title(self):
        """
        :return: Returns the title of the movie
        """
        return self.title

    def get_rating(self):
        """
        :return: Returns the rating of the movie
        """
        return self.rating

    def get_score(self):
        """
        :return: Returns the rating of the movie
        """
        return self.score

    def get_genre(self):
        """
        :return: Returns the genre of the movie
        """
        return self.genre

    def get_year(self):
        """
        :return: Returns the year of release of the movie
        """
        return int(self.year)

    def __str__(self):
        """
        :return: All the information of the movie concatenated into a nice line
        """
        genre_string = '/'.join(self.genre)
        return f'{self.title}, {self.year}, {self.rating}, {self.score}/10, {genre_string}'
