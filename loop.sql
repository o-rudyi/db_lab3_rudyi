DO
$do$
BEGIN
   FOR i IN 1..10 LOOP
      INSERT INTO class_game_session
         (id,game_session_id,class_id)
      SELECT i, i, i
      ON CONFLICT DO NOTHING;
   END LOOP;
END
$do$;
