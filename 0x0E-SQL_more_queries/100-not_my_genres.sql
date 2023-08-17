-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- List all genres not linked to the show Dexter
SELECT name FROM tv_genres
WHERE name NOT IN (
    SELECT g.name FROM tv_shows s
    INNER JOIN tv_show_genres sg ON
    sg.show_id = s.id
    INNER JOIN tv_genres g
    ON g.id = sg.genre_id
    WHERE s.title = "Dexter"
) ORDER BY name;
