// /in_out_ui/components/chatbot/pc_control.js
function handleCommand(command) {
    console.log(`Befehl ausführen: ${command}`);
    // Implementiere die Logik zur Ausführung der PC-Steuerbefehle
    executeCommand(command).then(response => {
        alert(response);
    });
}

function executeCommand(command) {
    // Beispielimplementierung zum Ausführen von PC-Steuerbefehlen
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(`Befehl ausgeführt: ${command}`);
        }, 1000);
    });
}
