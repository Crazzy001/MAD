// /in_out_ui/speech.js
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'de-DE';
recognition.interimResults = false;

recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    processCommand(transcript);
};

function startListening() {
    recognition.start();
}

function processCommand(command) {
    console.log('Sprachbefehl erkannt:', command);
    document.getElementById('chatbox').innerText += `\nUser: ${command}`;
    sendMessage(command).then(response => {
        document.getElementById('chatbox').innerText += `\nBot: ${response}`;
    });
}
