"""
CP1404/CP5632 Assignment 1 - Albums Archive
Name: Shuntong Wu
Date started: 24/06/2026
"""

from operator import itemgetter


FILENAME = "albums.csv"
REQUIRED = "r"
COMPLETED = "c"
TITLE_INDEX = 0
ARTIST_INDEX = 1
YEAR_INDEX = 2
STATUS_INDEX = 3
MENU = """Menu:
D - Display all albums
R - Recommend a random album
A - Add a new album
M - Mark an album as completed
Q - Quit"""


def main():
    """Run the Albums Archive program."""
    print("Albums Archive 1.0 - by Shuntong Wu")
    albums = load_albums(FILENAME)
    print("{} albums loaded from {}".format(len(albums), FILENAME))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            display_albums(albums)
        elif choice == "R":
            print("Recommendation feature coming soon.")
        elif choice == "A":
            print("Add album feature coming soon.")
        elif choice == "M":
            print("Complete album feature coming soon.")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_albums(albums, FILENAME)
    print("{} albums saved to {}".format(len(albums), FILENAME))
    print("Have a nice day :)")


def load_albums(filename):
    """Load albums from CSV file into a list of lists."""
    albums = []
    try:
        input_file = open(filename, "r")
        for line in input_file:
            album_data = line.strip().split(",")
            if len(album_data) == 4:
                album_data[YEAR_INDEX] = int(album_data[YEAR_INDEX])
                albums.append(album_data)
        input_file.close()
    except FileNotFoundError:
        print("Error, {} not found!".format(filename))
    return albums


def save_albums(albums, filename):
    """Save albums from a list of lists to CSV file."""
    output_file = open(filename, "w")
    for album in albums:
        album_data = [
            album[TITLE_INDEX],
            album[ARTIST_INDEX],
            str(album[YEAR_INDEX]),
            album[STATUS_INDEX],
        ]
        output_file.write(",".join(album_data) + "\n")
    output_file.close()


def display_albums(albums):
    """Display albums sorted by status and year."""
    if len(albums) == 0:
        print("No albums!")
        return
    sort_albums(albums)
    title_width = find_longest_field_length(albums, TITLE_INDEX)
    artist_width = find_longest_field_length(albums, ARTIST_INDEX)
    number_width = len(str(len(albums)))
    number_of_required_albums = count_required_albums(albums)
    for i, album in enumerate(albums, 1):
        marker = " "
        if album[STATUS_INDEX] == REQUIRED:
            marker = "*"
        print("{}{}. {:{}} by {:{}} {}".format(
            marker,
            i,
            album[TITLE_INDEX],
            title_width,
            album[ARTIST_INDEX],
            artist_width,
            album[YEAR_INDEX],
        ))
    print("{} albums in archive. You still want to listen to {} albums.".format(
        len(albums), number_of_required_albums))


def sort_albums(albums):
    """Sort albums by required/completed status and then by year."""
    albums.sort(key=itemgetter(YEAR_INDEX))
    albums.sort(key=itemgetter(STATUS_INDEX), reverse=True)


def find_longest_field_length(albums, field_index):
    """Find the length of the longest field in the album list."""
    longest_length = 0
    for album in albums:
        if len(album[field_index]) > longest_length:
            longest_length = len(album[field_index])
    return longest_length


def count_required_albums(albums):
    """Count the number of required albums."""
    number_of_required_albums = 0
    for album in albums:
        if album[STATUS_INDEX] == REQUIRED:
            number_of_required_albums += 1
    return number_of_required_albums


main()
