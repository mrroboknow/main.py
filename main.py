from fastapi import FastAPI

# Stwórz instancję aplikacji
app = FastAPI()

# Zdefiniuj pierwszy "punkt końcowy" (endpoint)
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint, który zwraca listę klientów (na razie na sztywno)
@app.get("/api/clients")
def get_clients():
    # W przyszłości te dane będą pochodzić z bazy danych
    return [
        {"id": 1, "name": "Klient A", "code": "KA.01"},
        {"id": 2, "name": "Klient B", "code": "KB.02"},
        {"id": 3, "name": "Cynkownia C", "code": "CC.03"},
    ]