# Plik: models.py

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Client(Base):
    __tablename__ = "clients"  # Nazwa tabeli w bazie danych

    # Definicja kolumn
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, unique=True, index=True)
    client_code = Column(String, unique=True, index=True)
    nip = Column(String, nullable=True) # nullable=True oznacza, że pole może być puste
    company_address = Column(String, nullable=True)
    delivery_address = Column(String, nullable=True)
    delivery_name = Column(String, nullable=True)
    is_cynkownia = Column(Boolean, default=False)
    zleceniodawca_name = Column(String, nullable=True)
