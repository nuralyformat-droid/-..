from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# Убедитесь, что файл выше называется euclid.py
from euclid import EuclidAlgorithm, EuclidResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NumbersInput(BaseModel):
    a: int
    b: int

@app.get("/")
def read_root():
    return {"message": "Euclid Algorithm API"}

@app.post("/euclid", response_model=EuclidResponse)
def calculate_euclid(numbers: NumbersInput):
    if numbers.a == 0 and numbers.b == 0:
        raise HTTPException(status_code=400, detail="Both numbers cannot be zero")
    return EuclidAlgorithm.calculate_gcd(numbers.a, numbers.b)

@app.get("/euclid/{a}/{b}", response_model=EuclidResponse)
def calculate_euclid_get(a: int, b: int):
    if a == 0 and b == 0:
        raise HTTPException(status_code=400, detail="Both numbers cannot be zero")
    return EuclidAlgorithm.calculate_gcd(a, b)