from sort import *


def update_database(database, preferences):
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
