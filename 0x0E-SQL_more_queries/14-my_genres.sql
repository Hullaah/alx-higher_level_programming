-- A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- Lists all genres of the show Dexter
SELECT g.name FROM tv_shows s
INNER JOIN tv_show_genres sg ON
sg.show_id = s.id
INNER JOIN tv_genres g
ON g.id = sg.genre_id
WHERE s.title = "Dexter" ORDER BY g.name;
