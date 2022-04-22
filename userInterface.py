from infoScrubber import make_dic_of_movies, suggest_based_on_year, suggest_based_on_genre, suggest_based_on_rating


while True:
    print('GREETINGS MOVIE GOER! Welcome to Javier Vidal\'s Fabulous Movie Recommender!')
    print('THE AVAILABLE MOVIE GENRE TO SEARCH FOR ARE:\n'
          'Action - Action - Adventure - Animation - Biography - Comedy - Crime',
          '\nDrama - Family - Fantasy - History - Horror - Musical - Music',
          '\nMystery - Romance - Sci-Fi - Sport - Thriller - War - Western')
    genre = input('WHAT GENRE OF MOVIE WOULD YOU LIKE TO WATCH?\n')
    year = input('WHAT ERA OF MOVIE WOULD YOU LIKE TO WATCH? ENTER THE NUMBER OPTION CORRESPONDING TO THE ERA\n'
                 '1. 1900->1950\n2. 1950->1975\n3. 1975->1990\n4. 1990->2000\n5. 2000->2005\n'
                 '6. 2005->2010\n7. 2010->2015\n8. 2015->Present\n9. If you don\'t care\n')
    rating = input('WHAT RATING WOULD YOU LIKE THE MOVIE TO HAVE?\n'
                   '1. G\n2. PG\n3. PG 13\n4. R\n6. Could Not Care Less\n')
    acceptable_movies = suggest_based_on_genre(genre, make_dic_of_movies())
    if year == 1:
        acceptable_movies = suggest_based_on_year([1900, 1950], acceptable_movies)
    elif year == 2:
        acceptable_movies = suggest_based_on_year([1950, 1975], acceptable_movies)
    elif year == 3:
        acceptable_movies = suggest_based_on_year([1975, 1990], acceptable_movies)
    elif year == 4:
        acceptable_movies = suggest_based_on_year([1990, 2000], acceptable_movies)
    elif year == 5:
        acceptable_movies = suggest_based_on_year([2000, 2005], acceptable_movies)
    elif year == 6:
        acceptable_movies = suggest_based_on_year([2005, 2010], acceptable_movies)
    elif year == 7:
        acceptable_movies = suggest_based_on_year([2010, 2015], acceptable_movies)
    elif year == 8:
        acceptable_movies = suggest_based_on_year([2015, 3000], acceptable_movies)

    if rating == 1:
        acceptable_movies = suggest_based_on_rating('G', acceptable_movies)
    elif rating == 2:
        acceptable_movies = suggest_based_on_rating('PG', acceptable_movies)
    elif rating == 3:
        acceptable_movies = suggest_based_on_rating('PG-13', acceptable_movies)
    elif rating == 4:
        acceptable_movies = suggest_based_on_rating('R', acceptable_movies)

    print()
    print('---------------------------------------------')
    for option in acceptable_movies:
        print(option)
        print()
        choice = int(input('Would You Like A Different Option? Enter 1 for Yes and 0 for No\n'))
        if choice:
            print()
            print('Next Option: ', end='')
        if choice == 0:
            print('Goodbye')
            quit()
    print('No More Choices, Goodbye')
    quit()