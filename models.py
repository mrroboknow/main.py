# Plik: models.py

from sqlalchemy import Column, Integer, String, Boolean

# POPRAWIONY IMPORT (bez kropki)
from database import Base

class Client(Base):
    __tablename__ = "clients"  # Nazwa tabeli w bazie danych

    # Definicja kolumn
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, unique=True, index=True)
    client_code = Column(String, unique=True, index=True)
    nip = Column(String, nullable=True)
    company_address = Column(String, nullable=True)
    delivery_address = Column(String, nullable=True)
    delivery_name = Column(String, nullable=True)
    is_cynkownia = Column(Boolean, default=False)
    zleceniodawca_name = Column(String, nullable=True)

# Tutaj w przyszłości dodasz inne modele, np. dla Projektów, Zleceń itd.
# class Project(Base):
#     __tablename__ = "projects"
#     ...