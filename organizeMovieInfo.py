from movie import Movie


def add_movie(movie_info):
    """
    Saves all important data of the movie into class movie
    :param movie_info: the individual info for one movie
    :return: Returns a variable mov thats basically a movie class that holds all the movies info
    """
    mov = Movie(movie_info[0], movie_info[4:], movie_info[1], movie_info[3], movie_info[2])
    return mov


def make_list_of_all_movie_info():
    """
    Reads in the text file created by the movie scrubber, and puts all movie data into a usable list
    :return: Returns list of list where every nested list is a movie with all its relevant data
    """
    big_lst = []
    with open('movieInfo.txt') as f:
        for line in f:
            small_lst = []
            holder = ''
            for word in line:
                if word == "~":
                    small_lst.append(holder)
                    holder = ''
                else:
                    holder = holder + word
            big_lst.append(small_lst)
    return big_lst


def make_dic_of_movies():
    """
    :return: returns a dictionary where the movie name is the key and the movie saved into a class is the value
    """
    lst_of_movie_info = make_list_of_all_movie_info()
    dic_of_movies = {}
    for element in lst_of_movie_info:
        dic_of_movies[element[0]] = add_movie(element)

    return dic_of_movies
