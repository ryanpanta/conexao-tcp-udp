	
# Implementação Cliente-Servidor TCP e UDP em Python utilizando Sockets e Biblioteca OS

**Introdução**

Este projeto foi desenvolvido como parte da disciplina de Redes de Computadores e Internet, com o intuito de aprofundar os conceitos de comunicação entre Cliente e Servidor utilizando os protocolos TCP e UDP. A implementação foi realizada em Python, fazendo uso da biblioteca "os" para funções específicas e utilizando sockets para estabelecer a conexão entre os dispositivos.

**Descrição**

O foco deste projeto foi criar um sistema Cliente-Servidor que suportasse comunicação bidirecional por meio dos protocolos TCP (Transmission Control Protocol) e UDP (User Datagram Protocol). Ambos os protocolos são amplamente utilizados em redes de computadores, e esta implementação permite explorar suas particularidades e diferenças de funcionamento. Também como objetivo do trabalho é permitir que o cliente se comunique com o servidor através de quatro comandos principais: ls, cd, pwd e scp. Esses comandos foram inspirados nos comandos já existentes no sistema operacional Linux e têm funcionalidades similares.

**Funcionalidades:**

**TCP (Transmission Control Protocol):**

Estabelecimento da conexão: O Cliente inicia uma solicitação de conexão com o Servidor por meio de um socket TCP.   
Troca de mensagens: Após o estabelecimento da conexão, ambas as partes podem enviar e receber mensagens por meio do socket.  
Encerramento da conexão: Tanto o Cliente quanto o Servidor podem finalizar a comunicação de forma ordenada, seguindo um procedimento de encerramento adequado.  

**UDP (User Datagram Protocol):**

Comunicação sem conexão: Ao contrário do TCP, não é necessário estabelecer uma conexão prévia antes de enviar mensagens. O Cliente envia pacotes independentes, e o Servidor responde diretamente a partir do endereço de origem.  
Baixa sobrecarga: O UDP é adequado para aplicações onde a perda ocasional de pacotes não compromete a integridade dos dados, e a velocidade é prioritária em relação ao controle de fluxo.  

**Comandos Implementados:**

O sistema Cliente-Servidor também suporta a execução de comandos similares aos do sistema operacional Linux. Os seguintes comandos foram implementados:

**ls**: O Cliente envia o comando "ls" para o Servidor, que responde com uma listagem de todos os arquivos no diretório onde se encontra.  
**cd**: Quando o Cliente envia o comando "cd", o Servidor recebe o diretório desejado e altera o diretório atual para o diretório especificado.  
**pwd**: Ao receber o comando "pwd", o Servidor retorna o diretório atual em que se encontra.  
**scp**: Ao enviar o comando "scp <caminho-do-arquivo>", o Cliente solicita ao Servidor que copie o arquivo do caminho especificado para a máquina cliente.  


**Como executar:**

Certifique-se de ter o Python instalado em sua máquina.  
Faça o download ou clone o repositório em seu computador.  
Acesse a pasta do projeto e escolha o protocolo desejado no sub-diretório.    
Selecione o arquivo _Server.py para fazer a alteração da porta desejada e execute-o para iniciar o Servidor.  
Em seguida, execute o arquivo _Client.py com o IP e a Porta do Servidor em um terminal distinto para iniciar o Cliente.  
O Servidor processará os comandos do Cliente e responderá de acordo.  

**Observações:**

É importante ressaltar que este projeto foi desenvolvido com fins educacionais, visando a compreensão dos conceitos básicos de comunicação Cliente-Servidor e o funcionamento dos comandos de sistema. Não é recomendado para uso em ambiente de produção.  
Para testar a aplicação em diferentes dispositivos, é necessário garantir que o endereço IP e a porta utilizados estejam configurados corretamente.  

Sinta-se à vontade para contribuir com melhorias e extensões neste projeto!