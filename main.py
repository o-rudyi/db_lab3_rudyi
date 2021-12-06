import psycopg2
import matplotlib.pyplot as plt

username = 'alex'
password = 'password'
database = 'world_of_warcraft'
host = 'localhost'
port = '5432'
query1 = []
query1.append('''
CREATE OR REPLACE VIEW alliance_on_battleground AS 
SELECT b.name as battleground, sum(case when f.name = 'Alliance' then 1 else 0 end) as alliance_players
 FROM game_sessions gs 
 INNER JOIN fraction_game_session fgs on gs.id = fgs.game_session_id 
 INNER JOIN battleground_game_session bgs on gs.id = bgs.game_session_id
 INNER JOIN fractions f on f.id = fgs.fraction_id 
 INNER JOIN battlegrounds b on b.id = bgs.battleground_id 
 GROUP BY b.name;

SELECT * FROM alliance_on_battleground;
''')
query1.append('''
CREATE OR REPLACE VIEW count_of_classes_on_bg AS
SELECT c.name as class, sum(case when cgs.id is NULL then 0 else 1 end) as number 
FROM classes c 
LEFT JOIN class_game_session cgs on c.id = cgs.class_id 
GROUP BY c.name;

SELECT * FROM number_of_characters_for_attributes;
''')

query1.append('''
CREATE OR REPLACE VIEW classes_kills_statistic AS
SELECT c.name as class, sum(case when cgs.id is NULL then 0 else gs.kills end)as number
 FROM classes c 
LEFT JOIN class_game_session cgs on c.id = cgs.class_id 
LEFT JOIN game_sessions gs on gs.id = cgs.game_session_id
 GROUP BY c.name

SELECT * FROM classes_kills_statistic;
''')

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor()


def __create_db():
    with open("create.sql", "r") as f:
        sql = f.read()
    cur.execute(sql)
    conn.commit()

__create_db()

def drop_db():
    with open("drop.sql", "r") as f:
        sql = f.read()
    cur.execute(sql)
    conn.commit()


def query_result(query_num: int):
    query = query1[query_num - 1]
    cur.execute(query)
    rows = cur.fetchall()
    return rows


def first_query_data():
    result = query_result(1)
    data = {
        'Battlegrounds': [i[0] for i in result],
        'Alliance Players': [i[1] for i in result],
    }
    return data


def second_query_data():
    result = query_result(2)
    data = {
        'Class': [i[0] for i in result],
        'Players': [i[1] for i in result],
    }
    return data


def third_query_data():
    result = query_result(3)
    data = {
        'Class': [i[0] for i in result],
        'Kills': [i[1] for i in result],
    }
    return data


plt.get_current_fig_manager().resize(1400, 600)
plt.show()

first_data = first_query_data()
second_data = second_query_data()
third_data = third_query_data()

data_battleground = first_data['Battlegrounds']
data_alliance_players = first_data['Alliance Players']

fig, ax = plt.subplots()

ax.bar(data_battleground, data_alliance_players)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

fig1, ax1 = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi=80)

data = second_data["Players"]
categories = second_data["Class"]

wedges, texts = ax1.pie(data,
                        textprops=dict(color="w"),
                        colors=plt.cm.Dark2.colors,
                        startangle=140)

ax1.legend(wedges, categories, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()

data_class = third_data['Class']
data_kills = third_data['Kills']

fig2, ax2 = plt.subplots()

ax2.bar(data_class, data_kills, color='red')

ax2.set_facecolor('seashell')
fig2.set_facecolor('floralwhite')
fig2.set_figwidth(12)
fig2.set_figheight(6)

plt.show()
