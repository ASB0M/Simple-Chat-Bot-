# 🤖 IoBM Knowledge Base Chatbot

## 🎓 Course Final Project: Intro to Database Systems Lab 🏆

This project serves as the **final project** for the **"Intro to Database Systems Lab"** course. While the application's interface is a client-server chatbot, its core function is to demonstrate **data retrieval, parsing, and query handling**—fundamental skills for any database system. The chatbot acts as a front-end to a simple, text-based **Knowledge Base**, simulating the structure and data-lookup functionality of a live database system.

---

## 📄 Overview

The IoBM Knowledge Base Chatbot is a simple, real-time client-server application built with Python. It allows a user to ask questions about the Institute of Business Management (IoBM).

The project is divided into two main components:

1.  **Server (`server.py`):** Handles network connections, **loads a structured knowledge base (data)** from `uni_info.txt`, and processes incoming queries by matching user input to keywords in the data, then returning the corresponding information.
2.  **Client (`client.py`):** Provides a simple **Tkinter-based GUI** for the user to interact with the bot and displays responses in real-time.

---

## ✨ Database / Data Handling Features

This project focuses on the following concepts relevant to an Introduction to Database Systems:

* **Knowledge Base Parsing:** The `server.py` implements a custom mechanism to parse structured data from the `uni_info.txt` file, simulating the reading and indexing of records from a table or document-based database.
* **Keyword-Based Querying:** Queries are resolved using simple **string matching (simulating a `LIKE` or basic `WHERE` clause)** to demonstrate data lookup logic.
* **Data Storage:** The `uni_info.txt` file serves as the **"database"**, storing various facts and information in a key-value format.
* **Data Integrity (Simple):** The server's loading function attempts to structure and normalize the raw text data before it is made available for querying.

---

## 🛠 Technologies Used

* **Core Language:** **Python 3.x**
* **Networking:** Standard **`socket`** library for TCP/IP client-server communication.
* **Concurrency:** **`threading`** library to allow the server to handle multiple clients and the client to continuously receive messages without freezing the GUI.
* **Client GUI:** **`tkinter`** for the desktop application interface.
* **Image Handling (Client):** **`Pillow (PIL)`** for displaying the IoBM logo.
* **"Database":** **`uni_info.txt`** (a custom text-file knowledge base).

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

3.  **Start the Server** (Must be done first):
    Open a terminal/command prompt, navigate to the project directory, and run:
    ```bash
    python server.py
    ```
    *Output should show: `Server listening on ('localhost', 8080)`*

4.  **Start the Client** (You can run multiple clients):
    Open a *second* terminal/command prompt, navigate to the project directory, and run:
    ```bash
    python client.py
    ```
    *The Tkinter GUI window will open, and the chat area should display: `Connected to the server.`*

---

## 💡 Usage

1.  In the Client window, type your query in the input box (e.g., "What is the mission statement?" or "What are the bba program specializations?").
2.  Click **"Send"** or press **Enter**.
3.  The server will check the message against the keywords in `uni_info.txt` and return the most relevant answer.

---

## 📂 Project Files

| File Name | Description |
| :--- | :--- |
| **`server.py`** | The core application that loads the data, listens for client connections, and handles query processing and response logic. |
| **`client.py`** | The GUI application that allows the user to send messages and displays the bot's responses. |
| **`uni_info.txt`** | The text-based **Knowledge Base** (the "data layer") containing all the IoBM facts and information. |
| `iobm_logo.png` | The image file used in the client GUI. |

---
