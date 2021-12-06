INSERT INTO battlegrounds(id, name)
VALUES(1,'Warsong gulch'),
       (2,'Twin peaks'),
       (3,'Eye of the storm'),
       (4,'Strand of the ancients'),
       (5,'Temple of Kotmogu');

INSERT INTO fractions(id, name)
VALUES (1,'Alliance'),
       (2,'Horde');

INSERT INTO classes(id,name)
VALUES (1,'Shaman'),
       (2,'Druid'),
       (3,'Paladin'),
       (4,'Priest'),
       (5,'Rogue'),
       (6,'Death Knight'),
       (7,'Hunter'),
       (8,'Warlock'),
       (9,'Warrior'),
       (10,'Mage');

INSERT INTO game_sessions(
    id,
    kills ,
    honor ,
    heal ,
    death ,
    damage
)
VALUES (
        1,2,2000,2323,2,122222
       ),
       (
        2,3,500,2323323,12,2312
       ),
       (
        3,24,11000,2323,1,511051
       ),
       (
        4,0,10000,2999323,0,1
       ),
       (
        5,3,2200,123123,3,23231231
       ),
       (
        6,12,9002,23233,0,123123123
       ),
       (
        7,21,20000,2323000,23232,12222222
       ),
       (
        8,12,10231,22323,12,12232122
       ),
       (
        9,1,12000,2323322,1,100200
       ),
       (
        10,12,3400,2323,2,10000
       );


INSERT INTO battleground_game_session(
                                      id,
                                      game_session_id,
                                      battleground_id
                                      )
VALUES (
        1,1,1
       ),
       (
        2,2,2
       ),
       (
        3,3,3
       ),
       (
        4,4,4
       ),
       (
        5,5,5
       ),
       (
        6,6,1
       ),
       (
        7,7,2
       ),
       (
        8,8,3
       ),
       (
        9,9,4
       ),
       (
        10,10,5
       );

INSERT INTO class_game_session(
                                id,
                                game_session_id,
                                class_id
)
VALUES (
        1,1,1
       ),
       (
        2,2,2
       ),
       (
        3,3,3
       ),
       (
        4,4,3
       ),
       (
        5,5,5
       ),
       (
        6,6,6
       ),
       (
        7,7,6
       ),
       (
        8,8,6
       ),
       (
        9,9,9
       ),
       (
        10,10,10
       );

INSERT INTO fraction_game_session(
                                id,
                                game_session_id,
                                fraction_id
)
VALUES (
        1,1,1
       ),
       (
        2,2,1
       ),
       (
        3,3,1
       ),
       (
        4,4,1
       ),
       (
        5,5,2
       ),
       (
        6,6,1
       ),
       (
        7,7,2
       ),
       (
        8,8,1
       ),
       (
        9,9,2
       ),
       (
        10,10,2
       );