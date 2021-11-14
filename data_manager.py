from sort import *


def update_database(database, preferences):
    """Assume database is a dictionary and preferences is a 2-element list.
    This method changes the preferences of the user given by preferences[0] using the liked artists specified by
    preferences[1]."""
    # Exception handling
    if type(database) != dict:
        raise Exception("database must be a dictionary!")
    elif len(preferences) != 2:
        raise Exception("preferences must be a key-value pair!")

    # Updating
    username, liked_artists = preferences[0], preferences[1]
    database[username] = liked_artists

    # Sorting
    sort(database[username])


def compareUsers(list_a, list_b):
    """Returns a tuple of the form (numMatches, difference). numMatches is the number of common elements in list_a
    and list_b, provided that list_b is not a subset of list_a. If list_b is a subset of list_a, numMathces is 0.
    difference is the list of elements in list_b that are not in list_a."""

    numMatches = 0
    difference = []
    i, j = 0, 0

    while i < len(list_a) and j < len(list_b):
        if list_a[i] == list_b[j]:
            numMatches += 1
            i += 1
            j += 1
        elif list_a[i] < list_b[j]:
            i += 1
        else:
            difference.append(list_b[j])
            j += 1

    if j < len(list_b):
        difference += list_b[j:]

    if difference:
        return numMatches, difference
    else:
        return 0, difference


def findRecommendations(database, username):
    """Returns a list of recommendations for the user 'username'. This is determined by finding the user with
    the most shared preferences with username that also has at least one liked artist not in username's preferences.
    Private mode users are not considered in this calculation."""
    maxMatches = 0
    recommendations = []
    for otherUser in database:
        if otherUser[-1] != "$":
            numMatches, difference = compareUsers(database[username], database[otherUser])
            if maxMatches <= numMatches:
                maxMatches, recommendations = numMatches, difference
        else:
            continue
    return recommendations


def userMostLikes(database):
    """prints the user with the most liked artists, one per line and sorted if more than one"""
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
    likeCount = {}
    for user in database:
        if user[-1] != '$':
            for artist in database[user]:
                if artist in likeCount:
                    likeCount[artist] += 1
                else:
                    likeCount[artist] = 1
    artistsSorted = sorted(likeCount, key=lambda artist: likeCount[artist])
    if len(artistsSorted) >= 3:
        return artistsSorted[:-4:-1]
    else:
        return artistsSorted


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


def mostPopular2(database):  # Basically same as the first but only prints the most popular artist and if there is a
    # tie print
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
