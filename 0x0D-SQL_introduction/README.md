# SQL Introduction

- [0-list_databases.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/0-list_databases.sql) - Script that lists all databases of MySQL server

- [1-create_database_if_missing.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/1-create_database_if_missing.sql) - Script that creates the database `hbtn_0c_0` in MySQL server
  - If the database `hbtn_0c_0` already exists, script should not fail

- [10-top_score.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/10-top_score.sql) - Script that lists all records of the table `second_table` of the database `hbtn_0c_0` in MySQL server.
  - Results displays both the score and the name
  - Records should be ordered by score (top first)

- [100-move_to_utf8.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/100-move_to_utf8.sql) - Script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in MySQL server.
  - Converts all of the following to UTF8:
    - Database `hbtn_0c_0`
    - Table `first_table`
    - Field `name` in `first_table`


- [101-avg_temperatures.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/101-avg_temperatures.sql) - Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

- [102-top_city.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/102-top_city.sql) - Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

- [103-max_state.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/103-max_state.sql) - Script that displays the max temperature of each state (ordered by State name).

- [11-best_score.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/11-best_score.sql) - Script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in MySQL server.
  - Results displays both the score and the name
  - Records should be ordered by score (top first)

- [12-no_cheating.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/12-no_cheating.sql) - Script that updates the score of Bob to `10` in the table `second_table`

- [13-change_class.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/13-change_class.sql) - Script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in MySQL server.

- [14-average.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/14-average.sql) - Script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in MySQL server.

- [15-groups.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/15-groups.sql) - Script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in MySQL server.
  - The result displays:
    - the `score`
    - the number of records for this `score` with the label `number`
  - The list is sorted by the number of records (descending)

- [16-no_link.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/16-no_link.sql) - Script that lists all records of the table `second_table` of the database `hbtn_0c_0` in MySQL server.
- Doesn’t list rows without a `name` value
- Results displays the score and the name
- Records are listed by descending score

- [2-remove_databases.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/2-remove_database.sql) - Script that deletes the database `hbtn_0c_0` in MySQL server
  - If the database `hbtn_0c_0` already exists, script should not fail

- [3-list_tables.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/3-list_tables.sql) - Script that lists all the tables of a database in MySQL server

- [4-first_table.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/4-first_table.sql) - Script that creates a table called `first_table` in the current database in MySQL server
  - `first_table` description:
    - `id` INT
    - `name` VARCHAR(256)
  - If the table `first_table` already exists, script should not fail

- [5-full_table.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/5-full_table.sql) - Script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in MySQL server.

- [6-list_values.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/6-list_values.sql) - Script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in MySQL server.

- [7-insert_values.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/7-insert_value.sql) - Script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in MySQL server.
  - New row:
    - `id` = `89`
    - `name` = `Best School`

- [8-count_89.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/8-count_89.sql) - Script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in MySQL server

- [9-full_creation.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/9-full_creation.sql) - Script that creates a table `second_table` in the database `hbtn_0c_0` in MySQL server and add multiples rows.
  - `second_table` description:
    - `id` INT
    - `name` VARCHAR(256)
    - `score` INT
  - If the table `second_table` already exists, script should not fail
  - Script creates these records:
    - `id` = 1, `name` = “John”, `score` = 10
    - `id` = 2, `name` = “Alex”, `score` = 3
    - `id` = 3, `name` = “Bob”, `score` = 14
    - `id` = 4, `name` = “George”, `score` = 8

- [temperatures.sql](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/temperatures.sql) - Temperature table
