from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Membuat engine dan koneksi ke SQLite
engine = create_engine('sqlite:///database.db', echo=True)

Base = declarative_base()


# Mendefinisikan model tabel
class Buku(Base):
    __tablename__ = 'buku'
    id = Column(Integer, primary_key=True)
    judul = Column(String)
    penulis = Column(String)
    tahun_terbit = Column(Integer)

# Membuat tabel di database
Base.metadata.create_all(engine)

# Membuat sesi
Session = sessionmaker(bind=engine)
session = Session()

# Menambahkan data baru
buku_baru = Buku(judul='Belajar SQLAclhemy', penulis='Jane Doe', tahun_terbit=2024)
session.add(buku_baru)
session.commit()

# Query data
for buku in session.query(Buku).all():
    print(buku.judul, buku.penulis, buku.tahun_terbit)