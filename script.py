import subprocess
import os
import sys

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

def configurar_usbip():
    try:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'usbip'], check=True)
        
        print("UBIP instalado e configurado corretamente.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar UBIP: {e}")
        return False
    
if __name__ == "__main__":
    if configurar_xrdp():
        print("\nConfiguração do XRDP concluída. Prosseguindo para o USBIP...")
        if configurar_usbip():
            print("\nTodas as configurações foram concluídas com sucesso. Finalizando o script.")
            sys.exit(0)
        else:
            print("\nOcorreu um erro fatal na configuração do USBIP. O script será encerrado.")
            sys.exit(1)
    else:
        print("\nOcorreu um erro fatal na configuração do XRDP. O script será encerrado.")
        sys.exit(1)