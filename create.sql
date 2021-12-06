create table battlegrounds(
    id integer primary key,
    name varchar(255) NOT NULL
);

create table classes(
    id integer primary key,
    name varchar(255) NOT NULL
);

create table fractions(
    id integer primary key,
    name varchar(255) NOT NULL
);

create table game_sessions(
    id integer primary key,
    kills integer,
    honor integer,
    heal integer,
    death integer,
    damage integer
);

create table battleground_game_session(
    id integer primary key,
    game_session_id integer NOT NULL,
    battleground_id integer NOT NULL,
    FOREIGN KEY(game_session_id) REFERENCES game_sessions(id),
    FOREIGN KEY(battleground_id) REFERENCES battlegrounds(id)
);

create table fraction_game_session(
    id integer primary key,
    game_session_id integer NOT NULL,
    fraction_id integer NOT NULL,
    FOREIGN KEY(game_session_id) REFERENCES game_sessions(id),
    FOREIGN KEY(fraction_id) REFERENCES fractions(id)
);

create table class_game_session(
    id integer primary key,
    game_session_id integer NOT NULL,
    class_id integer NOT NULL,
    FOREIGN KEY(game_session_id) REFERENCES game_sessions(id),
    FOREIGN KEY(class_id) REFERENCES classes(id)
);


