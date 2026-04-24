document.addEventListener("DOMContentLoaded", function () {

    alert("JS Loaded");

    document.getElementById("send-btn").addEventListener("click", sendPrompt);

});

function sendPrompt() {

    const prompt = document.getElementById("prompt-input").value;

    fetch("/process", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(res => {
        // 🔥 Handle non-JSON (important fix)
        if (!res.ok) {
            throw new Error("Server error");
        }
        return res.json();
    })
    .then(data => {

        console.log(data);

        // ✅ Chat history
        let chat = document.getElementById("chat-history");

        if (chat) {
            let msg = document.createElement("div");
            msg.className = "ai-message";
            msg.innerText = data.message;

            chat.appendChild(msg);
            chat.scrollTop = chat.scrollHeight;
        }

        // ✅ Optional response box
        let aiBox = document.getElementById("ai-response");
        if (aiBox) {
            aiBox.innerText = data.message;
        }

        // ✅ Code editor
        let editor = document.getElementById("code-editor");

        if (editor) {
            if (editor.value.trim() === "") {
                editor.value = data.code;
            } else {
                editor.value += "\n\n# --- New Code ---\n" + data.code;
            }
            editor.focus();
        }

        // ✅ Clear input
        document.getElementById("prompt-input").value = "";
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error: " + error.message);
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
