from socket import *
import os

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    # Recebe o comando do cliente
    message, clientAddress = serverSocket.recvfrom(2048)
    command = message.decode()

    if command == 'sair':
        break

    # Executa o comando no servidor e obtém a saída
    if command == 'ls':
        output = '\n'.join(os.listdir())
        
    elif command.startswith('cd'):
        try:
            directory = command.split(' ')[1]
            directory.strip()
            os.chdir(directory)
            output = f"Diretório alterado para: {os.getcwd()}"
        except FileNotFoundError:
            if not directory:
                output = "É possível apenas dar o comando cd + o diretório desejado"
            else:
                output = "Nome do diretório errado"
        except IndexError:
            output = "É possível apenas dar o comando cd + o diretório desejado"
        
    elif command == 'pwd':
        output = os.getcwd()
        
    elif command.startswith('scp'):
        try:
            file = command.split(' ')[1]
            if os.path.isfile(file):
                size = os.path.getsize(file)
                serverSocket.sendto(str(size).encode(), clientAddress)
                tamanho = 1024
                serverSocket.sendto(str(tamanho).encode(), clientAddress)

                with open(file, 'rb') as f:
                    while size > 0:
                        data = f.read(tamanho)
                        serverSocket.sendto(data, clientAddress)
                        serverSocket.recvfrom(1024)
                        size -= len(data)
                f.close()
                output = "Arquivo copiado com sucesso."
            else:
                output = "Arquivo não encontrado."
        except IndexError:
            output = "É necessário especificar o arquivo para transferência."
        
    else:
        output = "Comando inválido."
    serverSocket.sendto(output.encode(), clientAddress)

serverSocket.close()
