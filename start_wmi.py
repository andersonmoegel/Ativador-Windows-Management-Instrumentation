import os
import subprocess
import logging
import time
from datetime import datetime
import win32com.client
import ctypes
import sys

# Função para garantir execução como administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"Erro ao verificar se é administrador: {e}")
        return False

# Função para forçar a execução como administrador
def run_as_admin():
    if not is_admin():
        script = sys.argv[0]
        params = " ".join(sys.argv[1:])
        subprocess.run(['runas', '/user:Administrator', f'python {script} {params}'], shell=True)
        return True
    return False

# Função para registrar logs
def write_log(message):
    log_path = os.path.join("C:\\Windows\\Temp", "wmi_status.txt")
    
    # Verificar se o arquivo já existe e apagar
    if os.path.exists(log_path):
        try:
            os.remove(log_path)
            print("Arquivo de log anterior removido.")
        except Exception as e:
            print(f"Erro ao remover o arquivo de log antigo: {e}")
    
    try:
        # Criar e escrever o novo log
        with open(log_path, "w") as log_file:
            log_file.write(message)
        print(f"Log gravado em {log_path}")
    except Exception as e:
        print(f"Erro ao escrever no arquivo de log: {e}")

# Função para verificar o status do WMI
def check_wmi():
    try:
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        wmi_connect = wmi.ConnectServer()
        return True
    except Exception as e:
        return False

# Função para ativar WMI se necessário
def activate_wmi():
    try:
        subprocess.run(["sc", "start", "winmgmt"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "WMI ativado com sucesso."
    except subprocess.CalledProcessError as e:
        return f"Falha ao ativar o WMI: {e.stderr.decode()}"

# Função para reparar o WMI
def repair_wmi():
    try:
        subprocess.run("winmgmt /verifyrepository", shell=True, check=True)
        subprocess.run("winmgmt /salvagerepository", shell=True, check=True)
        return "WMI reparado com sucesso."
    except subprocess.CalledProcessError as e:
        return f"Erro ao reparar WMI: {e.stderr.decode()}"

# Função principal que controla o fluxo de instalação e diagnóstico
def main():
    # Verificando se o script está rodando como administrador
    if not is_admin():
        write_log("Este script precisa ser executado como administrador.")
        return

    log_message = f"Processo iniciado em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    
    # Diagnóstico do WMI
    wmi_status = check_wmi()
    if wmi_status:
        log_message += "WMI está funcionando corretamente.\n"
    else:
        log_message += "WMI não está funcionando. Tentando reparo...\n"
        repair_message = repair_wmi()
        log_message += repair_message + "\n"

    # Ativando o WMI
    activation_message = activate_wmi()
    log_message += activation_message + "\n"

    # Escrevendo no arquivo de log
    write_log(log_message)
    print(log_message)  # Apenas para depuração ou feedback no console

if __name__ == "__main__":
    main()
