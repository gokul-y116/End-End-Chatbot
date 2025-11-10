# 🔒 End-to-End Encrypted Chat Application (Single Network Implementation)

## 🧠 Project Overview
This project is a **secure local network chat application** that enables two or more users to **communicate privately within the same LAN (Local Area Network)**.  
It provides **end-to-end encryption (E2EE)** using **RSA and AES algorithms**, ensuring that all messages are completely protected — even the server cannot read them.  

This project demonstrates how **cryptography**, **socket programming**, and **GUI-based communication** can combine to form a secure and user-friendly cybersecurity system.

---

## 🎯 Objective
To develop a **real-time encrypted chat system** that:
- Works entirely within a **single LAN network**
- Provides **multi-layer encryption** for every message
- Features a **simple, user-friendly GUI**
- Demonstrates core **cybersecurity principles of confidentiality and integrity**

---

## 🧩 System Architecture

### ⚙️ Components
| Component | Function |
|------------|-----------|
| **server.py** | Acts as the main relay hub. Receives encrypted messages and forwards them to the target user. |
| **client.py** | Connects to the server, encrypts and decrypts messages locally. Provides GUI interface for chatting. |
| **crypto_core.py** | Contains cryptographic logic (RSA & AES key generation, encryption, decryption). |
| **Tkinter GUI** | Creates the user interface for sending and receiving encrypted messages. |

---

## 🔐 Encryption Workflow (Multi-Layer Security)

| Layer | Algorithm | Purpose |
|--------|-------------|-----------|
| **Layer 1** | **RSA (Asymmetric Encryption)** | Encrypts the AES session key before sending it to the receiver. |
| **Layer 2** | **AES (Symmetric Encryption)** | Encrypts and decrypts the actual chat messages. |
| **Layer 3** | **Base64 Encoding** | Ensures encrypted data is safely transmitted as text. |

---

## 🖥️ Network Setup (Single Network / LAN)
This project is designed to run within a **single local network (LAN)** such as a Wi-Fi network or Ethernet connection.

### Example Setup
| Role | Device | IP Address |
|-------|----------|-------------|
| Server | PC 1 | 192.168.1.10 |
| Client 1 | PC 2 | 192.168.1.11 |
| Client 2 | PC 3 | 192.168.1.12 |

All devices must be on the same network.  
Clients connect to the server using its **local IP address** and the defined port (`12345`).

---

## ⚙️ How It Works

### 🧾 Step 1 — Generate Keys
Each user generates a **public** and **private** RSA key pair:
