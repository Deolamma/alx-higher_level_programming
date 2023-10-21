-- Selecting and counting occurrences of a record in another table
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.genre_id > 0 OR tv_show_genres.genre_id IS NOT NULL
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
