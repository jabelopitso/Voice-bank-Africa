#!/bin/bash

echo "🚀 Starting VoiceBank Africa..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv_flask" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv_flask
fi

# Activate virtual environment
source venv_flask/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q flask

# Run the app
echo ""
echo "✓ Starting Flask server..."
echo "✓ Open your browser at: http://127.0.0.1:5000/"
echo "✓ Test users: jabelo or thabo"
echo ""
python3 app.py
