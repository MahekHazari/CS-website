async function sendMessage(){

let input = document.getElementById("chat-input").value;

let response = await fetch("https://your-backend-url/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({message:input})

});

let data = await response.json();

let chat = document.getElementById("chat-messages");

chat.innerHTML += "<p><b>You:</b> "+input+"</p>";

chat.innerHTML += "<p><b>AI:</b> "+data.reply+"</p>";

}