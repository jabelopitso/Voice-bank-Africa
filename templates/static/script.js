function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
    document.getElementById("output").innerText = text;
}

function checkBalance() {
    fetch('/balance').then(res => res.json()).then(data => speak(`Your balance is ${data.balance} Rand`));
}

function sendMoney() {
    const recipient = prompt("Recipient?");
    const amount = prompt("Amount?");
    if(recipient && amount) {
        fetch('/send', {
            method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({recipient, amount})
        }).then(res => res.json()).then(data => speak(data.error ? data.error : data.message));
    }
}

function payBill() {
    const bill = prompt("Bill name?");
    const amount = prompt("Amount?");
    if(bill && amount) {
        fetch('/pay', {
            method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({bill_name:bill, amount})
        }).then(res => res.json()).then(data => speak(data.error ? data.error : data.message));
    }
}

function viewTransactions() {
    fetch('/transactions').then(res => res.json()).then(data => {
        let output = "Transactions:\n";
        data.forEach(t => {
            if(t.type==="send") output+=`Sent R${t.amount} to ${t.recipient}\n`;
            if(t.type==="bill") output+=`Paid ${t.bill_name} bill R${t.amount}\n`;
        });
        speak(output || "No transactions yet.");
    });
}

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang='en-US'; recognition.continuous=false;
function startListening() {
    recognition.start();
    recognition.onresult = function(event) {
        const command = event.results[0][0].transcript.toLowerCase();
        if(command.includes("balance")) checkBalance();
        else if(command.includes("send")) sendMoney();
        else if(command.includes("pay")||command.includes("bill")) payBill();
        else if(command.includes("transaction")) viewTransactions();
        else speak("Command not recognized.");
    };
}
