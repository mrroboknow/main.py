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

    # Ta konfiguracja pozwala Pydanticowi czytać dane z obiektów SQLAlchemy
    class Config:
        from_attributes = True

@app.post("/api/clients", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """
    Tworzy nowego klienta w bazie danych.
    """
    log.info(f"Otrzymano prośbę o utworzenie klienta: {client.client_name}")
    
    # Tworzymy obiekt bazy danych na podstawie otrzymanych danych
    db_client = models.Client(**client.dict())
    
    db.add(db_client)
    db.commit()
    db.refresh(db_client) # Odśwież, aby pobrać ID z bazy
    
    log.info(f"Pomyślnie utworzono klienta z ID: {db_client.id}")
    return db_client