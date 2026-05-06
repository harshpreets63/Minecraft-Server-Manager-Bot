# 🟢 Minecraft Server Manager Bot

A lightweight **Telegram bot** to manage and monitor a Minecraft server running on a VPS.

---

## 🚀 Features

### 🎮 Server Control

* Start Minecraft server (`/start_server`)
* Stop Minecraft server (`/stop_server`)
* Check server status (`/status`)

### 📊 Server Monitoring

* Player count (online/max)
* Server version
* Latency (ping)

### 💻 System Monitoring

* RAM usage
* Disk usage

### 🤖 Telegram Integration

* Command-based interaction
* Custom command menu
* Async handling (non-blocking)

---

## 🧠 Tech Stack

* Python
* `python-telegram-bot`
* `mcstatus`
* `psutil`
* `subprocess`
* Linux (VPS environment)

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/harshpreets63/Minecraft-Server-Manager-Bot
cd Minecraft-Server-Manager-Bot
```

---

### 2. Run Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

### 🔧 What setup.sh does

* Installs Python and Java
* Downloads Fabric Minecraft server
* Accepts EULA automatically
* Generates server files
* Applies optimized server configuration

---

### 3. Configure Environment

Create a `config.env` file:

```env
BOT_TOKEN=
OWNER_ID=
SERVER_PATH=
```

---

### 4. Install Python Requirements

```bash
pip install -r requirements.txt
```

---

### 5. Run Bot

```bash
python3 -m bot
```

---

## ⚙️ Server Configuration (Automated)

The setup script automatically:

* Sets max players to 50
* Enables query
* Disables online mode
* Increases view/simulation distance
* Disables auto-pause when server is empty

---

## 🛠️ TODO / Future Improvements

### 🔧 Core Features

* [ ] Restart command
* [ ] Uptime tracking
* [ ] Auto-restart on crash

### 📊 Monitoring

* [ ] Detailed logs command (`/logs`)
* [ ] Player join/leave tracking

### ⚙️ System

* [ ] Setup as a systemd service (auto start on boot)

### 🤖 Events

* [ ] Telegram notifications for player join/leave

---

## 💡 Learning Goals

This project demonstrates:

* Process management using `subprocess`
* Async programming in Python
* Linux server management
* Networking & port handling
* API integration (Telegram)

---

## 📌 Notes

* Designed as a **portfolio project**
* Focused on **real-world system interaction**
* Built and tested on Linux VPS

---

## 🧑‍💻 Author

Harshpreet Singh

---
