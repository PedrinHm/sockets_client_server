import socket
import threading

def handle_client(conexao, addr):
    print(f"Conectado por {addr}")

    def receive_messages():
        while True:
            data = conexao.recv(1024)
            if not data:
                break
            print(f"Pedro diz: {data.decode()}")

    def send_messages():
        while True:
            message = input()
            conexao.sendall(message.encode())

    thread_receive = threading.Thread(target=receive_messages)
    thread_send = threading.Thread(target=send_messages)

    thread_receive.start()
    thread_send.start()

    thread_receive.join()
    thread_send.join()

    print(f"Conexão com {addr} encerrada.")
    conexao.close()

def accept_connections(server_socket):
    while True:
        conexao, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conexao, addr))
        thread.start()

def start_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Servidor escutando em {host}:{port}")
        accept_connections(server_socket)

if __name__ == '__main__':
    start_server()