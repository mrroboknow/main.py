# Plik: main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

# Importujemy nasze moduły
from . import models, schemas
from .database import SessionLocal, engine

# Ta linia tworzy wszystkie tabele w bazie danych (jeśli jeszcze nie istnieją)
# Na podstawie tego, co zdefiniowaliśmy w models.py
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Funkcja pomocnicza do "wstrzykiwania" sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- NASZ ZMODYFIKOWANY ENDPOINT ---

@app.get("/api/clients", response_model=List[schemas.Client])
def get_clients(db: Session = Depends(get_db)):
    """
    Pobiera listę wszystkich klientów z bazy danych.
    """
    clients = db.query(models.Client).order_by(models.Client.client_name).all()
    return clients

# --- ENDPOINT DO DODAWANIA DANYCH TESTOWYCH (opcjonalny, ale przydatny) ---

@app.post("/api/add-test-client")
def add_test_client(db: Session = Depends(get_db)):
    """
    Dodaje jednego, testowego klienta do bazy.
    """
    # Sprawdź, czy klient testowy już istnieje
    existing_client = db.query(models.Client).filter(models.Client.client_code == "TEST.01").first()
    if existing_client:
        return {"message": "Klient testowy już istnieje."}

    new_client = models.Client(
        client_name="Klient Testowy",
        client_code="TEST.01",
        is_cynkownia=False
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return {"message": "Dodano klienta testowego.", "client": new_client.client_name}
