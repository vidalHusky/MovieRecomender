from organizeMovieInfo import make_dic_of_movies


class MovieLibrary:
    def __init__(self, genre='ALL', year=None, rating='ALL'):
        """
        All these values for the MovieLibrary object are the constraints for the movie library given by the user.
        :param genre: Designated Genre For Movie Library
        :param year: Designated Time Frame For Movie Library
        :param rating: Designated Rating For Movie Library
        """
        # A little confusing but basically the actual dictionary that contains all the movie objects
        self.movie_library = make_dic_of_movies()
        if year is None:
            self.year = [1900, 3000]
        # The constraints of the dictionary of movies
        self.genre = genre
        self.year = year
        self.rating = rating

    def change_year(self, year):
        """
        :param year: the new range of years wanted
        """
        self.year = year

    def change_rating(self, rating):
        """
        :param rating: The new rating constraint wanted for the dictionary
        :return:
        """
        self.rating = rating

    def suggest_based_on_genre(self):
        """
        Goes through the entire dictionary of movies and replaces that dictionary with an appended dictionary that
        only contains the movies wanted depending on the genre.
        :return: the library of all wanted movies, according to genre
        """
        if self.genre == 'ALL':
            return
        library_of_chosen_movies = {}
        for mov, mov_info in self.movie_library.items():
            if self.genre in str(mov_info.get_genre()):
                library_of_chosen_movies[mov] = mov_info
        self.movie_library = library_of_chosen_movies
        return

    def suggest_based_on_year(self):
        """
        Goes through the entire dictionary of movies and replaces that dictionary with an appended dictionary that
        only contains the movies wanted depending on the year time frame.
        :return: the library of all wanted movies according to year
        """
        library_of_chosen_movies = {}
        for mov, mov_info in self.movie_library.items():
            if self.year[0] <= mov_info.get_year() <= self.year[1]:
                library_of_chosen_movies[mov] = mov_info
        self.movie_library = library_of_chosen_movies
        return

    def suggest_based_on_rating(self):
        """
        Goes through the entire dictionary of movies and replaces that dictionary with an appended dictionary that
        only contains the movies wanted depending on the rating.
        :return: the library of all wanted movies according to their ratting
        """
        if self.rating == 'ALL':
            return
        if self.rating == 'G':
            library_of_chosen_movies = {}
            for mov, mov_info in self.movie_library.items():
                if 'PG' in mov_info.get_rating:
                    pass
                elif self.rating in mov_info.get_rating():
                    library_of_chosen_movies[mov] = mov_info
            self.movie_library = library_of_chosen_movies
            return
        if self.rating == 'PG':
            library_of_chosen_movies = {}
            for mov, mov_info in self.movie_library.items():
                if 'PG-13' in mov_info.get_rating():
                    pass
                elif self.rating in mov_info.get_rating():
                    library_of_chosen_movies[mov] = mov_info
            self.movie_library = library_of_chosen_movies
            return
        if self.rating == 'R':
            library_of_chosen_movies = {}
            for mov, mov_info in self.movie_library.items():
                if 'Not Rated' in mov_info.get_rating():
                    pass
                elif self.rating in mov_info.get_rating():
                    library_of_chosen_movies[mov] = mov_info
            self.movie_library = library_of_chosen_movies
            return
        else:
            library_of_chosen_movies = {}
            for mov, mov_info in self.movie_library.items():
                if self.rating in mov_info.get_rating():
                    library_of_chosen_movies[mov] = mov_info
            self.movie_library = library_of_chosen_movies
            return
