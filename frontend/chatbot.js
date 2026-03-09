async function sendMessage() {

  const inputBox = document.getElementById("chat-input");
  const chat = document.getElementById("chat-messages");

  const input = inputBox.value.trim();
  if (!input) return;

  // show user message
  chat.innerHTML += `<p><b>You:</b> ${input}</p>`;

  inputBox.value = "";

  try {

    const response = await fetch("https://cs-api-zb8v.onrender.com/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: input })
    });

    const data = await response.json();

    // show AI response
    chat.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;

  } catch (error) {

    chat.innerHTML += `<p><b>AI:</b> Server error. Please try again.</p>`;
    console.error(error);

  }

}

