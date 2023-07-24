from socket import *
import os
import time


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    #print(f"Nova conexão estabelecida com {addr} ")

    while True:
        message = connectionSocket.recv(1024)
        command = message.decode()

        if command == 'sair':
            break

        elif command == 'ls':
            output = '\n'.join(os.listdir())
            
        elif command.startswith('cd'):
            try:
                directory = command.split(' ')[1]
                #directory.strip()
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
                    #servidor chegar aqui?
                    
                    confirmation = connectionSocket.recv(1024).decode()
                    if confirmation == "Pronto para receber":
                        connectionSocket.send(str(size).encode())
                        confirmation = connectionSocket.recv(1024).decode()
                        if confirmation == "Pronto para receber":
                            tamanho = 1024
                            connectionSocket.send(str(tamanho).encode())            
                            confirmation = connectionSocket.recv(1024).decode()
                            if confirmation == "Pronto para receber":
                                with open(file, 'rb') as f:
                                    while size > 0:
                                        data = f.read(tamanho)
                                        connectionSocket.send(data)
                                        connectionSocket.recv(1024)
                                        size -= len(data)
                                # Adiciona a mensagem de sucesso com o tamanho do arquivo
                                output = "Arquivo copiado com sucesso."
                            else:
                                output = "Falha ao confirmar recebimento do cliente."
                        else:
                            output = "Falha ao confirmar recebimento do cliente."
                    else:
                        output = "Falha ao confirmar recebimento do cliente."
                else:
                    output = "Arquivo não encontrado."
            except IndexError:
                output = "É necessário especificar o arquivo para transferência."

        else:
            output = "Comando inválido."
        connectionSocket.send(output.encode())

    connectionSocket.close()
    print(f"Conexão com {addr} encerrada.")

serverSocket.close()
