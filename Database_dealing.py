import psycopg2

conn = psycopg2.connect(host = "localhost",
                        user = "postgres" , 
                        dbname = "database1",
                        password = "postgreSQL",
                        port = 5432)

cur = conn.cursor()


 # Do data stuff
cur.execute(""" Create table demo 
             (id int primary key,
             name varchar(25) not null,
             course varchar (34))
            """)

cur.execute("""insert into demo (id , name , course) values(2 , 'Raghava','ISE');
""")
cur.execute("""Select * from demo""")

print(cur.fetchall())

conn.commit()


# close all connections
cur.close()
conn.close()