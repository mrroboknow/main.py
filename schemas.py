# Plik: schemas.py

from pydantic import BaseModel
from typing import Optional

# Schemat, który będzie używany do ZWRACANIA danych o kliencie przez API
class Client(BaseModel):
    id: int
    client_name: str
    client_code: str
    nip: Optional[str] = None # Optional oznacza, że pole może nie istnieć w odpowiedzi
    company_address: Optional[str] = None
    delivery_address: Optional[str] = None
    delivery_name: Optional[str] = None
    is_cynkownia: bool
    zleceniodawca_name: Optional[str] = None

    # Ta konfiguracja pozwala Pydanticowi czytać dane z obiektów SQLAlchemy
    class Config:
        from_attributes = True
