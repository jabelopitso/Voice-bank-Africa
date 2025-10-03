function speak(text){
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
    console.log(text);
}

// Update balance on page
function checkBalance(){
    fetch('/balance').then(res=>res.json()).then(data=>{
        document.getElementById('balance').innerText = `R${data.balance.toFixed(2)}`;
        speak(`Your balance is ${data.balance} Rand`);
    });
}

// Send money
function sendMoney(){
    const recipient = prompt("Recipient?");
    const amount = prompt("Amount?");
    if(recipient && amount){
        fetch('/send',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({recipient, amount})
        }).then(res=>res.json()).then(data=>{
            if(data.error) speak(data.error);
            else { speak(data.message); checkBalance(); }
        });
    }
}

// Pay bill
function payBill(){
    const bill = prompt("Bill name?");
    const amount = prompt("Amount?");
    if(bill && amount){
        fetch('/pay',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({bill_name:bill, amount})
        }).then(res=>res.json()).then(data=>{
            if(data.error) speak(data.error);
            else { speak(data.message); checkBalance(); }
        });
    }
}

// Transactions
function viewTransactions(){
    fetch('/transactions').then(res=>res.json()).then(data=>{
        const div = document.getElementById('transactions');
        if(data.length===0){ div.innerText="No transactions yet."; speak("No transactions yet."); return; }
        let html="";
        data.forEach(t=>{
            if(t.type==="send") html+=`Sent R${t.amount} to ${t.recipient}\n`;
            if(t.type==="bill") html+=`Paid ${t.bill_name} bill R${t.amount}\n`;
        });
        div.innerText = html;
        speak("Here are your recent transactions.");
    });
}

// Voice commands
const recognition = new (window.SpeechRecognition||window.webkitSpeechRecognition)();
recognition.lang='en-US';
recognition.continuous=false;
function startListening(){
    recognition.start();
    recognition.onresult = function(event){
        const command = event.results[0][0].transcript.toLowerCase();
        if(command.includes("balance")) checkBalance();
        else if(command.includes("send")) sendMoney();
        else if(command.includes("pay")||command.includes("bill")) payBill();
        else if(command.includes("transaction")) viewTransactions();
        else speak("Command not recognized.");
    };
}
