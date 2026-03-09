async function sendMessage() {

  const inputBox = document.getElementById("chat-input");
  const chat = document.getElementById("chat-messages");

  const input = inputBox.value.trim();
  if (!input) return;

  chat.innerHTML += `<p><b>You:</b> ${input}</p>`;
  inputBox.value = "";

  const response = await fetch("https://cs-api-zb8v.onrender.com/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message: input
    })
  });

  const data = await response.json();

  chat.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;
}

