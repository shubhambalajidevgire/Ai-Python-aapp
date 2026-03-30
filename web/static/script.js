document.addEventListener("DOMContentLoaded", function () {

    alert("JS Loaded");

    document.getElementById("send-btn").addEventListener("click", sendPrompt);

});

function sendPrompt() {

    const prompt = document.getElementById("prompt-input").value;

    if (!prompt) {
        alert("Please enter a prompt");
        return;
    }

    fetch("/process", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(res => res.json())
    .then(data => {

        console.log(data);

        let aiBox = document.getElementById("ai-response");
let chat = document.getElementById("chat-history");

let msg = document.createElement("div");
msg.className = "ai-message";
msg.innerText = data.message;

chat.appendChild(msg);
chat.scrollTop = chat.scrollHeight;

if (aiBox) {
    aiBox.innerText = data.message;
}

let editor = document.getElementById("code-editor");

if (editor.value.trim() === "") {
    editor.value = data.code;
} else {
    editor.value += "\n\n# --- New Code ---\n" + data.code;
}

editor.focus();                 // optional

        // 🔥 CLEAR INPUT AFTER SUCCESS
        document.getElementById("prompt-input").value = "";

        document.getElementById("prompt-input").focus();
 })
    .catch(err => {
        alert("Error: " + err);
    });
}

// =========================
// ADD MESSAGE TO CHAT
// =========================
function addMessage(text, type) {

    const chat = document.getElementById("chat-history");

    const msg = document.createElement("div");
    msg.className = (type === "user") ? "user-message" : "ai-message";

    msg.innerText = text;

    chat.appendChild(msg);

    chat.scrollTop = chat.scrollHeight;
}
// =========================
// RUN CODE
// =========================
function runCode() {

    alert("run clicked");

    const code = document.getElementById("code-editor").value;

    fetch("/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: code })
    })
    .then(res => res.json())
    .then(data => {

        alert("response received");

        document.getElementById("output-text").innerText = data.output;

        document.getElementById("output-modal").style.display = "block";
    })
    .catch(err => {
        alert("Error: " + err);
    });
}

// =========================
// CLOSE OUTPUT
// =========================
function closeOutput() {
    document.getElementById("output-modal").style.display = "none";
}
