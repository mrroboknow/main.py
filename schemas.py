# Plik: schemas.py

from pydantic import BaseModel
from typing import Optional

# Schemat, który będzie używany do ZWRACANIA danych o kliencie przez API
class Client(BaseModel):
    id: int
    client_name: str
    client_code: str
    nip: Optional[str] = None
    company_address: Optional[str] = None
    delivery_address: Optional[str] = None
    delivery_name: Optional[str] = None
    is_cynkownia: bool
    zleceniodawca_name: Optional[str] = None

    class Config:
        from_attributes = True

# Schemat do TWORZENIA nowego klienta
class ClientCreate(BaseModel):
    client_name: str
    client_code: str
    nip: Optional[str] = None
    company_address: Optional[str] = None
    delivery_address: Optional[str] = None
    delivery_name: Optional[str] = None
    is_cynkownia: bool = False
    zleceniodawca_name: Optional[str] = None

# --- USUŃ STĄD WSZYSTKIE LINIE Z @app.post ---