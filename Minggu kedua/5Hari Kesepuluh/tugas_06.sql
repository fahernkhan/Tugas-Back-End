DROP DATABASE IF EXISTS library;

#1. Persiapkan database, buat database dengan nama library
CREATE DATABASE IF NOT EXISTS library
;

#2. Pindahkan penggunaan pada database library
USE library
;

#3. Buat tabel
CREATE TABLE IF NOT EXISTS members(
	id int primary key auto_increment,
    name varchar(50) not null,
    city varchar(15) not null,
    age int not null,
    is_active tinyint not null
)
;

SHOW TABLES
;

#4. Input data yang telah disediakan
-- Taruh query di bawah



select * from members
;

#5. Edit data yang diperintahkan
-- Taruh query di bawah


select * from members
;

#6. Hapus semua member yang sudah tidak aktif
-- Taruh query di bawah



select * from members
;