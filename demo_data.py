import sqlite3



def create_connection(db_file):
    """ create a database connection to the SQLite database"""

    conn = sqlite3.connect(db_file)
    return conn
    
 





def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    c = conn.cursor()
    c.execute(create_table_sql)




sql_table= '''	CREATE TABLE demo(
                s varchar(1) PRIMARY KEY,
                x int,
                y int
                );'''
#Define Columns
row_1="""INSERT INTO demo (s,x,y)
			VALUES ("g","3","9");"""

row_2="""INSERT INTO demo(s,x,y)
			VALUES ("v",5,7);"""

row_3="""INSERT INTO demo(s,x,y)
			VALUES ('f',8,7);"""


#Define Queries
Quer1="""SELECT COUNT(s) FROM demo;"""
Quer2="""SELECT COUNT(s) FROM demo WHERE x > 5 AND y > 5;"""
Quer3="""SELECT COUNT(DISTINCT y) FROM demo;"""



db='demo_data.sqlite3'
conn=create_connection(db)
create_table(conn,sql_table)
curs=conn.cursor()

#Create column 1
r1 = curs.execute(row_1)

#Create column 2
r2=curs.execute(row_2)

#Create column 3
r3=curs.execute(row_3)

#------

#Query 1
Q1=curs.execute(Quer1)

#Query 2
Q2=curs.execute(Quer2)

#Query 3
Q3=curs.execute(Quer3)

#------



print(Q1.fetchall())
print(Q2.fetchall())
print(Q3.fetchall())


conn.commit()






