import tkinter as tk
from tkinter import scrolledtext, ttk
from PIL import Image, ImageTk  # For handling images (like the logo)
import socket
import threading

class ChatClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("IoBM Chatbot")

        # Load the logo
        try:
            self.logo_image = Image.open("iobm_logo.png")  # Replace with your logo file name
            self.logo_image = self.logo_image.resize((100, 100))  # Adjust size as needed
            self.logo_tk = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = tk.Label(master, image=self.logo_tk)
            self.logo_label.pack(pady=10)
        except FileNotFoundError:
            print("Error: Logo file not found.")

        master.configure(bg="white") # Set main window background to white

        self.chat_area = scrolledtext.ScrolledText(master, width=40, height=20, state=tk.DISABLED, bg="lightblue", fg="black") # Light blue background for chat
        self.chat_area.pack(padx=10, pady=10)

        self.input_frame = tk.Frame(master, bg="white") # Ensure input frame is also white
        self.input_frame.pack(padx=10, pady=5)

        self.message_entry = tk.Entry(self.input_frame, width=30, bg="white", fg="black", insertbackground="black") # Style the entry
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.message_entry.bind("<Return>", self.send_message)

        self.style = ttk.Style()
        self.style.theme_use('clam') # A decent modern theme
        self.style.configure('TButton', background='lightblue', foreground='black', font=('Arial', 10))
        self.style.map('TButton',
                       foreground=[('active', 'white')],
                       background=[('active', 'blue')])

        self.send_button = ttk.Button(self.input_frame, text="Send", command=self.send_message, style='TButton')
        self.send_button.pack(side=tk.RIGHT)

        self.client_socket = None
        self.connect_to_server()

    def connect_to_server(self):
        server_address = ('localhost', 8080)

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(server_address)
            self.display_message("Connected to the server.")

            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()

        except ConnectionRefusedError:
            self.display_message("Connection to the server failed.")

    def display_message(self, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def send_message(self, event=None):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        if self.client_socket:
            try:
                self.client_socket.send(message.encode('utf-8'))
                self.display_message(f"You: {message}")
            except socket.error as e:
                self.display_message(f"Error sending message: {e}")

    def receive_messages(self):
        while True:
            try:
                if self.client_socket:
                    message = self.client_socket.recv(1024).decode('utf-8')
                    if not message:
                        break
                    self.display_message(f"Bot: {message}")
            except socket.error as e:
                self.display_message(f"Error receiving message: {e}")
                break
            except ConnectionResetError:
                self.display_message("Connection to the server was reset.")
                break
        if self.client_socket:
            self.client_socket.close()
            self.display_message("Disconnected from the server.")

def main():
    root = tk.Tk()
    gui = ChatClientGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()