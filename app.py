from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "demo_secret"
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Fake accounts
accounts = {
    "jabelo": {"balance": 500.00, "transactions": []},
    "thabo": {"balance": 300.00, "transactions": []}
}

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username in accounts:
            session['user'] = username
            return redirect(url_for('dashboard'))
        return "User not found", 404
    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['user'])

# API endpoints
@app.route('/balance', methods=['GET'])
def get_balance():
    user = session.get('user')
    return jsonify({"balance": accounts[user]["balance"]})

@app.route('/send', methods=['POST'])
def send_money():
    user = session.get('user')
    data = request.json
    recipient = data.get('recipient')
    amount = float(data.get('amount', 0))

    if recipient not in accounts: return jsonify({"error":"Recipient not found"}), 404
    if amount <= 0: return jsonify({"error":"Invalid amount"}), 400
    if accounts[user]["balance"] < amount: return jsonify({"error":"Insufficient funds"}), 400

    accounts[user]["balance"] -= amount
    accounts[recipient]["balance"] += amount
    accounts[user]["transactions"].append({"type":"send", "recipient":recipient, "amount":amount})
    return jsonify({"message": f"Sent R{amount:.2f} to {recipient}", "balance": accounts[user]["balance"]})

@app.route('/pay', methods=['POST'])
def pay_bill():
    user = session.get('user')
    data = request.json
    bill = data.get('bill_name')
    amount = float(data.get('amount',0))

    if amount <=0: return jsonify({"error":"Invalid amount"}), 400
    if accounts[user]["balance"] < amount: return jsonify({"error":"Insufficient funds"}), 400

    accounts[user]["balance"] -= amount
    accounts[user]["transactions"].append({"type":"bill","bill_name":bill,"amount":amount})
    return jsonify({"message": f"Paid {bill} bill of R{amount:.2f}","balance": accounts[user]["balance"]})

@app.route('/transactions', methods=['GET'])
def transactions():
    user = session.get('user')
    return jsonify(accounts[user]["transactions"])

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
