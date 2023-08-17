-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT g.name, SUM(sr.rate) rating FROM tv_show_genres sg
INNER JOIN tv_show_ratings sr
ON sr.show_id = sg.show_id
INNER JOIN tv_genres g
ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY rating DESC;
