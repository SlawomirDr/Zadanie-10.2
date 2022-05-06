import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)





class TodosSQLite:

    def all(self, conn, table):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        return rows


    def get(self, conn, table, **query):
        cur = conn.cursor()
        qs = []
        values = ()
        for k, v in query.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)
        cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
        rows = cur.fetchall()
        return rows


    def create(self, conn, todo):
        sql = '''INSERT INTO projects(id, title, description, done)
             VALUES(?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, todo)
        conn.commit()
        return cur.lastrowid


    def update(self, conn, table, id, **kwargs):
        parameters = [f"{k} = ?" for k in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(v for v in kwargs.values())
        values += (id, )

        sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            print("OK")
        except sqlite3.OperationalError as e:
            print(e)


    def delete_where(self, conn, table, **kwargs):
        qs = []
        values = tuple()
        for k, v in kwargs.items():
            qs.append(f"{k}=?")
        values += (v,)
        q = " AND ".join(qs)

        sql = f'DELETE FROM {table} WHERE {q}'
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Deleted")

    def delete_all(conn, table):
        sql = f'DELETE FROM {table}'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Deleted")


if __name__ == "__main__":

   create_projects_sql = """
   -- projects table
   CREATE TABLE IF NOT EXISTS projects (
      id integer PRIMARY KEY,
      title text NOT NULL,
      description text,
      done text
   );
   """

   db_file = "database2.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_projects_sql)
       conn.close()

db_file = "database2.db"

todos = db_file