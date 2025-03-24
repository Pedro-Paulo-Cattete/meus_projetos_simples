"""
Login Ambiente Virtual Linux Privado.:
pedro
Senha123!

Entrar no projeto:
cd ~/linux_network_project

source venv/bin/activate

nano config_linux_network.py

chmod +x config_linux_network.py

python3 config_linux_network.py

Testar Projeto no Linux:

1)Errar informações  de Login e Depois por Login correto
Login correto:
Login: admin
Senha: senha123

2) Errar comandos e depois por comandos corretos:
Errado:
show inter fa ces
Certo:
show interfaces

3) Errar comandos de configurar e verificar IP e depois utilizar comandos corretos:
configure enp0s3 ip 192.999.1.10/24
configure enp0s3 ip 192.168.1.10/99
configure exemplo ip 192.168.1.10/24
configure enp0s3 ip 192.168.1.135/24

verify exemplo
verify enp0s3
verify docker0
configure docker0 ip 192.168.1.64/24
"""

import re
import os
import subprocess

# Sistema de login
USERS = {
    "admin": "senha123"  # Usuário e senha
}

def login():
    print("### Welcome to Config Linux Network System ###")
    username = input("login: ")
    password = input("password: ")
    if username in USERS and USERS[username] == password:
        print("\nLogin bem-sucedido!\n")
        return True
    else:
        print("\nUsuário ou senha incorretos!\n")
        return False

# Listar interfaces
def show_interfaces():
    try:
        result = subprocess.check_output("sudo ip -brief addr", shell=True).decode("utf-8")
        interfaces = result.strip().split("\n")
        print("-" * 75)  # Linha de separação antes de exibir as interfaces
        print(f"\n{'Intf':<25}{'IP Address':<20}{'MAC':<20}{'MTU':<6}{'Status':<6}")
        print("-" * 75)  # Linha de separação após o cabeçalho

        for interface in sorted(interfaces):
            fields = interface.split()
            name = fields[0].strip() if len(fields) > 0 else "unknown"  # Definindo diretamente o nome

            # Ignorar interfaces com '@' no nome (geralmente virtuais)
            if "@" in name:
                continue

            # Atribuir valor a 'ip' diretamente se não houver erro
            ip = "N/A"
            try:
                ip = fields[2] if len(fields) > 2 else "N/A"
            except IndexError:
                pass  # Deixe ip como "N/A" se houver erro no índice

            try:
                mac = subprocess.check_output(
                    f"sudo cat /sys/class/net/{name}/address", shell=True
                ).decode("utf-8").strip()
            except Exception:
                mac = "N/A"
            
            try:
                mtu_command = f"sudo cat /sys/class/net/{name}/mtu"
                mtu = subprocess.check_output(mtu_command, shell=True).decode("utf-8").strip()
            except Exception:
                mtu = "N/A"
            
            status = "UP" if "UP" in fields else "DOWN"
            print(f"{name:<25}{ip:<20}{mac:<20}{mtu:<6}{status:<6}")
        print("-" * 75)  # Linha de separação ao final

    except Exception as e:
        print(f"Erro ao listar interfaces: {e}")

# Configurar IP
def configure_interface(interface, ip_address):
    if validate_ip(ip_address):
        try:
            command = f"sudo ip addr add {ip_address} dev {interface}"
            os.system(command)
            print(f"Configuração aplicada: {ip_address} na interface {interface}.")
            result = subprocess.check_output(f"sudo ip addr show {interface}", shell=True).decode("utf-8)")
            if ip_address.split("/") [0] in result:
                print(f"IP {ip_address} configurado corretamente na interface {interface}.")
            else:
                print(f"Falha ao configurar o IP {ip_address} na interface {interface}.")
        except Exception as e:
            print(f"Erro ao configurar IP: {e}")
    else:
        print("Endereço IP inválido!")

# Validação de IP usando regex
def validate_ip(ip):
    regex = r"^(\d{1,3}\.){3}\d{1,3}\/\d{1,2}$"
    if re.match(regex, ip):
        octets = ip.split("/")[0].split(".")
        return all(0 <= int(octet) <= 255 for octet in octets)
    return False

def verify_interface(interface):
    try:
        command = f"sudo /usr/sbin/ip addr show {interface}"
        result = subprocess.check_output(command, shell=True).decode("utf-8")
        print(f"\nDetalhes da interface {interface}:\n{result}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e.output.decode('utf-8')}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Menu principal
def main_menu():
    while True:
        command = input("> ").strip()
        if command == "show interfaces":
            show_interfaces()
        elif command.startswith("configure"):
            parts = command.split()
            if len(parts) == 4 and parts[2] == "ip":
                interface = parts[1]
                ip_address = parts[3]
                configure_interface(interface, ip_address)
            else:
                print("Comando inválido. Use: configure <interface-name> ip <ip-address/mask>")
        elif command.startswith("verify"):
            if len(parts) == 2:
                verify_interface(parts[1])
            else:
                print("Comando Inválido. Use: verify <interface-name>")
        elif command == "exit":
            print("Saindo do sistema...")
            break
        else:
            print("Comando não reconhecido.")

if __name__ == "_main_":
    if login():
        main_menu()