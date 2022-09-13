import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect("test.db", isolation_level=None)

c = conn.cursor()

c.execute(" \
    create table if not exists table1  \
    ( id integer primary key, name text, birthday text) \
    ")

c.execute(" \
    insert into table1 \
    values( 1, 'lee', '2000-01-01') \
    ")
