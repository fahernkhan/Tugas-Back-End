from mysql.connector import connect
from dotenv import dotenv_values

# Membuat koneksi database
params = {
    "db": dotenv_values(".env")
}
print(params['db'].keys())
db_user = params['db']['MYSQL_USERNAME']
db_password = params['db']['MYSQL_PASSWORD']
db_host = params['db']['MYSQL_HOST']
db_port = params['db']['MYSQL_PORT']


db = connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database='imdb_movie'
)

if db:
    print(db)
    print("Database berhasil terkoneksi")

#Membuat Database
try: 
    cursor_db = db.cursor()
    cursor_db.execute("CREATE DATABASE IF NOT EXISTS schoole")
    cursor_db.close()
    db.close()
except Exception as e:
    print(f"Database Gagal dibuat: {e}")
