from bs4 import BeautifulSoup
import requests


def unpack_data():
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    response = requests.get(url)
    text = response.text
    data = BeautifulSoup(text, 'html.parser')

    lst_of_movie_tickets = []
    # Gets all url tickets for all top 250 imdb movies
    for x in range(1, 1250):  # 'Should be 1250
        table = data.find_all('td')[x]
        url = table.find_all('a', href=True)  # 'href=True -> Gets the url ticket for each individual website
        for url in url:
            if url.string:
                #print(url.string)
                lst_of_movie_tickets.append(get_all_info(url['href'], url.text))
    return lst_of_movie_tickets


def get_all_info(link, name):
    genre_set = {'Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary',
                 'Drama', 'Family', 'Fantasy', 'Film Noir', 'Game Show', 'History', 'Horror', 'Musical', 'Music',
                 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller',
                 'War', 'Western'}

    response1 = requests.get('https://www.imdb.com' + link)
    text1 = response1.text
    data1 = BeautifulSoup(text1, 'html.parser')
    table1 = data1.find_all('a')

    counter = 0
    lst_of_info = [name]
    for genre in table1:
        counter += 1
        #Year = 50, Rating = 51, Score = 52, Genre = 62 till not b/c movie can be placed in more than 1 genre, max is 3
        if 50 <= counter <= 51:
            lst_of_info.append(genre.text)
        elif counter == 52:
            lst_of_info.append(genre.text[0:3])
        elif 62 <= counter <= 64 and genre.text in genre_set:
            lst_of_info.append(genre.text)
        elif counter > 64:
            break

    return lst_of_info


def create_text_file(lst_of_movie_info):
    with open('movieInfo.txt', 'w') as f:
        for i in lst_of_movie_info:
            for j in i:
                f.write(j+' ~ ')
            f.write('\n')


lst_of_movies = unpack_data()
create_text_file(lst_of_movies)

