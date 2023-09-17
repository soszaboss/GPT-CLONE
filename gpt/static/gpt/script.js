// DOM elements
const chatPage = document.getElementById('chat-page');
const chatMessages = document.getElementById('chat-messages');
const messageForm = document.getElementById('message-form');
const userMessageInput = document.getElementById('user-message');
// Function to append a user or AI message to the chat
function appendMessage(message, isUser = false) {
    const messageElement = document.createElement('div');
    messageElement.className = isUser ? 'user-message p-3 border-top border-end shadow bg-light-subtle fs-5 shadow lh-base' : 'ai-message p-2 bg-secondary-subtle fs-5 lh-base';
    messageElement.innerText = message;
    chatMessages.appendChild(messageElement);
    // Scroll to the bottom of the chat container
    // chatMessages.scrollTop = chatMessages.scrollHeight;
}
// Event listener for sending messages
const sendingMessages = function (message = "AI response goes here") {
    messageForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const userMessage = userMessageInput.value.trim();
    if (userMessage !== '') {
        appendMessage(userMessage, true); // Display user message
        userMessageInput.value = '';

        // Send the user message to the GPT model (you'll need to implement this part)
        // Receive a response from the model and append it to the chat
        const aiResponse = message; // Replace with actual AI response
        appendMessage(aiResponse, false);
    }
});
};

function enterPress(event) {
  // If the user pressed the Enter key, trigger the sendMessage() function.
  if (event.keyCode === 13) {
    // Get the message from the input field.
    let message = userMessageInput.value;
    sendingMessages(message)

    // Send the message to the server.
    // ...
  }
}
// Example: Automatically show the chat interface after successful login/registration
// Replace this with your actual logic
// chatPage.style.display = 'block';


