# Names: Matthew Angelakos, Nicholas Weidman, Winston Lee
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.


from sort import *  # sort functions
import database_loader as db_load  # load_database and save_database functions
import data_manager  # all functions involing interaction with the database


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


def show_most_popular():
    pass


def how_most_popular():
    pass


def user_most_likes():
    pass


def main():
    """Main method for running the music recommender."""
    # Loading data and user
    menu = "Enter a letter to choose an option :\n e - Enter preferences\n r - Get recommendations\n p - Show most " \
           "popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n q - Save and " \
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
            show_most_popular()
        elif user_choice == "h":
            how_most_popular()
        elif user_choice == "m":
            user_most_likes()
        else:
            print("Invalid choice!\n")
        print(menu)
        user_choice = input()

    # Save and quit
    db_load.save_database(database, filename)


if __name__ == "__main__":
    main()
