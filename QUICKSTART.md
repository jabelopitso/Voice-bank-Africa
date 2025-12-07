# 🚀 Quick Start Guide

## Run the Application

### Option 1: Using the run script (Recommended)
```bash
./run.sh
```

### Option 2: Manual setup
```bash
# Install Flask
pip3 install flask

# Run the app
python3 app.py
```

## Access the Application

1. Open your browser: **http://127.0.0.1:5000/**

2. **Sign Up** for a new account (starts with R1000.00)
   - OR -
   **Login** with demo accounts:
   - Username: `jabelo` / Password: `1234`
   - Username: `thabo` / Password: `1234`

## Features to Try

### 1. Check Balance
- Click "Refresh Balance" button
- Or use voice: "Check balance"

### 2. Send Money
- Click "Send Money" button
- Enter recipient username (e.g., `thabo`)
- Enter amount
- Or use voice: "Send money"

### 3. Pay Bills
- Click "Pay Bill" button
- Enter bill name (e.g., `Electricity`)
- Enter amount
- Or use voice: "Pay bill"

### 4. View Transactions
- Click "Refresh Transactions" button
- Or use voice: "View transactions"

### 5. Voice Commands
- Click 🎤 "Voice Command" button
- Allow microphone access
- Say: "Check balance", "Send money", "Pay bill", or "View transactions"

## Troubleshooting

**Port already in use?**
```bash
lsof -ti:5000 | xargs kill -9
```

**Flask not installed?**
```bash
pip3 install flask
```

**Permission denied on run.sh?**
```bash
chmod +x run.sh
```
