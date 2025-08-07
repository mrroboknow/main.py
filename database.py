# Plik: database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# !!! WAŻNE: PONIŻEJ WKLEJ SWÓJ ADRES URL Z RENDER.COM !!!
SQLALCHEMY_DATABASE_URL = "postgresql://warsztat_user:xKoCBmPizi6sVsSm8T7VTDKylWl42KhT@dpg-d2a6jpbuibrs73bumu00-a/warsztat"

# Tworzymy "silnik" bazy danych
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Tworzymy sesję, która będzie zarządzać połączeniami
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baza, której będą "dziedziczyć" nasze modele tabel
Base = declarative_base()