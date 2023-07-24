from socket import *
import os 

serverName = 'localhost'
serverPort = 12000

# Criação do socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    # Recebe o comando do usuário
    message = input("Digite um comando (ls, cd, pwd, scp) ou 'sair' para encerrar: ")
    # Envia o comando para o servidor
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    if message == 'sair':
        break

    if message.startswith('scp'):
        try:
            file = message.split(' ')[1]
            base_file = os.path.basename(file)
            clientSocket.settimeout(5)  # Define um tempo limite de resposta do servidor

            size_file, _ = clientSocket.recvfrom(2048)
            size = int(size_file.decode())
            print(f"Tamanho do arquivo a ser escrito em bytes: {size}")

            tamanho_max, _ = clientSocket.recvfrom(2048)
            tamanho = int(tamanho_max.decode())
            print(f"Tamanho recebido: {tamanho}")

            with open(base_file, 'wb') as f:
                while size > 0:
                    if size < tamanho:
                        tamanho = size
                    data, _ = clientSocket.recvfrom(tamanho)
                    f.write(data)
                    clientSocket.sendto("ACK".encode(), (serverName, serverPort))
                    size -= len(data)
                    
            success_message = clientSocket.recv(1024)
            print(success_message.decode())
        except IndexError:
            print("É necessário especificar o arquivo para transferência.")
        except timeout:
            print("Tempo limite de resposta excedido. Tente novamente.")

    else:
        # Recebe a resposta do servidor
        modifiedMessage, serverAddress = clientSocket.recvfrom(4096)
        print(modifiedMessage.decode())

# Fecha o socket
clientSocket.close()
