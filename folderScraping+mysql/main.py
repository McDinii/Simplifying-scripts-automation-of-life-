import os
import mysql.connector
from mysql.connector import Error


def abcolute_path(path):
    return os.path.abspath(path)


def create_folder_arr(path):
    folder_arr = []
    for folder in os.listdir(path):
        folder_arr.append(folder)
    return folder_arr


def parser(data):
    club = data[0]
    players = data[1]
    info = []
    check_name = 0
    if check_name == 0:
        print("Parsing data: " + str(players[0]))
    for player in players:
        img = player
        player = player.split('_')  # string format: Leo_Messi_RW_Rare_Male_36_Argentina.png
        info.append({"Fullname": player[0] + " " + player[1], "Position": player[2], "Rarity": player[3], "Club": club,
                     "Age": 20,
                     "Sex": player[4], "Country": player[5].split('.')[0], "img": img})
    return info
def compose():
    pass

def get_list_of_players(path):
    folder_arr = create_folder_arr(path)
    list_of_players = []
    for folder in folder_arr:
        list_of_players += parser([folder, create_folder_arr(os.path.join(path, folder))])
    return list_of_players


def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def add_players_to_db(self, players):
    cursor = self.cursor()
    sql = "INSERT INTO SportyPoolWebTests.cardTemplates ( fullname, position, rarity, club, age, sex, country, path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = []
    for player in players:
        val.append(tuple(player.values()))
    cursor.executemany(sql, val)
    self.commit()
    print(cursor.rowcount, "was inserted.")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def compose_query(footballers,clubs):
    # info = []
    # for fotballer in footballers:
    #     img = fotballer[-1]
    #     club = fotballer[4]
    #     if (club in clubs):
    #         # string format: Leo_Messi_RW_Rare_Male_36_Argentina.png
    #         clubs[club] = info.append(f"{img}")
    #     else:
    #         clubs.update({club: [img]})
    # return info
    pass


if __name__ == '__main__':
    # parse data
    folder_with_clubs = "data"  # folder with clubs
    players_to_DB = get_list_of_players(folder_with_clubs)

    # work with DB
    host_name = "185.87.50.136"
    user_name = "SportyPoolUser"
    user_password = "chXFjuNSfT4DEQq8"
    connection = create_connection(host_name, user_name, user_password)
    add_players_to_db(connection, players_to_DB)
    # query = "SELECT * FROM SportyPoolWebTests.cardTemplates"
    # footballers =execute_read_query(connection, query)
    # clubs = {}
    # compose_query(footballers,clubs)
