async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    const userMessage = document.createElement("div");

    userMessage.className = "user-message";

    userMessage.innerText = message;

    chatBox.appendChild(userMessage);

    input.value = "";

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const data = await response.json();

    const botMessage = document.createElement("div");

    botMessage.className = "bot-message";

    botMessage.innerText = data.response;

    chatBox.appendChild(botMessage);

    chatBox.scrollTop = chatBox.scrollHeight;
}