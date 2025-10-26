#!/bin/sh
set -e

echo "Running database setup..."
python app/scripts/setup_db.py

echo "Starting application..."
exec "$@"
