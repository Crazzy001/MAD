// /mnt/f/chatbot/mad-dashboard/renderer.js
async function sendMessage() {
  const message = document.getElementById('message').value;
  const responseElement = document.getElementById('response');

  const response = await fetch('http://localhost:8150/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message, model: 'local' })
  });

  const result = await response.json();
  responseElement.textContent = result.response;
}
