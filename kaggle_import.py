import psycopg2

username = 'alex'
password = 'password'
database = 'world_of_warcraft'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database)
cursor = conn.cursor()

tables = {
    "battlegrounds(id, name)": "/Users/alex/PycharmProjects/databases/import/battlegrounds.csv",
    "fractions(id, name)": "/Users/alex/PycharmProjects/databases/import/fractions.csv",
    "classes(id,name)": "/Users/alex/PycharmProjects/databases/import/classes.csv",
    "game_sessions(id,kills ,honor ,heal ,death ,damage)":
        "/Users/alex/PycharmProjects/databases/import/game_sessions.csv",
    "battleground_game_session(id,game_session_id,battleground_id)":
        "/Users/alex/PycharmProjects/databases/import/battleground_game_session.csv",
    "class_game_session(id,game_session_id,class_id)":
        "/Users/alex/PycharmProjects/databases/import/class_game_session.csv",
    "fraction_game_session(id,game_session_id, fraction_id)":
        "/Users/alex/PycharmProjects/databases/import/fraction_game_session.csv",

}

import_table_from_csv_query = "COPY {} FROM '{}' DELIMITER ',' CSV HEADER;"

with conn:
    cur = conn.cursor()

    for table, import_file in tables.items():
        cur.execute(import_table_from_csv_query.format(table, import_file))
        cur.execute(f"SELECT * FROM {table.split('(')[0]}")
