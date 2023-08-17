-- A script that lists all Comedy shows in the database hbtn_0d_tvshows
-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT s.title FROM tv_genres g
INNER JOIN tv_show_genres sg
ON sg.genre_id = g.id
INNER JOIN tv_shows s
ON s.id = sg.show_id
WHERE g.name = "Comedy" ORDER BY s.title;
