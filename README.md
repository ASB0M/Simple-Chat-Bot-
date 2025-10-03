# 🤖 IoBM Knowledge Base Chatbot

## 🎓 Course Final Project: Operating Systems Lab 🏆

This project serves as the **final project** for the **"Operating Systems Lab"** course. It is designed to demonstrate proficiency in core OS-related concepts, particularly **process communication, concurrency management, and network programming (sockets)**. The application is a real-time, multi-client **Client-Server Chatbot** that simulates a crucial OS function: resource sharing and concurrent handling of multiple users.

---

## 📄 Overview

The IoBM Knowledge Base Chatbot is a concurrent client-server application built with Python. It allows multiple users to connect simultaneously and query information about the Institute of Business Management (IoBM) from a shared knowledge base.

The project is divided into two main components:

1.  **Server (`server.py`):** Acts as the **central resource manager**. It handles concurrent client connections using **multithreading**, manages the shared resource (the knowledge base), and processes the communication flow using **TCP sockets**.
2.  **Client (`client.py`):** Provides a simple **Tkinter-based GUI** for the user to initiate a connection, send queries, and receive responses.

---

## ✨ Operating System Concepts Demonstrated

This project focuses on the following concepts critical to an Operating Systems course:

* **Inter-Process Communication (IPC) / Network Programming:** Utilizes the **TCP/IP socket interface** to enable reliable communication between the separate Client and Server programs running as distinct processes.
* **Concurrency and Threading:** The server uses the **`threading`** module to create a dedicated thread (`handle_client`) for *every connected client*. This demonstrates how an OS handles concurrent requests efficiently and prevents one slow client from blocking all others.
* **Resource Management:** The **`knowledge_base`** is a shared data structure loaded into the server's memory. The concurrent access to this shared resource is managed implicitly by the read-only nature of the lookup, but it serves as a basis for discussing critical sections and synchronization.
* **Event Handling:** The client's GUI uses event loops to handle user input and asynchronously receive data from the network, a fundamental pattern in OS design for managing I/O.
* **I/O Operations:** The server performs file I/O to load the data from `uni_info.txt`, showcasing how an application interacts with the file system.

---

## 🛠 Technologies Used

* **Core Language:** **Python 3.x**
* **Networking:** Standard **`socket`** library for **TCP** (Transmission Control Protocol) communication.
* **Concurrency:** **`threading`** library for managing simultaneous client connections.
* **Client GUI:** **`tkinter`** for the desktop application interface.
* **Data Source:** **`uni_info.txt`** (The structured knowledge base).

---

## 🚀 Installation and Setup

### Prerequisites

* **Python 3.x** installed.
* **Pillow** library for the client GUI:
    ```bash
    pip install Pillow
    ```

### Running the Application

1.  **Clone or Download** the project files: `server.py`, `client.py`, and `uni_info.txt`.
2.  Ensure the **logo file `iobm_logo.png`** is in the same directory as `client.py`.

3.  **Start the Server** (Must be done first to open the port):
    Open a terminal/command prompt, navigate to the project directory, and run:
    ```bash
    python server.py
    ```
    *Output should show: `Server listening on ('localhost', 8080)`*

4.  **Start the Client** (You can run multiple instances to test concurrency):
    Open a *second* terminal/command prompt, navigate to the project directory, and run:
    ```bash
    python client.py
    ```
    *The Tkinter GUI window will open, and the chat area should display: `Connected to the server.`*

---

## 💡 Usage

1.  In the Client window, type your query in the input box (e.g., "What are the admission requirements for bba?" or "What is the university's vision?").
2.  Click **"Send"** or press **Enter**.
3.  The server's dedicated thread will process the query and send the response back to your client.

---

## 📂 Project Files

| File Name | Description |
| :--- | :--- |
| **`server.py`** | **OS Focus:** Implements the concurrent TCP server using `threading` to manage multiple client sessions. |
| **`client.py`** | **OS Focus:** The user process that establishes a network connection and provides the GUI for I/O. |
| **`uni_info.txt`** | The structured text file that the server loads as its resource. |
| `iobm_logo.png` | The image file used in the client GUI. |

---
