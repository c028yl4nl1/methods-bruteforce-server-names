import socket
from  re import search
from requests import options

host = input('digite o Host: ').lstrip()


listar = ['ips_naõ remove essa configuração']
lista_names_serves = open('lista.txt','r')
##### hábil ###*###
for names_servidor in lista_names_serves:
    names_serve = names_servidor.lstrip().rstrip()
    try:
        nome = socket.gethostbyname(f'{names_serve}.{host}')
        if search(str(nome) , str(listar)):
            pass
        else:
            listar.append(nome)
            print(f'host Encontrado:{names_servidor}.{host} : IP: {nome}')
            
            #print(listar)
            
    except:
        pass                
for servers in listar:
    #### configurando a conexão #####
    http_80 = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try:
        http_exe = http_80.connect_ex((servers,80))
    except:
        pass
    else:
        print('Completando o handshake com http Port: 80')
    if http_exe == 0:
        print('handshake success  :)  ')
        try:
            olhar = options(f'http://{str(servers)}/index.html')
            
            try:
                print(f"\033[32mServer : {servers}\nMetodos aceitos {olhar.headers['Allow']}")
            except KeyError:
                print(f'\033[31mNão foi possível Host:  {servers}\n')
        except:
            pass            
    else:
        print('handshake failed :(  ')                 