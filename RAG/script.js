// Toggle the chat window popup visibility
function toggleChat() {
    const chatPopup = document.getElementById("chat-popup");
    chatPopup.style.display = (chatPopup.style.display === "none" || chatPopup.style.display === "") ? "block" : "none";
}

// Send message on Enter key press
function sendMessage(event) {
    if (event.key === "Enter") {
        const chatMessages = document.getElementById("chat-messages");
        const chatInput = document.getElementById("chat-input");
        
        const userMessage = chatInput.value.trim();
        if (userMessage) {
            const messageElement = document.createElement("p");
            messageElement.textContent = `You: ${userMessage}`;
            chatMessages.appendChild(messageElement);
            chatInput.value = "";
            chatMessages.scrollTop = chatMessages.scrollHeight;
            
            // Add response from chatbot (for demo purposes)
            const botResponse = document.createElement("p");
            botResponse.textContent = "Bot: I received your message!";
            chatMessages.appendChild(botResponse);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    }
}

