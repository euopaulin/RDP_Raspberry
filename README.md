# 📜 Projeto: Raspberry Pi como Thin Client RDP com Redirecionamento de Webcam via USB/IP  

## 📌 Visão Geral  
Este projeto transforma um **Raspberry Pi** com **Raspberry Pi OS** em um **Thin Client RDP** (Remote Desktop Protocol).  
Além de acessar a sessão remota em uma **VM Windows**, foi configurado o **USB/IP** para permitir o **redirecionamento de dispositivos USB**, como webcams, do Raspberry para a máquina virtual.  

Isso possibilita usar a webcam conectada no Raspberry diretamente dentro da sessão remota Windows.  

---

## ⚙️ Requisitos  

- Foi utilziado o raspberry Pi 3 (funciona em modelos superiores também e é até recomendado, pois terá mais performance).  
- Raspberry Pi OS atualizado.  
- Acesso root/`sudo` no Raspberry.  
- VM Windows (pode ser Hyper-V, VMware, VirtualBox, Proxmox, etc.).  
- Conexão de rede estável.  

---

## 🛠️ Instalação e Configuração  

### 1️⃣ Atualizar pacotes no Raspberry  
```bash
sudo apt update && sudo apt upgrade -y
```

### 2️⃣ Instalar o RDP Client (FreeRDP ou Remmina)  
```bash
sudo apt install freerdp2-x11 remmina -y
```

Exemplo de uso:  
```bash
xfreerdp /u:usuario /p:senha /v:IP_DA_VM
```

---

### 3️⃣ Instalar e configurar o USB/IP no Raspberry  

1. Instale os pacotes:  
```bash
sudo apt install usbip usbipd linux-tools-$(uname -r) linux-cloud-tools-$(uname -r) -y
```

2. Carregue os módulos do kernel:  
```bash
sudo modprobe usbip_host
sudo modprobe vhci_hcd
```

3. Liste os dispositivos USB conectados:  
```bash
usbip list -l
```

4. Exporte o dispositivo desejado (exemplo: webcam):  
```bash
sudo usbip bind -b 1-1.2
```

5. Inicie o daemon:  
```bash
sudo usbipd -D
```

---

## Após ter configurado a Raspberry é necessario também configurar a VM Windows.

### 4️⃣ Conectar o dispositivo USB na VM Windows  

1. No Windows, instale o **driver USB/IP** (pacote disponível no [USB/IP for Windows](https://github.com/dorssel/usbipd-win/releases), baixe a versão mais recente).

- Caso queira uma versão de interface gráfica, baixe e instale a versão com launcher: [Versão com interface grafíca](https://github.com/vadimgrn/usbip-win2)

2. Liste os dispositivos remotos disponíveis:  
```powershell
usbip list -r IP_DO_RASPBERRY
```
3. Anexe o dispositivo:  
```powershell
usbip attach -r IP_DO_RASPBERRY -b 1-1.2
```

---

### 5️⃣ Teste e validação  

- Abra o **Gerenciador de Dispositivos** no Windows → confirme se a **webcam** aparece.  
- Teste em aplicativos como **Câmera, Teams, Zoom, Meet** dentro da sessão RDP.  

---

## 🚀 Resultado  

- Raspberry Pi funcionando como **cliente RDP**.  
- Webcam conectada no Raspberry é usada pela **VM Windows** via **USB/IP**.  

