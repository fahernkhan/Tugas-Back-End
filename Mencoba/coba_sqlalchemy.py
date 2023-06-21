import sqlalchemy as sa
meta = sa.MetaData()
students = sa.Table("students", 
                      meta, 
                      sa.Column("id_siswa", sa.Integer, primary_key=True), 
                      sa.Column("nama", sa.String), sa.Column("id_kelas", sa.Integer), sa.Column("tahun_masuk", sa.Integer)
                      )

sql = sa.select(students)

print(sql.where(students.c.id_siswa == 1))