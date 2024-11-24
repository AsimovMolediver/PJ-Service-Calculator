# PJ-Service-Calculator

# C.D.S - Calculadora de Serviços

## Descrição

O "C.D.S - Calculadora de Serviços" é um aplicativo de calculadora criado com Pygame, destinado a calcular o valor líquido de um serviço após deduzir impostos. O aplicativo permite a entrada de valores monetários, calcula impostos como ISS, INSS e IRPF e exibe o valor líquido restante.

## Requisitos

- Python 3.x
- Pygame (versão 2.0 ou superior)

## Instalação

1. **Clone o Repositório**

   Clone este repositório para o seu ambiente local usando:

   ```bash ou windows
   git clone https://github.com/seu-usuario/seu-repositorio.git
## Interface

- Tela Principal: Exibe uma mensagem de boas-vindas e um botão para acessar a tela de serviços.
- Tela de Serviços: Permite inserir um valor monetário e calcular os impostos. Utilize o ponto . para separar os centavos. Você pode ver o valor líquido após impostos, ISS, INSS e IRPF. Também há opções para limpar a entrada ou sair do programa.

## Construção do Executável

1. Para criar um executável a partir do código Python, use PyInstaller. Certifique-se de que o PyInstaller está instalado:
   
- pip install pyinstaller

2. Para gerar um executável sem console e com um ícone personalizado, execute o comando (Certifique-se de que o arquivo icone.ico está no mesmo diretório que o seu script service.py):

- pyinstaller --noconsole --onefile --icon=icone.ico --name=ZecaCalculinho service.py

## Problemas Comuns

- Aviso de Antivírus: Se o Windows Defender ou outro antivírus sinalizar o executável como potencialmente perigoso, pode ser um falso positivo. Verifique o arquivo em [VirusTotal](https://www.virustotal.com/gui/home/upload) e, se necessário, adicione uma exceção no antivírus.
  
- Execução em Outros PCs: Certifique-se de que todas as dependências (como o Python e Pygame) estejam corretamente instaladas no computador onde o executável será executado.

## Contribuição

- Contribuições são bem-vindas! Se você deseja contribuir com melhorias ou correções, sinta-se à vontade para abrir uma issue ou um pull request.


### Personalização

- **Nome do Repositório**: Substitua `seu-usuario/seu-repositorio` pelo caminho correto do seu repositório no GitHub, se você estiver hospedando o código lá.
- **Nome do Autor**: Substitua `Seu Nome` pelo seu nome real ou nome de usuário.
- **Ícone e Nome do Executável**: Certifique-se de que `icone.ico` e `ZecaCalculinho` estão corretos e substitua conforme necessário.
- Para fazer o Download da versão 2024 só seguir o link: https://drive.google.com/file/d/1_lXjb8tU-90x-r_BHmcovZNyFd8Cp4R4/view?usp=sharing

Se precisar de mais ajustes ou tiver alguma outra questão, estou aqui para ajudar!






