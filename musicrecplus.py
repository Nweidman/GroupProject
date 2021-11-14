# Names: Matthew Angelakos, Nicholas Weidman, Winston Lee
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.


import data_manager  # all functions involing interaction with the database
import database_loader as db_load  # load_database and save_database functions
from sort import *  # sort functions


def enter_preferences(database, username):
    """Prompts the user to enter new liked artists, and replaces any previous preferences."""
    liked_artists = []
    artist = input("Enter an artist that you like ( Enter to finish ): ")
    while artist != "":
        liked_artists.append(artist)
        artist = input("Enter an artist that you like ( Enter to finish ): ")
    data_manager.update_database(database, [username, liked_artists])


def get_recommendations(database, username):
    """Prints recommended artists for the user based on their own preferences."""
    recommendations = data_manager.findRecommendations(database, username)
    sort(recommendations)
    if len(recommendations) <= 0:
        print("No recommendations available at this time.")
    else:
        for i in range(len(recommendations)):
            print(recommendations[i])


def show_most_popular(database):
    """Most popular aritst based on the example using a database"""
    mostPopular = data_manager.mostPopular(database)
    if len(mostPopular) == 0:
        print("Sorry, no artists found.")
    else:
        for artist in mostPopular:
            print(artist)


def how_most_popular(database):
    """how many people like the most popular artists from a database"""
    data_manager.howPopular(database)


def user_most_likes(database):
    """prints the user with the most liked artists, one per line and sorted if more than one"""
    data_manager.userMostLikes(database)


def delete_preferences(database, username):
    """Prints the current users preferences on the screen and removes a
    preference depending on the user's input"""
    count = 1
    string = "Which number would you like to remove? (Enter to cancel)\n"
    while count <= len(list(database[username])):
        string += (str(count) + ". " + list(database[username])[count - 1]) + "\n"
        count += 1
    delete = input(string)
    if delete.isnumeric() and int(delete) - 1 < len(database[username]) and int(delete) > 0:
        database[username] = database[username][0:int(delete) - 1] + database[username][int(delete):]
        print("Number " + str(delete) + " has been removed!\n")
    elif delete == "":
        print("Deletion Cancelled\n")
    else:
        print("Invalid choice!\n")


def show_preferences(database, username):
    """Prints the current users preferences on the screen."""
    count = 1
    string = "Here are your current preferences:\n"
    while count <= len(list(database[username])):
        string += (str(count) + ". " + list(database[username])[count - 1]) + "\n"
        count += 1
    print(string)


def main():
    """Main method for running the music recommender."""
    # Loading data and user
    menu = "Enter a letter to choose an option :\n e - Enter preferences\n r - Get recommendations\n p - Show most " \
           "popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n d - Delete " \
           "Preferences\n s - Show Preferences\n q - Save and " \
           "quit\n "
    filename = "musicrecplus.txt"
    database = db_load.load_database(filename)
    username = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private "
                     "): ")
    if username not in database:
        enter_preferences(database, username)

    # Menu
    print(menu)
    user_choice = input()
    while user_choice != "q":
        if user_choice == "e":
            enter_preferences(database, username)
        elif user_choice == "r":
            get_recommendations(database, username)
        elif user_choice == "p":
            show_most_popular(database)
        elif user_choice == "h":
            how_most_popular(database)
        elif user_choice == "m":
            user_most_likes(database)
        elif user_choice == "d":
            delete_preferences(database, username)
        elif user_choice == "s":
            show_preferences(database, username)
        else:
            print("Invalid choice!\n")
        print(menu)
        user_choice = input()

    # Save and quit
    db_load.save_database(database, filename)


if __name__ == "__main__":
    main()
