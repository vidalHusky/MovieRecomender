class Movie:
    def __init__(self, title, genre, year, score, rating):
        self.title = title
        self.rating = rating
        self.score = score
        self.genre = genre
        self.year = year

    def get_title(self):
        return self.title

    def get_rating(self):
        return self.rating

    def get_score(self):
        return self.score

    def get_genre(self):
        return self.genre

    def get_year(self):
        return int(self.year)

    def __str__(self):
        genre_string = '/'.join(self.genre)
        return f'{self.title}, {self.year}, {self.rating}, {self.score}/10, {genre_string}'
