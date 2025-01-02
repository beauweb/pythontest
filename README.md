# Simple Flask API

A basic Flask API ready for deployment on Amazon Linux.

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will be available at http://localhost:5000

## Production Deployment

For production deployment on Amazon Linux:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Endpoints

- `/`: Welcome message
- `/health`: Health check endpoint
