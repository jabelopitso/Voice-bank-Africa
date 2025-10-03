from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

accounts = {
    "jabelo": {
        "balance": 500.00,
        "transactions": []
    }
}

current_user = "jabelo"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify({"balance": accounts[current_user]["balance"]})

@app.route('/send', methods=['POST'])
def send_money():
    data = request.json
    amount = float(data.get("amount", 0))
    recipient = data.get("recipient", "Unknown")
    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400
    if accounts[current_user]["balance"] < amount:
        return jsonify({"error": "Insufficient funds"}), 400
    accounts[current_user]["balance"] -= amount
    accounts[current_user]["transactions"].append({"type": "send", "recipient": recipient, "amount": amount})
    return jsonify({"message": f"Sent R{amount:.2f} to {recipient}", "balance": accounts[current_user]["balance"]})

@app.route('/pay', methods=['POST'])
def pay_bill():
    data = request.json
    amount = float(data.get("amount", 0))
    bill_name = data.get("bill_name", "Unknown")
    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400
    if accounts[current_user]["balance"] < amount:
        return jsonify({"error": "Insufficient funds"}), 400
    accounts[current_user]["balance"] -= amount
    accounts[current_user]["transactions"].append({"type": "bill", "bill_name": bill_name, "amount": amount})
    return jsonify({"message": f"Paid {bill_name} bill of R{amount:.2f}", "balance": accounts[current_user]["balance"]})

@app.route('/transactions', methods=['GET'])
def transactions():
    return jsonify(accounts[current_user]["transactions"])

if __name__ == "__main__":
    app.run(debug=True)
