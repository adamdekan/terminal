const socketHostname = new WebSocket("ws://127.0.0.1:8000/ws/host");
const messageContainer = document.getElementById("message-container");

socketHostname.onmessage = function (event) {
  // Handle the received ping message
  const message = event.data;
  // Append the message to the DOM
  const messageElement = document.createElement("p");
  messageElement.textContent = message;
  messageContainer.appendChild(messageElement);
};

socketHostname.onclose = function (event) {
  // Handle the WebSocket connection closed event
  console.log("WebSocket connection closed");
};

socketHostname.onerror = function (error) {
  // Handle WebSocket connection errors
  console.error("WebSocket error:", error);
};

const socketPing = new WebSocket("ws://127.0.0.1:8000/ws/ping");
const pingContainer = document.getElementById("ping-container");

socketPing.onmessage = function (event) {
  // Handle the received ping message
  const message = event.data;
  // Append the message to the DOM
  pingContainer.textContent = message;
};
