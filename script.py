import subprocess
import os
import sys
import glob

def configurar_xrdp():
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)

        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'xrdp'], check=True)
        
        subprocess.run(['sudo', 'systemctl', 'enable', 'xrdp'], check=True)
        subprocess.run(['sudo', 'systemctl', 'start', 'xrdp'], check=True)
        
        print("Servidor RDP instalado e configurado corretamente.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configura o servidor RDP: {e}")
        return False

def configurar_pacotes_usbip():
    try:
        subprocess.run(['sudo', 'apt', 'install', 'linux-tools-virtual', 'hwdata'], check=True)
        
        print("Pacotes necessarios para o USBIP instalados corretamente.")
        return True
    except subprocess.CalledProcessError as erro1:
        print(f"Erro ao instalar pacotes: {erro1}")
        return False
    
def instalar_usbip():
    try:
        usbip_path = glob.glob('/usr/lib/linux-tools/*/usbip')[0]
        print(f"Caminho do usbip encontrado: {usbip_path}")
    except IndexError:
        print("Erro: usbip não encontrado no sistema.")
        return False

    #Outra alternativa para criar caminho
    try:
        subprocess.run(['sudo', 'update-alternatives', '--install', '/usr/local/bin/usbip', 'usbip', usbip_path, '20'], check=True)
        print("Caminho alternativo para usbip criado com sucesso.")
    except subprocess.CalledProcessError as erro2:
        print(f"Erro ao criar caminho alternativo para usbip: {erro2}")

    
if __name__ == "__main__":
    if configurar_xrdp():
        print("\nConfiguração do XRDP concluída. Prosseguindo para o USBIP...")
        if configurar_pacotes_usbip():
            print("\nTodas os pacotes necessários foram instalados com sucesso. Finalizando o script.")
            sys.exit(0)
        else:
            print("\nOcorreu um erro fatal na configuração do USBIP. O script será encerrado.")
            sys.exit(1)
    else:
        print("\nOcorreu um erro fatal na configuração do XRDP. O script será encerrado.")
        sys.exit(1)