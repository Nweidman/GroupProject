from search_and_sort import *  # search and sort functions
import database_loader as db_load
import data_manager  #

menu = "Enter a letter to choose an option :\n e - Enter preferences\n r - Get recommendations\n p - Show most " \
       "popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n q - Save and quit\n"
filename = "musicrecplus.txt"


def enter_preferences(database, username):
    liked_artists = []
    artist = input("Enter an artist that you like ( Enter to finish ): ")
    while artist != "":
        liked_artists.append(artist)
        artist = input("Enter an artist that you like ( Enter to finish ): ")
    data_manager.update_database(database, [username, liked_artists])


def get_recommendations():
    pass


def show_most_popular():
    pass


def how_most_popular():
    pass


def user_most_likes():
    pass


def main():
    # Loading data and user
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
            get_recommendations()
        elif user_choice == "p":
            show_most_popular()
        elif user_choice == "h":
            how_most_popular()
        elif user_choice == "m":
            user_most_likes()
        else:
            print("Invalid choice!\n")

    # Save and quit
    db_load.save_database(database, filename)


if __name__ == "__main__":
    main()
