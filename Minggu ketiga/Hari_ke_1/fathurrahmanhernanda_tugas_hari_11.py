from mysql.connector import connect
from dotenv import dotenv_values

# Membuat koneksi database
params = {
    "db": dotenv_values("tugas10.env")
}

db_user = params['db']['root']
db_password = params['db']['bobotoh93']
db_host = params['db']['localhost']
db_port = params['db']['3306']

db = connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database='imdb_movie'
)

if db:
    print(db)
    print("Database berhasil terkoneksi")

cursor_db = db.cursor()

# Fungsi untuk menampilkan 5 direktur dengan jumlah film terbanyak dalam daftar
def most_maker_director():
    query = "SELECT director_name, COUNT(*) AS film_count FROM movies GROUP BY director_name ORDER BY film_count DESC LIMIT 5"
    cursor_db.execute(query)
    result = cursor_db.fetchall()

    if result:
        print("Top 5 Directors with the Most Films:")
        for i, row in enumerate(result, start=1):
            director_name = row[0]
            film_count = row[1]
            print(f"{i}. {director_name} - {film_count} films")
    else:
        print("No data found.")

# Fungsi untuk menampilkan 10 direktur dengan total jumlah pendapatan terbesar
def most_profitable_director():
    query = "SELECT director_name, SUM(gross) AS total_gross FROM movies GROUP BY director_name ORDER BY total_gross DESC LIMIT 10"
    cursor_db.execute(query)
    result = cursor_db.fetchall()

    if result:
        print("Top 10 Directors with the Highest Total Gross:")
        for i, row in enumerate(result, start=1):
            director_name = row[0]
            total_gross = row[1]
            print(f"{i}. {director_name} - {total_gross:.2f}")
    else:
        print("No data found.")

# Fungsi untuk menampilkan 15 film dengan pendapatan terbesar
def most_profitable_movie():
    query = "SELECT movie_title, gross FROM movies ORDER BY gross DESC LIMIT 15"
    cursor_db.execute(query)
    result = cursor_db.fetchall()

    if result:
        print("Top 15 Movies with the Highest Gross:")
        for i, row in enumerate(result, start=1):
            movie_title = row[0]
            gross = row[1]
            print(f"{i}. {movie_title} - {gross:.2f}")
    else:
        print("No data found.")

# Panggil fungsi-fungsi yang telah dibuat
most_maker_director()
most_profitable_director()
most_profitable_movie()
