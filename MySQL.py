import MySQLdb

host = "localhost"
user = "root"
password = "752301"
db = "escola"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):

    global C

    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()

def insert(values, tables, fields=None):

    global c, con

    query = "INSERT INTO " + tables
    if(fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()

values = ["DEFAULT, 'Evandro Diehl', '1950-09-23', 'Quinto dos Infernos, 15', 'Alegrete', 'RS', '12345678911'"]

def update(sets, table, where=None):

    global c,con

    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if (where):
        query = query + "WHERE" + where

    c.execute(query)
    con.commit()

def delete(table, where):

    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()

print(select("*","alunos)"))
