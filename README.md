# PortScan GUI - Scanner de Portas com Interface Gráfica

## Descrição
PortScan GUI é uma ferramenta simples e intuitiva para escanear portas abertas em um IP ou domínio especificado pelo usuário. Utiliza Python, `socket` para a varredura, `threading` para otimização e `tkinter` para interface gráfica.

## Funcionalidades
- Permite inserir um IP ou domínio para escaneamento.
- Define um intervalo de portas para verificar.
- Exibe portas abertas em uma interface amigável.
- Utiliza threads para acelerar o escaneamento.

## Estrutura do Projeto
```
portscan_gui/
│── portscan.py        # Arquivo principal com a lógica do scanner
│── gui.py             # Arquivo para a interface gráfica
│── requirements.txt   # Lista de dependências do projeto
│── README.md          # Documentação inicial
│── LICENSE            # Licença do projeto (opcional)
│── docs/              # Pasta para documentação futura
│── assets/            # Pasta para ícones ou imagens da interface (se necessário)
```

## Instalação
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

## Uso
Execute o arquivo principal:
```sh
python gui.py
```
Insira um IP/Domínio, defina o intervalo de portas e inicie a varredura.

## Dependências
As bibliotecas utilizadas estão listadas em `requirements.txt`, incluindo:
- `socket`
- `threading`
- `tkinter`

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Contribuição
Se desejar contribuir, envie um Pull Request ou abra uma Issue.


