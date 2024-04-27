#!/bin/bash
echo "Moving to back_end directory..."
cd back_end
pwd
echo "Starting FastAPI application..."
# Start FastAPI application using uvicorn
export PYTHONPATH=/app/back_end:$PYTHONPATH
uvicorn src.main:app --host 0.0.0.0 --port 8000 &

echo "Starting cron..."
cron -f