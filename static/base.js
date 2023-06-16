const socket = new WebSocket("ws://localhost:8000/ws/ping/");
const messageContainer = document.getElementById("message-container");

socket.onmessage = function (event) {
  // Handle the received ping message
  const message = event.data;
  // Update the DOM with the received message
  messageContainer.innerText = message;
};
