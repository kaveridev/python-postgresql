import psycopg2
from config import config
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE Books (
            book_id SERIAL PRIMARY KEY,
            book_name VARCHAR(255) NOT NULL,
        )
        """,
        """ CREATE TABLE Author (
                book_id SERIAL PRIMARY KEY,
                author_name VARCHAR(255) NOT NULL
                )
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
            cur.close()
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
