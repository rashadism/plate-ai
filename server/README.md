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

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
DB_SCHEMA=public
```

Adjust the values as needed for your PostgreSQL setup.

## Running the Server
```bash
uvicorn main:app --reload
```

The server will be available at http://127.0.0.1:8000

## Health Check
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to verify the server is running. 