#!/bin/bash

# Activate virtual environment if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install dependencies
if pip install -r requirements.txt; then
    echo "Dependencies installed successfully"
else
    echo "Failed to install dependencies"
    exit 1
fi

# Collect static files
if python manage.py collectstatic --no-input; then
    echo "Static files collected successfully"
else
    echo "Failed to collect static files"
    exit 1
fi
