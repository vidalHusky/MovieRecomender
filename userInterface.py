from suggestMovie import MovieLibrary


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
    movieLibrary = MovieLibrary(genre)
    
    # Depending on user input changes constraints of the movieLibrary class to the desired year time frames
    if year == 1:
        movieLibrary.change_year([1900, 1950])
    elif year == 2:
        movieLibrary.change_year([1950, 1975])
    elif year == 3:
        movieLibrary.change_year([1975, 1990])
    elif year == 4:
        movieLibrary.change_year([1990, 2000])
    elif year == 5:
        movieLibrary.change_year([2000, 2005])
    elif year == 6:
        movieLibrary.change_year([2005, 2010])
    elif year == 7:
        movieLibrary.change_year([2010, 2015])
    elif year == 8:
        movieLibrary.change_year([2015, 3000])

    # Depending on user input changes constraints of the movieLibrary class to the desired rating of movie
    if rating == 1:
        movieLibrary.change_rating('G')
    elif rating == 2:
        movieLibrary.change_rating('PG')
    elif rating == 3:
        movieLibrary.change_rating('PG-13')
    elif rating == 4:
        movieLibrary.change_rating('R')

    # Does all the actual trimming of the dictionary to library of movies that is wanted by the user
    movieLibrary.suggest_based_on_genre()
    movieLibrary.suggest_based_on_year()
    movieLibrary.suggest_based_on_rating()


    # Display mechanism for the user

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
