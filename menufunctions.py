from sort import sort  # import funny sort


def mostLiked(database):
    """returns the user with the most liked artists, one per line and sorted if more than one"""
    keys = list(database.keys())  # Gets a list of keys from the database
    ch = "$"
    mostLikedArtists = []
    biggestLength = 0
    itemIndex = 0
    Artists = list(database.items())  # Gets a list of key, item pair from the database
    for keyIndex in keys:  # For loop to iterate through all the keys in database
        if ch in keyIndex:  # If the user is private skip it
            mostLikedArtists = mostLikedArtists
            itemIndex += 1
        else:
            likedArtists = Artists[itemIndex]
            likedArtists = likedArtists[1]
            length = len(
                likedArtists)  # Get a list of the items at the current keyIndex from the database list and from
            # there get the length of said list
            itemIndex += 1
            if length > biggestLength:  # If the current length is bigger than the longest recorded length set the
                # biggest length to that and set current key(user) to the mostLiked artist list
                biggestLength = length
                mostLikedArtists = [keyIndex]
            elif length == biggestLength:  # If the current length is equal to the longest recorded length add the
                # current key(user) to the mostLiked artist List
                mostLikedArtists = mostLikedArtists + [keyIndex]
    sort(mostLikedArtists)  # Sort the mostLiked Artist list
    for i in mostLikedArtists:  # For each element of the mostLiked Artist List print out the artist
        print(i)


def mostPopular(database):
    """top 3 most popular aritsts using the pdf description from a database"""
    popularDB = {}
    itemIndex = 0
    ch = "$"
    keys = list(database.keys())  # same as above
    Artists = list(database.items())  # same as above
    for keyIndex in keys:  # If user is private skip
        if ch in keyIndex:
            itemIndex += 1
        else:
            popularArtists = Artists[itemIndex]  # same as above
            popularArtists = popularArtists[1]
            itemIndex += 1
            for listIndex in popularArtists:  # Set the popularDB to the artists and the amount of times they appear
                # in the normal db
                if listIndex in popularDB:
                    popularDB[listIndex] += 1
                else:
                    popularDB[listIndex] = 1
    mostPopularLikes = 0
    mostPopularArtist = ""
    secondMostPopular = 0
    secondMostPopularArtist = ""
    thirdMostPopular = 0
    thirdMostPopularArtist = ""  # Decleare the top 3 most popular aritsts and their numerical value
    keys = list(popularDB.keys())  # same as above
    Artists = list(popularDB.items())  # same as above
    ItemIndex = 0
    for itemIndex in Artists:
        howPopularLikes = list(itemIndex)
        print(howPopularLikes)
        howPopularKey = howPopularLikes[0]
        howPopularLikes = howPopularLikes[1]
        if howPopularLikes > mostPopularLikes:  # Sees if the current artists is more popular than the most popular
            # aritst if
            # so set the mostPopular Artists to that and if there is a current most popular artists set the 2nd most
            # popular artist to that
            if mostPopularArtist != "":
                if secondMostPopularArtist != "":
                    thirdMostPopularArtist = secondMostPopularArtist
                    thirdMostPopular = secondMostPopular
                secondMostPopularArtist = mostPopularArtist
                secondMostPopular = mostPopularLikes
            mostPopularLikes = howPopularLikes
            mostPopularArtist = howPopularKey
        elif howPopularLikes == mostPopularLikes:  # Same thing as above but with no 2nd most popular becoming
            # current most
            # popular and instead adding onto the currentMost Popular Artist
            mostPopularArtist = mostPopularArtist + ", " + howPopularKey
        elif howPopularLikes > secondMostPopular:  # Same thing but with 2ndMostPopular
            if secondMostPopularArtist != "":
                thirdMostPopularArtist = secondMostPopularArtist
                thirdMostPopular = secondMostPopular
            secondMostPopular = howPopularLikes
            secondMostPopularArtist = howPopularKey
        elif howPopularLikes == secondMostPopular:  # Same thing but with 2ndMostPopular
            secondMostPopularArtist = secondMostPopularArtist + ", " + howPopularKey
        elif howPopularLikes > thirdMostPopular:  # Same thing but with 3rdMostPopular
            thirdMostPopular = howPopularLikes
            thirdMostPopularArtist = howPopularKey
        elif howPopularLikes == thirdMostPopular:  # Same thing but with 3rdMostPopular
            thirdMostPopularArtist = thirdMostPopularArtist + ", " + howPopularKey
        print(mostPopularArtist)  # Print the stuff
        print(secondMostPopularArtist)
        print(thirdMostPopularArtist)
    print(mostPopularArtist)  # Print the stuff
    print(secondMostPopularArtist)
    print(thirdMostPopularArtist)


def howPopular(database):
    """how many people like the most popular artists from a database"""
    popularDB = {}
    itemIndex = 0
    ch = "$"
    keys = list(database.keys())
    Artists = list(database.items())
    for keyIndex in keys:
        if ch in keyIndex:
            itemIndex += 1
        else:
            popularArtists = Artists[itemIndex]
            popularArtists = popularArtists[1]
            itemIndex += 1
            for listIndex in popularArtists:
                if listIndex in popularDB:
                    popularDB[listIndex] += 1
                else:
                    popularDB[listIndex] = 1  # Same as above
    mostPopularLikes = 0
    mostPopularArtist = ""
    keys = list(popularDB.keys())
    Artists = list(popularDB.items())
    ItemIndex = 0  # same as above
    for itemIndex in Artists:
        howPopularLikes = list(itemIndex)
        howPopularKey = howPopularLikes[0]
        howPopularLikes = howPopularLikes[1]
        if howPopularLikes > mostPopularLikes:  # Same as above but instead with the numerical value
            mostPopularLikes = howPopularLikes
    if mostPopularLikes == 0:  # Print
        print("Sorry , no artists found .")
    else:
        print(mostPopularLikes)


def mostPopular2(
        database):  # Basically same as the first but only prints the most popular artist and if there is a tie print
    # them out one on each line steming from a list
    """Most popular aritst based on the example using a database"""
    popularDB = {}
    itemIndex = 0
    ch = "$"
    keys = list(database.keys())
    Artists = list(database.items())
    for keyIndex in keys:
        if ch in keyIndex:
            itemIndex += 1
        else:
            popularArtists = Artists[itemIndex]
            popularArtists = popularArtists[1]
            itemIndex += 1
            for listIndex in popularArtists:
                if listIndex in popularDB:
                    popularDB[listIndex] += 1
                else:
                    popularDB[listIndex] = 1
    mostPopularLikes = 0
    mostPopularArtist = []
    keys = list(popularDB.keys())
    Artists = list(popularDB.items())
    ItemIndex = 0
    for itemIndex in Artists:
        howPopularLikes = list(itemIndex)
        howPopularKey = howPopularLikes[0]
        howPopularLikes = howPopularLikes[1]
        if howPopularLikes > mostPopularLikes:
            mostPopularLikes = howPopularLikes
            mostPopularArtist = [howPopularKey]
        elif howPopularLikes == mostPopularLikes:
            mostPopularArtist = mostPopularArtist + [howPopularKey]
    for i in mostPopularArtist:
        print(i)
