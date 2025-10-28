#!/bin/sh
set -e

export PYTHONPATH=/app

echo "Running database setup..."
python app/scripts/setup_db.py

echo "Seeding test users..."
python app/scripts/test_seed_users.py


echo "Starting application..."
exec "$@"
