#Script para automatizar a configuração da VM para RDP

#Instalação do usbipd-win
function instalar_driver {
    param (
        [string]$caminho_usbipd
    )
try{
    Write-Host "Verificando se o arquivo do instalador existe em $caminho_usbipd..."
    if (-Not (Test-Path $caminho_usbipd)) {
        Write-Host "Arquivo do instalador nao encontrado em $caminho_usbipd."
        return
    }
    else {
        Write-Host "Arquivo do instalador encontrado em $caminho_usbipd."
    }
    Write-Host "Instalando usbipd-win..."
    Start-Process msiexec.exe -ArgumentList "/i $caminho_usbipd /quiet /norestart" -Wait
    Write-Host "usbipd-win instalado com sucesso."
} catch {
        Write-Host "Erro ao instalar usbipd-win: $_"
    }
}

function instalar_launcher {
    param (
        [string]$caminho_usbip_launcher
    )
try{
    write-host "Verificando se o arquivo do instalador existe em $caminho_usbip_launcher..."
    if (-Not (Test-Path $caminho_usbip_launcher)) {
        Write-Host "Arquivo do instalador nao encontrado em $caminho_usbip_launcher."
        return
    }
    else {
        Write-Host "Arquivo do instalador encontrado em $caminho_usbip_launcher."
    }
    Write-Host "Instalando usbip-launcher..."
    Start-Process $caminho_usbip_launcher -Wait
    Write-Host "usbip-launcher instalado com sucesso."
} catch {
        Write-Host "Erro ao instalar usbip-launcher: $_"
}
    
}


$caminho_usbip_launcher = "\\storage1\bibsoft\# PH - Softwares\RaspRDP\USBip-0.9.7.3-x64-release.exe"
$caminho_usbipd = "\\storage1\bibsoft\# PH - Softwares\RaspRDP\usbipd-win_5.2.0_x64.msi"

instalar_driver -caminho_usbipd $caminho_usbipd
instalar_launcher -caminho_usbip_launcher $caminho_usbip_launcher