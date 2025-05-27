from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Buku(Base):
    __tablename__ = 'buku'
    id = Column(Integer, primary_key=True)
    judul = Column(String)
    penulis = Column(String)


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

buku_baru = Buku(judul='Python Lanjutan', penulis='Supa AI')
session.add(buku_baru)
session.commit()
