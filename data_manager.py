from search_and_sort import *


def update_database(database, preferences):
    # Exception handling
    if type(database) != dict:
        raise Exception("database must be a dictionary!")
    elif len(preferences) != 2:
        raise Exception("preferences must be a key-value pair!")

    # Updating
    username, liked_artists = preferences[0], preferences[1]
    if username not in database:
        database[username] = liked_artists
    else:
        database[username].append(liked_artists)

    # Sorting
    sort(database[username])
    sort(database)


def numMatchesNoSubset(listA, listB):
    isSubset = True
    count = 0
    for a in listA:
        if a in listB:
            count += 1
        else:
            isSubset = False
    if not isSubset:
        return count
    else:
        return 0
