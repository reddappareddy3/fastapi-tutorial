from fastapi import FastAPI
import json
from pathlib import Path

# Create FastAPI app
app = FastAPI()

# File path (recommended way)
DATA_FILE = Path(r"C:\Users\mollu\OneDrive\Desktop\fastAPI_tutorial__\patients.json")

# Helper function to load data
def load_data():
    if not DATA_FILE.exists():
        return {"error": "patients.json file not found"}

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data

# Root endpoint
@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

# About endpoint
@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records."}

# View patients endpoint
@app.get("/view")
def view():
    data = load_data()
    return data
