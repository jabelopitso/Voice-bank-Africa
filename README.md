# Voice-bank-Africa# VoiceBank Africa

🚀 **VoiceBank Africa** is a demo web application that simulates a voice-activated banking system.  
It allows users to **check balance, send money, pay bills, and view transactions** using buttons or **voice commands**.

This project is built with **Python (Flask)** for the backend and **HTML, CSS, and JavaScript** for the frontend.

---

## Features

- User signup and login with password authentication
- Demo accounts available (`jabelo`, `thabo` - password: 1234)
- New accounts start with R1000.00 balance
- View account balance directly on the dashboard  
- Send money to other users  
- Pay bills  
- View transaction history  
- Voice commands for checking balance, sending money, paying bills, and viewing transactions  
- Logout functionality  

---

## Project Structure

```
Voice-bank-Africa/
├── app.py                 # Flask backend
├── data/
│   └── accounts.json      # Account data storage
├── static/
│   ├── script.js          # Frontend JavaScript
│   └── style.css          # Styling
├── templates/
│   ├── login.html         # Login page
│   └── dashboard.html     # Dashboard page
├── venv_flask/            # Virtual environment
└── README.md
```

---

## Requirements

- Python 3.8+  
- Flask  
- Flask-Session  

---

## Setup & Run

1. Clone the repository:
```bash
git clone <repository-url>
cd Voice-bank-Africa

python3 -m venv venv_flask
source venv_flask/bin/activate  # On Windows: venv_flask\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask
```

4. Run the application:
```bash
python app.py
```

5. Open your browser:
```
http://127.0.0.1:5000/
```

6. Login with test accounts or create a new account:
   - Username: `jabelo` / Password: `1234` (Balance: R500.00)
   - Username: `thabo` / Password: `1234` (Balance: R300.00)
   - Or click "Sign Up" to create your own account (starts with R1000.00)

---

## Usage

### Button Controls
- **Refresh Balance**: Update your current balance
- **Send Money**: Transfer money to another user
- **Pay Bill**: Pay a bill (e.g., electricity, water)
- **Refresh Transactions**: View transaction history
- **Voice Command**: Use voice to control the app
- **Logout**: End your session

### Voice Commands
Click the 🎤 Voice Command button and say:
- "Check balance" - View your balance
- "Send money" - Initiate money transfer
- "Pay bill" - Pay a bill
- "View transactions" - See transaction history

---

## API Endpoints

- `GET /` - Login page
- `GET /dashboard` - User dashboard
- `GET /balance` - Get current balance
- `POST /send` - Send money (JSON: {recipient, amount})
- `POST /pay` - Pay bill (JSON: {bill_name, amount})
- `GET /transactions` - Get transaction history
- `GET /logout` - Logout

---

## Features Implemented

✅ User signup and authentication with passwords  
✅ Balance checking  
✅ Money transfer between accounts  
✅ Bill payment  
✅ Transaction history  
✅ Voice recognition for commands  
✅ Text-to-speech feedback  
✅ Data persistence (JSON)  
✅ Responsive UI design  

---

## Notes

- This is a **demo application** for educational purposes
- Account data is stored in `data/accounts.json`
- Voice commands require browser microphone permissions
- Works best in Chrome/Edge browsers for voice features
