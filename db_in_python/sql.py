# Relational Operators
# There are several relational operators you can use:

# < less than
# <= less than or equal to
# > greater than
# >= greater than or equal to
# These are primarily used to compare numeric and date/time types.

# SELECT <columns> FROM <table> WHERE <column name> < <value>;
# SELECT <columns> FROM <table> WHERE <column name> <= <value>;
# SELECT <columns> FROM <table> WHERE <column name> > <value>;
# SELECT <columns> FROM <table> WHERE <column name> >= <value>;
# Examples:

# SELECT first_name, last_name FROM users WHERE date_of_birth < '1998-12-01';
# SELECT title AS "Book Title", author AS Author FROM books WHERE year_released <= 2015;
# SELECT name, description FROM products WHERE price > 9.99;
# SELECT title FROM movies WHERE release_year >= 2000;

# Searching Within a Set of Values
# SQL Used
# SELECT <columns> FROM <table> WHERE <column> IN (<value 1>, <value 2>, ...);
# Examples:

# SELECT name FROM islands WHERE id IN (4, 8, 15, 16, 23, 42);
# SELECT * FROM products WHERE category IN ("eBooks", "Books", "Comics");
# SELECT title FROM courses WHERE topic IN ("JavaScript", "Databases", "CSS");
# SELECT * FROM campaigns WHERE medium IN ("email", "blog", "ppc");
# To find all rows that are not in the set of values you can use NOT IN.

# SELECT <columns> FROM <table> WHERE <column>  NOT IN (<value 1>, <value 2>, ...);
# Examples:

# SELECT answer FROM answers WHERE id IN (7, 42);
# SELECT * FROM products WHERE category NOT IN ("Electronics");
# SELECT title FROM courses WHERE topic NOT IN ("SQL", "NoSQL");
# See all of the SQL used in SQL Basics in the SQL Basics Cheat Sheet.

# Have questions about this video? Start a discussion with the community and Treehouse staff

# Searching Within a Range of Values
# SQL Used
# SELECT <columns> FROM <table> WHERE <column> BETWEEN <lesser value> AND <greater value>;
# Examples:

# SELECT * FROM movies WHERE release_year BETWEEN 2000 AND 2010;
# SELECT name, description FROM products WHERE price BETWEEN 9.99 AND 19.99;
# SELECT name, appointment_date FROM appointments WHERE appointment_date BETWEEN "2015-01-01" AND "2015-01-07";


# Finding Data that Matches a Pattern
# SQL Used
# Placing the percent symbol (%) any where in a string in conjunction with the LIKE keyword will operate as a wildcard. Meaning it can be substituted by any number of characters, including zero!

# SELECT <columns> FROM <table> WHERE <column> LIKE <pattern>;
# Examples:

# SELECT title FROM books WHERE title LIKE "Harry Potter%Fire";
# SELECT title FROM movies WHERE title LIKE "Alien%";
# SELECT * FROM contacts WHERE first_name LIKE "%drew";
# SELECT * FROM books WHERE title LIKE "%Brief History%";
# PostgreSQL Specific Keywords
# LIKE in PostgreSQL is case-sensitive. To case-insensitive searches do ILIKE.

# SELECT * FROM contacts WHERE first_name ILIKE "%drew";


# Filtering Out or Finding Missing Information
IS NOT NUll