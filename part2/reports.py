import csv
# Report functions


def load_list(file_name, index):
    properties = []
    reader = open(file_name, "r")
    game_stats = csv.reader(reader, delimiter="\t")
    for row in game_stats:
        properties.append(row[index])
    reader.close()
    return properties

#   1


def get_most_played(file_name):
    titles = load_list(file_name, 0)
    copies = load_list(file_name, 1)
    copies = [float(x) for x in copies]
    most_copies_index = copies.index(max((copies)))
    return str(titles[most_copies_index])


def sum_sold(file_name):
    copies = load_list(file_name, 1)
    copies = [float(x) for x in copies]
    sum_of_copies = sum(copies)
    return sum_of_copies


def get_selling_avg(file_name):
    copies = load_list(file_name, 1)
    copies = [float(x) for x in copies]
    avg_sell = sum(copies) / len(copies)
    return avg_sell


def count_longest_title(file_name):
    titles = load_list(file_name, 0)
    count_title = [len(x) for x in titles]
    return max(count_title)


def get_date_avg(file_name):
    years = load_list(file_name, 2)
    years = [float(x) for x in years]
    avg_years = sum(years) / len(years)
    return round(avg_years)


def get_game(file_name, title):
    titles = load_list(file_name, 0)
    copies = load_list(file_name, 1)
    copies = [float(x) for x in copies]
    years = load_list(file_name, 2)
    years = [int(x) for x in years]
    genre = load_list(file_name, 3)
    publisher = load_list(file_name, 4)
    game_index = titles.index(title)
    properties = [titles[game_index], copies[game_index], years[game_index], genre[game_index], publisher[game_index]]
    return properties

def count_grouped_by_genre(file_name):
    genre=load_list(file_name,3)
    genres_dict={}
    for game in genre:
        if game in genres_dict.keys():
            genres_dict[game]+=1
        else:
            genres_dict[game]=1
    return genres_dict


stat = "game_stat.txt"
print(get_most_played(stat))
print(sum_sold(stat))
print(get_selling_avg(stat))
print(count_longest_title(stat))
print(get_date_avg(stat))
print(get_game(stat , "Minecraft"))
print(count_grouped_by_genre(stat))