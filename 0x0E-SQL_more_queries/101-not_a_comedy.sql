-- A script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title FROM tv_shows
WHERE title NOT IN (
    SELECT s.title FROM tv_genres g
    INNER JOIN tv_show_genres sg
    ON sg.genre_id = g.id
    INNER JOIN tv_shows s
    ON s.id = sg.show_id
    WHERE g.name = "Comedy" ORDER BY s.title
) ORDER BY title;
