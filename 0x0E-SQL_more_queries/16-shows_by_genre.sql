-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT s.title, g.name FROM tv_genres g
INNER JOIN tv_show_genres sg
ON sg.genre_id = g.id
RIGHT OUTER JOIN tv_shows s
ON s.id = sg.show_id
ORDER BY s.title, g.name;
