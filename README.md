# PortScan GUI - Scanner de Portas com Interface Web

## 📌 Descrição
PortScan GUI é uma ferramenta simples e interativa para escanear portas abertas em um IP ou domínio especificado pelo usuário. Utiliza Python, `socket` para a varredura, `threading` para otimização e `Streamlit` para a interface web.

## 🚀 Funcionalidades
- Interface web intuitiva usando Streamlit.
- Insira um IP ou domínio e selecione portas específicas para análise.
- Exibição de portas abertas diretamente na interface.
- Explicação educativa sobre portas e redes.
- Registro dos escaneamentos em um arquivo de log (`scan_log.txt`).

## 📂 Estrutura do Projeto
```
portscan_gui/
│── portscan.py        # Lógica do scanner de portas
│── gui.py             # Interface web com Streamlit
│── requirements.txt   # Lista de dependências
│── README.md          # Documentação do projeto
│── LICENSE            # Licença do projeto
│── docs/              # Pasta para documentação futura
│── assets/            # Ícones ou imagens da interface (se necessário)
│── scan_log.txt       # Arquivo de log com o histórico dos escaneamentos
```

## 🛠️ Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/seuusuario/portscan_gui.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd portscan_gui
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## ▶ Uso
Execute a interface web com o seguinte comando:
```sh
streamlit run gui.py
```
Depois, acesse o navegador no link gerado pelo Streamlit para utilizar a ferramenta.

## 📦 Dependências
As bibliotecas utilizadas estão listadas em `requirements.txt`, incluindo:
- `socket`
- `threading`
- `streamlit`

## 📜 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição
Se desejar contribuir, envie um Pull Request ou abra uma Issue no repositório.

