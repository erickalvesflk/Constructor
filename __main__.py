# IMPORTAÇÕES
from textwrap import dedent
from time import sleep, strftime
from colorama import Fore, Style, init
import os, json, format, data
init(autoreset=True) # Inicializando o colorama
# VARIÁVEIS
    
path = os.getcwd()
executing = True

COLORS = data.COLORS
cooldown = data.configs["cooldown"]
flag = data.configs["flag"]
studentName = data.configs["studentName"]

# PROGRAMA

def drawBoxInstructions (title, color, *texts):
    maxWidth = len(texts[0])

    for text in texts :
        if (maxWidth < len(text)):
            maxWidth = len(text)
    
    print(f"{color}{title} \n",end=COLORS["RESET"])
    print(f"{color}|"+ ("‾" * (maxWidth + 5)) + "|\n",end=COLORS["RESET"])

    for text in texts :
        print(f"{color}| {text}"+ (" " * (maxWidth - len(text) + 14)) + "|\n",end=COLORS["RESET"])

    print(f"{color}|"+ ("_" * (maxWidth + 5)) + "|\n\n",end=COLORS["RESET"])


while executing :

    print(f"{COLORS["AMARELO"]}=== GERADOR DE ARQUIVOS ({data.configs["language"].capitalize()}) === \n\n",end=COLORS["RESET"])

    drawBoxInstructions("Instruções : ", COLORS["MAGENTA"],
        f" - Informe{COLORS["CIANO"]} {flag}{COLORS["MAGENTA"]} para encerrar o programa",
        f" - Informe{COLORS["CIANO"]} c{COLORS["MAGENTA"]} para acessar as configurações"
    )

    userNameAq = input(f"{COLORS["CIANO"]}- Informe o nome do projeto: {COLORS["RESET"]}")

    if userNameAq == flag:
        executing = False
        print(f"\n{COLORS["VERMELHO"]}- Programa encerrado!",end=COLORS["RESET"])
        sleep(cooldown)
        break

    elif userNameAq == "c":
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"{COLORS["AMARELO"]}=== GERADOR DE ARQUIVOS (Configurações) === \n\n",end=COLORS["RESET"])

            drawBoxInstructions("Configurações :", COLORS["LCIANO"],
                f" - Linguagem ({COLORS["MAGENTA"]}l{COLORS["LCIANO"]}) : {data.configs["language"]}",
                f" - Nome do Usuário ({COLORS["MAGENTA"]}u{COLORS["LCIANO"]}) : {data.configs["studentName"]}",
                f" - Tamanho maximo de linha ({COLORS["MAGENTA"]}t{COLORS["LCIANO"]}) : {data.configs["limitDescPerLine"]}",
                f" - Cooldown ({COLORS["MAGENTA"]}c{COLORS["LCIANO"]}) : {data.configs["cooldown"]}",
                f' - flag ({COLORS["MAGENTA"]}f{COLORS["LCIANO"]}) : "{data.configs["flag"]}"',
            )

            print(f'{COLORS["MAGENTA"]}- Informe ({COLORS["LCIANO"]}0{COLORS["MAGENTA"]}) para voltar a tela principal \n')

            config = input(f"{COLORS["MAGENTA"]}- Informe a configuração que deseja alterar: {COLORS["RESET"]}")

            def newValue(name):
                newValue = input(f"{COLORS["MAGENTA"]}- Informe o novo valor para {COLORS["LCIANO"]} {name}{COLORS["MAGENTA"]}: {COLORS["RESET"]}")

                return newValue
            
            commands = {
                "l" : ["language"],
                "u" : ["studentName",str],
                "t" : ["limitDescPerLine",int],
                "c" : ["cooldown",float],
                "f" : ["flag",str],
            }
            
            if (config in ["u","t","c","f"]):

                value = newValue(config)
                operation = data.saveConfig(commands[config][0],commands[config][1](value))

                if operation:
                    print(f"\n{COLORS["VERDE"]}- A configuração foi salva!",end=COLORS["RESET"])
                else:
                    print(f"\n{COLORS["VERMELHO"]}- Deu erro!",end=COLORS["RESET"])

            elif (config == "0"):
                print(f"\n{COLORS["VERDE"]}- Saindo das configurações!",end=COLORS["RESET"])
                break

            elif (config == "l"):
                print(f"\n{COLORS["LCIANO"]}| Moldes disponíveis : \n",end=COLORS["RESET"])

                for pattern in data.dataConfigs["patterns"].keys():
                    print(f"{COLORS["LCIANO"]}| - {pattern} \n",end=COLORS["RESET"])

                language_value = input(f"\n{COLORS["MAGENTA"]}| - Informe o molde que deseja utilizar :{COLORS["RESET"]}")

                operation = data.changeLanguage(language_value)

                if (operation):
                    print(f"\n{COLORS["VERDE"]}- Molde aplicado!",end=COLORS["RESET"])
                else:
                    print(f"\n{COLORS["VERMELHO"]}- Molde não encontrado...",end=COLORS["RESET"])

            else:

                print(f"\n{COLORS["VERMELHO"]}- Você informou um valor errado",end=COLORS["RESET"])

            sleep(cooldown)

            os.system('cls' if os.name == 'nt' else 'clear')


        os.system('cls' if os.name == 'nt' else 'clear')

        continue
    
    if not(userNameAq):
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    userDescAq = input(f"{COLORS["CIANO"]}- Informe a descrição desse projeto: {COLORS["RESET"]}")

    format.createScript(data.configs["language"],userNameAq,userDescAq,path)
    print(f"\n{COLORS["VERDE"]}- Arquivo {userNameAq.replace(" ","")}.{data.dataConfigs["patterns"][data.configs["language"]]["extension"]} criado!",end=COLORS["RESET"])
    sleep(cooldown)
    
    os.system('cls' if os.name == 'nt' else 'clear')