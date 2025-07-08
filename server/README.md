# PlateAI Server

This is the backend server for PlateAI, built with FastAPI.

## Requirements
- Python 3.10+

## Installation
```bash
cd server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Server
```bash
uvicorn main:app --reload
```

The server will be available at http://127.0.0.1:8000

## Health Check
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to verify the server is running. 