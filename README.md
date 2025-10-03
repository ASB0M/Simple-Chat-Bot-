IoBM Chatbot System 💬
Project Overview
This is a simple, socket-based TCP chatbot designed to answer frequently asked questions (FAQs) about the Institute of Business Management (IoBM).

Academic Context
Course: Introduction to Database Systems Lab

Purpose: This project was developed as a course requirement to demonstrate fundamental concepts of data retrieval, client-server communication, and basic database management via a flat-file knowledge base. The primary focus was on implementing the TCP network communication model between the server and the Tkinter GUI client.

The system consists of a Python TCP server that loads a static knowledge base (uni_info.txt) and a Python Tkinter-based GUI client for user interaction. The server uses basic keyword matching to parse user queries and retrieve pre-defined answers from the knowledge file.

Features
Client-Server Architecture: Uses standard Python socket and threading modules for network communication.

GUI Client: A user-friendly interface built with Tkinter for chat interaction.

Static Knowledge Base: A text file (uni_info.txt) serves as the database for easy-to-update and manage knowledge in a keyword-answer format.

Logo Integration: Displays the university logo in the client application (requires Pillow library).

⚙️ Setup and Installation
Prerequisites
You need Python 3.x and the Pillow library installed to run this project. Pillow is necessary for the client to handle and display the iobm_logo.png.

Bash

pip install Pillow
File Structure
Ensure the following files are in the same directory:

/IoBM_Chatbot/
├── client.py
├── server.py
├── uni_info.txt
├── iobm_logo.png
└── README.md (This file)
▶️ How to Run
The system is a classic client-server application and must be started in two steps:

Step 1: Start the Server (The "Database" Host)
Open your terminal or command prompt and run the server file.

Bash

python server.py
You should see the message: Server listening on ('localhost', 8080)

Step 2: Start the Client (The GUI)
Open a second terminal or command prompt and run the client file.

Bash

python client.py
The graphical client window will appear. You can now type your queries (e.g., "what is the mission statement?", "tell me about the bba program") into the text box and press Enter or click Send.

🧠 Knowledge Base Structure
The knowledge base, uni_info.txt, serves as the data source for the chatbot. It uses a simple format for keyword-answer mapping:

# [Optional Section Header]
[keyword]: [Answer text begins here]
[Continuation of answer text on the next line]
To add new questions or answers, simply follow the keyword: answer structure.

⚖️ Legal & Licensing
Code License
The source code for client.py and server.py is licensed under the MIT License.

See the full LICENSE.txt (coming soon) file for details.

⚠️ Intellectual Property Disclaimer
This project is a non-commercial, educational demonstration.

IoBM Logo (iobm_logo.png): The Institute of Business Management (IoBM) logo and any associated branding are the registered trademarks and copyrighted material of IoBM. Its use in this project is strictly for non-commercial, educational demonstration and does not imply endorsement or official affiliation. For any public or commercial use, formal permission must be obtained from the university.

University Data (uni_info.txt): The information in the knowledge base is a compilation of publicly available facts and/or fictional content used for testing the chatbot functionality. Always refer to the official IoBM website for accurate and up-to-date information.
