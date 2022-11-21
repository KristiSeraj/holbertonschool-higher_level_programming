# SQL More queries

- [0-privileges.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/0-privileges.sql) - SQL script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on localhost server

- [1-create_user.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/1-create_user.sql) - SQL script that creates the MySQL server user `user_0d_1`

- [10-genre_id_by_show.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/10-genre_id_by_show.sql) - SQL script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`

- [100-not_my_genres.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/100-not_my_genres.sql) - SQL script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter` in ascending order by the genre name

- [101-not_a_comedy.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/101-not_a_comedy.sql) - SQL script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows` in ascending order by the show title

- [102-rating_shows.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/102-rating_shows.sql) - SQL script that lists all shows from `hbtn_0d_tvshows_rate` in descending order by their rating

- [103-rating_genres.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/103-rating_genres.sql) - SQL script that lists all genres in the database `hbtn_0d_tvshows_rate` in descending order by their rating

- [11-genre_id_all_shows.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/11-genre_id_all_shows.sql) - SQL script that lists all shows contained in `hbtn_0d_tvshows` in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`

- [12-no_genre.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/12-no_genre.sql) - SQL script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`

- [13-count_shows_by_genre.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/13-count_shows_by_genre.sql) - SQL script that lists all genres contained in `hbtn_0d_tvshows` and displays the number of shows linked to each in descending order by the number of shows linked

- [14-my_genres.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/14-my_genres.sql) - SQL script that uses `hbtn_0d_tvshows` to list all genres of the show Dexter in ascending order by the genre name

- [15-comedy_only.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/15-comedy_only.sql) - SQL script that lists all Comedy shows in `hbtn_0d_tvshows` in asceding order by the show title

- [16-shows_by_genre.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/16-shows_by_genre.sql) - SQL script that lists all shows and all genres linked to that show from the database `hbtn_0d_tvshows` in ascending order by the show title and genre name

- [2-create_read_user.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/2-create_read_user.sql) - SQL script that creates the database `hbtn_0d_2` and the user `user_0d_2`

- [3-force_name.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/3-force_name.sql) - SQL script that creates the table `force_name` on MySQL server with
    - `id`: int
    - `name`: varchar(256) not null

- [4-never_empty.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/4-never_empty.sql) - SQL script that creates the table `id_not_null` on MySQL server with
    - `id`: int with default value `1`
    - `name`: varchar(256)

- [5-unique_id.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/5-unique_id.sql) - SQL script that creates the table `unique_id` on MySQL server with
    - `id`: int with default value `1`, unique
    - `name`: varchar(256)

- [6-states.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/6-states.sql) - SQL script that creates the database `hbtn_0d_usa` and the table `states` on MySQL server with
    - `id`: int, unique, not null, primary key
    - `name`: varchar(256), not null

- [7-cities.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/7-cities.sql) - SQL script that creates the database `hbtn_0d_usa` and the table `cities` on MySQL server with
    - `id`: int, unique, auto generated, not null, primary key
    - `state_id`: int, not null, foreign key (reference to `id` of the `states` table)
    - `name`: varchar(256), not null

- [8-cities_of_california_subquery.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql) - SQL script that lists all the cities of California that can be found in the database `hbtn_0d_usa` in ascending order by `cities.id`

- [9-cities_by_state_join.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/9-cities_by_state_join.sql) - SQL script that lists all the cities contained in the database `hbtn_0d_usa` in ascending order by `cities.id`
