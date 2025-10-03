import socket
import threading


server_address = ('localhost', 8080)

KNOWLEDGE_FILE = "uni_info.txt"

def load_knowledge_base(file_path):
    knowledge = {}
    try:
        with open(file_path, 'r') as f:
            current_keyword = None
            answer_lines = []
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    continue
                elif ':' in line:
                    parts = line.split(':', 1)
                    keyword = parts[0].strip().lower()
                    answer = parts[1].strip()
                    if current_keyword:
                        knowledge[current_keyword] = " ".join(answer_lines).strip()
                    current_keyword = keyword
                    answer_lines = [answer]
                elif current_keyword and line:
                    answer_lines.append(line)
            if current_keyword:
                knowledge[current_keyword] = " ".join(answer_lines).strip()
    except FileNotFoundError:
        print(f"Error: Knowledge file '{file_path}' not found.")
    return knowledge

knowledge_base = load_knowledge_base(KNOWLEDGE_FILE)

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8').lower()
            if not data:
                break
            print(f"Received from {client_address}: {data}")

            response = "I'm sorry, I don't have information on that."
            for keyword, answer in knowledge_base.items():
                if keyword in data:
                    response = answer
                    break

            client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error with client {client_address}: {e}")
    finally:
        print(f"Connection with {client_address} closed.")
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(server_address)
        server_socket.listen(5)
        print(f"Server listening on {server_address}")

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()