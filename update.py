import psycopg2
from config import config
 def update_Books(book_id, book_name):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE Books
                SET book_name = %s
                WHERE book_id = %s"""
    conn = None
    updated_rows = 0
    try:
        
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (book_name, book_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return updated_rows
