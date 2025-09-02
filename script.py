import subprocess
import os
import sys

def configurar_xrdp():
    try:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'xrdp'], check=True)
        
        subprocess.run(['sudo', 'systemctl', 'enable', 'xrdp'], check=True)
        subprocess.run(['sudo', 'systemctl', 'start', 'xrdp'], check=True)
        
        print("Servidor RDP instalado e configurado corretamente.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configura o servidor RDP: {e}")



def configurar_ubip():
    try:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'ubip'], check=True)
        
        print("UBIP instalado e configurado corretamente.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar UBIP: {e}")

sys.exit(0)