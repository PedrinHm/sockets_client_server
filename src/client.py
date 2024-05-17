import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print(f"Servidor: {message.decode()}")

def send_messages(client_socket):
    while True:
        message = input("")
        if message.lower() == 'sair':
            client_socket.close()
            break
        client_socket.sendall(message.encode())

def start_client(server_host='localhost', server_port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_host, server_port))
        print(f"Conectado ao servidor em {server_host}:{server_port}")

        thread_receive = threading.Thread(target=receive_messages, args=(client_socket,))
        thread_send = threading.Thread(target=send_messages, args=(client_socket,))

        thread_receive.start()
        thread_send.start()

        thread_receive.join()
        thread_send.join()

if __name__ == '__main__':
    start_client()
