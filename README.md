# 🚀 Ollama Local Chat App

<img width="1623" height="1004" alt="1" src="https://github.com/user-attachments/assets/b9809378-0b35-4db7-817d-39d1ab0467d0" />


A sleek, minimal, and powerful **local AI chat application** built using:

* ⚡ **Flask (Backend)**
* 🎨 **Vanilla HTML/CSS/JS (Frontend)**
* 🧠 **Ollama (Local LLM Runtime)**

Run AI models **completely offline** on your machine — no API keys, no cloud dependency.

---

## ✨ Features

* 💬 Chat with local LLM (e.g., `llama3.2:1b`)
* ⚡ Fast & lightweight Flask backend
* 🎯 Clean, modern UI with dark theme
* 🧠 Maintains chat history
* 🚫 Fully offline (privacy-first)
* ⚠️ Error handling (Ollama not running, timeout, etc.)

---

## 🏗️ Project Structure

```
.
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Frontend UI
└── README.md
```

---

## 🧠 How It Works

1. User sends message from UI
2. Frontend sends request → Flask backend
3. Flask calls Ollama API:

   ```
   http://localhost:11434/api/chat
   ```
4. Ollama processes using local model
5. Response sent back → UI

---

## ⚙️ Prerequisites

Make sure you have:

* ✅ Python 3.8+
* ✅ Ollama installed

👉 Install Ollama: https://ollama.com

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ollama-chat-app.git
cd ollama-chat-app
```

---

### 2. Install Dependencies

```bash
pip install flask requests
```

---

### 3. Start Ollama

```bash
ollama serve
```

---

### 4. Pull Required Model

```bash
ollama pull llama3.2:1b
```

> You can change the model in `app.py`:

```python
MODEL = "llama3.2:1b"
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## 🖥️ Usage

* Type your message
* Press **Enter** or click **Send**
* Chat with your local AI 🚀

---

## ⚠️ Troubleshooting

### ❌ Ollama not running

```
Error: Ollama is not running
```

👉 Fix:

```bash
ollama serve
```

---

### ⏳ Timeout Error

* Try shorter prompts
* Restart Ollama

---

### 🔌 Connection Error

* Ensure port `11434` is free
* Restart both Flask & Ollama

---

## 🎨 UI Preview

* Dark theme 🌑
* Chat bubbles 💬
* Typing animation ⏳
* Clean developer-style interface

---

## 🔧 Customization

### Change Model

Edit in `app.py`:

```python
MODEL = "mistral"
```

---

### Enable Streaming (Advanced)

Modify API call:

```python
"stream": True
```

---

## 🚀 Future Improvements

* ✅ Streaming responses
* ✅ Markdown rendering
* ✅ Code highlighting
* ✅ Multi-model selection
* ✅ Chat export

---

## 🤝 Contributing

Pull requests are welcome!

If you have ideas to improve UI/UX or performance — go ahead 🚀

---

## 📜 License

MIT License

---

## 💡 Inspiration

Built for developers who want:

* Local AI ⚡
* Full control 🔒
* Zero API cost 💸



---

⭐ If you like this project, give it a star on GitHub!
