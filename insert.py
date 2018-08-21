
 
import psycopg2
from config import config
 
 
def insert_Book(vendor_name):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO Books(book_name)
             VALUES(%s) RETURNING book_id;"""
    conn = None
    book_id = None
    try:
        
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (vendor_name,))
        vendor_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return insert_id