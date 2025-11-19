#!/bin/bash
#start.sh - start the FastAPI app on the port provided by the host

uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1