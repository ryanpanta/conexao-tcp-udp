from socket import *
import os

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = input("Digite um comando (ls, cd, pwd, scp) ou 'sair' para encerrar: ")
    #clientSocket.send(message.encode())
    if message == 'sair':
        clientSocket.send(message.encode())
        break

    elif message.startswith('scp'):
        try:
            print("O scp foi escolhido")
            file = message.split(' ')[1]
            base_file = os.path.basename(file)
            #cliente chegar aqui?
    
            clientSocket.settimeout(5)
            clientSocket.send(message.encode())
            clientSocket.send("Pronto para receber".encode())
           
            size_file = clientSocket.recv(1024)
            size = int(size_file.decode())
            clientSocket.send("Pronto para receber".encode())
    
            tamanho_max = clientSocket.recv(1024)
            tamanho = int(tamanho_max.decode())
            
            print(f"Tamanho do arquivo a ser escrito em bytes: {size}")
            print(f"Tamanho máximo dos dados recebidos: {tamanho}")
            
            clientSocket.send("Pronto para receber".encode())
           
            with open(base_file, 'wb') as f:
                while size > 0:
                    if size < tamanho:
                        tamanho = size
                    data = clientSocket.recv(tamanho)
                    f.write(data)
                    clientSocket.send("ACK".encode())
                    size -= len(data)
            # Recebe a mensagem de sucesso com o tamanho do arquivo
            success_message = clientSocket.recv(1024)
            print(success_message.decode())

        except IndexError:
            print("É necessário especificar o arquivo para transferência.")
        except timeout:
            print("Tempo limite de resposta excedido. Tente novamente.")
        except ConnectionResetError:
            print("Conexão foi encerrada pelo servidor.")
            break
        except ConnectionAbortedError:
            print("Conexão foi encerrada pelo servidor.")
            break
        except UnicodeDecodeError:
            print("Erro ao decodificar mensagem do servidor.")
            break
    else:
        clientSocket.send(message.encode())
        modifiedMessage = clientSocket.recv(3072)
        print(modifiedMessage.decode())
    

clientSocket.close()
