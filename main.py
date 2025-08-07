# Plik: main.py

import sys
import traceback
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

# Dodajemy logowanie, żeby widzieć więcej na serwerze
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

# POPRAWIONE IMPORTY (bez kropek)
try:
    log.info("Importowanie lokalnych modułów...")
    import models
    import schemas
    from database import SessionLocal, engine
    log.info("Importowanie zakończone sukcesem.")
except ImportError as e:
    log.error(f"KRYTYCZNY BŁĄD IMPORTU: {e}")
    log.error(traceback.format_exc())
    raise

# Ta linia tworzy wszystkie tabele w bazie danych
try:
    log.info("Tworzenie tabel w bazie danych (jeśli nie istnieją)...")
    models.Base.metadata.create_all(bind=engine)
    log.info("Tabele utworzone/sprawdzone pomyślnie.")
except Exception as e:
    log.error(f"KRYTYCZNY BŁĄD PODCZAS create_all: {e}")
    log.error(traceback.format_exc())
    raise

app = FastAPI()

# Funkcja pomocnicza do "wstrzykiwania" sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTY ---

@app.get("/api/clients", response_model=List[schemas.Client])
def get_clients(db: Session = Depends(get_db)):
    """
    Pobiera listę wszystkich klientów z bazy danych.
    """
    log.info("Otrzymano zapytanie do /api/clients")
    clients = db.query(models.Client).order_by(models.Client.client_name).all()
    log.info(f"Znaleziono {len(clients)} klientów w bazie.")
    return clients

@app.post("/api/add-test-client")
def add_test_client(db: Session = Depends(get_db)):
    """
    Dodaje jednego, testowego klienta do bazy.
    """
    log.info("Otrzymano zapytanie do /api/add-test-client")
    existing_client = db.query(models.Client).filter(models.Client.client_code == "TEST.01").first()
    if existing_client:
        log.warning("Klient testowy już istnieje.")
        return {"message": "Klient testowy już istnieje."}

    new_client = models.Client(
        client_name="Klient Testowy",
        client_code="TEST.01",
        is_cynkownia=False
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    log.info("Dodano nowego klienta testowego.")
    return {"message": "Dodano klienta testowego.", "client": new_client.client_name}

log.info("Aplikacja FastAPI została zainicjowana i jest gotowa do przyjmowania zapytań.")