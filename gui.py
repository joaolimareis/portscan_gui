import streamlit as st
import threading
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Garante que o diretório do script está no caminho do Python
from portscan import scan_ports

stop_scan = False  # Flag para parar o escaneamento
open_ports = []  # Lista global para armazenar portas abertas

def log_scan(ip, ports, open_ports):
    """Registra os resultados do escaneamento em um arquivo de log."""
    with open("scan_log.txt", "a") as log_file:
        log_file.write(f"[{datetime.now()}] Escaneamento realizado em {ip}\n")
        log_file.write(f"Portas analisadas: {', '.join(map(str, ports))}\n")
        log_file.write(f"Portas abertas: {', '.join(map(str, open_ports)) if open_ports else 'Nenhuma'}\n")
        log_file.write("-" * 50 + "\n")

def start_scan(ip, ports):
    """Inicia a varredura de portas."""
    global stop_scan, open_ports
    stop_scan = False  # Reseta a flag de parada
    open_ports = []  # Reseta a lista de portas abertas
    result_text = f"🔍 Escaneando {ip} nas portas: {', '.join(map(str, ports))}"
    
    for port in ports:
        if stop_scan:
            result_text = "Escaneamento interrompido."
            return result_text, []
        
        if scan_ports(ip, port, port):
            open_ports.append(port)
    
    if open_ports:
        result_text = f"✅ Escaneamento concluído para {ip}. Portas abertas: " + ", ".join(map(str, open_ports))
    else:
        result_text = f"❌ Nenhuma porta aberta encontrada para {ip}."
    
    log_scan(ip, ports, open_ports)  # Registra no log
    return result_text, open_ports

def stop_scan_process():
    """Interrompe o escaneamento."""
    global stop_scan
    stop_scan = True

# Interface Web com Streamlit
st.set_page_config(page_title="Scanner de Portas", layout="centered")

st.title("🔍 Scanner de Portas - Aprenda Sobre Redes")
st.write("Este scanner de portas permite que você insira um IP/Domínio e portas específicas para verificar quais estão abertas.")

st.divider()

ip = st.text_input("🌐 Digite o IP ou domínio:", placeholder="ex: google.com")
manual_ports = st.text_input("🔢 Portas (separadas por vírgula):", placeholder="ex: 80, 443, 8080")

if manual_ports:
    try:
        ports = [int(port.strip()) for port in manual_ports.split(',')]
    except ValueError:
        st.error("⚠️ Insira portas válidas separadas por vírgula.")
        ports = []
else:
    ports = []

start_button = st.button("🚀 Iniciar Escaneamento", use_container_width=True)

if start_button:
    if ip and ports:
        st.info(f"🛠️ Configuração do escaneamento: IP/Domínio: {ip} | Portas analisadas: {', '.join(map(str, ports))}")
        result_text, open_ports = start_scan(ip, ports)
        st.success(result_text)
        
        if open_ports:
            st.subheader("✅ Portas abertas:")
            st.write(open_ports)
        
        # Adicionando explicação educacional sobre redes e portas
        st.divider()
        st.subheader("📖 O que são portas e como funcionam?")
        st.write("As portas são pontos de comunicação usados pelos dispositivos para enviar e receber dados na rede.")
        st.write("Cada serviço na internet utiliza portas específicas para funcionar. Exemplos comuns incluem:")
        st.markdown("- **80 (HTTP)**: Usada para carregar páginas web não seguras.")
        st.markdown("- **443 (HTTPS)**: Para páginas web seguras com criptografia SSL/TLS.")
        st.markdown("- **22 (SSH)**: Para acesso remoto seguro a servidores.")
        st.markdown("- **25 (SMTP)**: Para envio de e-mails.")
        st.write("Saber quais portas estão abertas pode ajudar na segurança de redes, prevenindo acessos indesejados.")
        
    else:
        st.error("❌ Por favor, insira um IP/Domínio e pelo menos uma porta.")

if stop_scan:
    st.warning("⏹️ Escaneamento interrompido.")
else:
    if start_button and open_ports:
        st.stop()
    elif start_button:
        stop_button = st.button("⏹️ Parar Escaneamento", use_container_width=True)
        if stop_button:
            stop_scan_process()
            st.experimental_rerun()
