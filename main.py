# Plik: main.py

import sys
import traceback
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

# Importujemy nasze moduły
import models
import schemas
from database import SessionLocal, engine

# Tworzenie tabel
try:
    log.info("Tworzenie tabel w bazie danych...")
    models.Base.metadata.create_all(bind=engine)
    log.info("Tabele utworzone/sprawdzone.")
except Exception as e:
    log.error(f"BŁĄD PODCZAS create_all: {e}")
    log.error(traceback.format_exc())
    raise

# Inicjalizacja aplikacji FastAPI
app = FastAPI()

# Funkcja pomocnicza do sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTY APLIKACJI ---

@app.get("/api/clients", response_model=List[schemas.Client])
def get_clients(db: Session = Depends(get_db)):
    """Pobiera listę wszystkich klientów."""
    log.info("Otrzymano zapytanie GET do /api/clients")
    clients = db.query(models.Client).order_by(models.Client.client_name).all()
    return clients

# TEN KOD MUSI BYĆ TUTAJ, W main.py
@app.post("/api/clients", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """Tworzy nowego klienta w bazie danych."""
    log.info(f"Otrzymano zapytanie POST do /api/clients z danymi: {client.client_name}")
    
    # Sprawdzenie, czy klient o takim kodzie już nie istnieje (opcjonalne, ale dobre)
    # existing_client = db.query(models.Client).filter(models.Client.client_code == client.client_code).first()
    # if existing_client:
    #     raise HTTPException(status_code=400, detail="Klient o tym kodzie już istnieje")

    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    
    log.info(f"Pomyślnie utworzono klienta z ID: {db_client.id}")
    return db_client

log.info("Aplikacja FastAPI zainicjowana.")