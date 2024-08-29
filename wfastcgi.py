# wfastcgi.py
import sys

def main():
    try:
        from fastapi import FastAPI
        from fastapi.middleware.wsgi import WSGIMiddleware
    except ImportError:
        sys.stderr.write("Error: Can't find FastAPI module.")
        sys.exit(1)
    
    import app as myapp  # Import your FastAPI app here
    app = WSGIMiddleware(myapp.app)

    return app
