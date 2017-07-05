
# Report functions
# How many games are in the file?
# Expected name of the function: count_games(file_name)
# Expected output of the function: a number


def count_games(file_name):
    with open(file_name, 'r') as file:
        game_list = []
        for line in file:
            game_list.append(line)
        num_of_games = (len(game_list))
        return num_of_games


# Is there a game from a given year?
# Expected name of the function: decide(file_name, year)
# Expected output of the function: boolean value


def decide(file_name, year):
    with open(file_name, 'r') as file:
        game_list = []
        for row in file:
            game_list.append(row)
            game_list_string = ''.join(str(element) for element in game_list)
            game_list_string_split = game_list_string.split()
        if str(year) in game_list_string:
            return True
        if str(year) not in game_list_string:
            return False

# Which was the latest game?
# Expected name of the function: get_latest(file_name)
# Expected output of the function: the title of the latest game as a string
# Other expectation: if there is more than one, then return the first from the file


def get_latest(file_name):
    game_list = []
    year_list = []
    latest_year = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.split('\t'))
        for title, sold, year, genre, publisher in game_list:
            year_list.append(int(year))
            year_list.sort(reverse=True)
            latest_year = str(year_list[0])
        for title, sold, year, genre, publisher in game_list:
            if latest_year == year:
                return title


# How many games do we have by genre?
# Expected name of the function: count_by_genre(file_name, genre)
# Expected output of the function: a number

def count_by_genre(file_name, genree):
    game_list = []
    genre_list = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.split('\t'))
        for title, sold, year, genre, publisher in game_list:
            genre_list.append(genre)
        print(genre)
        return genre_list.count(genree)

print (count_by_genre("game_stat.txt","RPG"))