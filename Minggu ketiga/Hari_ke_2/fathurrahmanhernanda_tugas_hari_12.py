from sqlalchemy import create_engine , Column, String, Float, Integer ,cast
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values
from sqlalchemy.orm import sessionmaker

# Load konfigurasi dari berkas .env
params = {
    "db": dotenv_values(".env")
}

db_user = params['db']['MYSQL_USERNAME']
db_password = params['db']['MYSQL_PASSWORD']
db_host = params['db']['MYSQL_HOST']
db_port = params['db']['MYSQL_PORT']
db_databs = params['db']['MYSQL_DB']
print(params['db'].keys())

#Mendifinisikan base model
Base = declarative_base()

#Mendefinisikan model untuk tabel movies
class Movie(Base):
    __tablename__ = 'movies'
    movie_title = Column(String(255), primary_key=True)
    title_year = Column(Integer)
    gross = Column(Float)

#Membuat objek engine untuk koneksi database
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_databs}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
#Membuat session
Session = sessionmaker(bind = engine)
session = Session()

## Fungsi untuk menampilkan 15 film dengan pendapatan terbesar
def most_profitable_movie():
    result = session.query(Movie.movie_title, Movie.title_year, Movie.gross) \
    .distinct() \
    .order_by(Movie.gross.desc()) \
    .limit(15).all()

    if result:
        print("Top 15 Movies with the Highest Gross:")
        for i, row in enumerate(result, start=1):
            movie_title = row[0]
            title_year = int(row[1])
            gross = row[2]
            print(f"{i}. {movie_title} ({title_year}) - {gross:.2f}")
    else:
        print("No data found.")

# Panggil fungsi most_profitable_movie()
most_profitable_movie()


