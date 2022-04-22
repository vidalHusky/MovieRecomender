from movie import Movie


def suggest_based_on_genre(genre, movie_library):
    lst_of_chosen_movies = []
    for mov in movie_library.values():
        if genre in str(mov.get_genre()):
            lst_of_chosen_movies.append(mov.__str__())
    return lst_of_chosen_movies


def suggest_based_on_year(year, movie_library):
    lst_of_chosen_movies = []
    for mov in movie_library.values():
        if year[0] <= mov.get_year() <= year[1]:
            lst_of_chosen_movies.append(mov.__str())
    return lst_of_chosen_movies


def suggest_based_on_rating(rating, movie_library):
    lst_of_chosen_movies = []
    for mov in movie_library.values():
        if rating in mov.get_rating():
            lst_of_chosen_movies.append(mov.__str())
    return lst_of_chosen_movies


def add_movie(movie_info):
    mov = Movie(movie_info[0], movie_info[4:], movie_info[1], movie_info[3], movie_info[2])
    return mov


def make_list_of_all_movie_info():
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
    lst_of_movie_info = make_list_of_all_movie_info()
    dic_of_movies = {}
    for element in lst_of_movie_info:
        dic_of_movies[element[0]] = add_movie(element)

    return dic_of_movies
