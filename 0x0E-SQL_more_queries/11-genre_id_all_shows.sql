-- this script lists all shows contained in the database hbtn_0d_tvshows
SELECT tvs.title AS 'title', COALESCE(tvsg.genre_id) AS 'genre_id'
FROM tv_shows tvs LEFT JOIN tv_show_genres tvsg ON tvs.id = tvsg.show_id
ORDER BY tvs.title, tvsg.genre_id ASC;
