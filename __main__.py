# IMPORTAÇÕES
from textwrap import dedent
from time import sleep, strftime
from colorama import init
import os, json, src.fileCreator as fileCreator, src.dataOLD as dataOLD
init(autoreset=True) # Inicializando o colorama
# VARIÁVEIS
    
path = os.getcwd()
executing = True

COLORS = dataOLD.COLORS
cooldown = dataOLD.configs["cooldown"]
flag = dataOLD.configs["flag"]
studentName = dataOLD.configs["studentName"]

# PROGRAMA


while executing :

    print(f"{COLORS["AMARELO"]}=== GERADOR DE ARQUIVOS ({dataOLD.configs["language"].capitalize()}) === \n\n",end=COLORS["RESET"])

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
                f" - Linguagem ({COLORS["MAGENTA"]}l{COLORS["LCIANO"]}) : {dataOLD.configs["language"]}",
                f" - Nome do Usuário ({COLORS["MAGENTA"]}u{COLORS["LCIANO"]}) : {dataOLD.configs["studentName"]}",
                f" - Tamanho maximo de linha ({COLORS["MAGENTA"]}t{COLORS["LCIANO"]}) : {dataOLD.configs["limitDescPerLine"]}",
                f" - Cooldown ({COLORS["MAGENTA"]}c{COLORS["LCIANO"]}) : {dataOLD.configs["cooldown"]}",
                f' - flag ({COLORS["MAGENTA"]}f{COLORS["LCIANO"]}) : "{dataOLD.configs["flag"]}"',
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
                operation = dataOLD.saveConfig(commands[config][0],commands[config][1](value))

                if operation:
                    print(f"\n{COLORS["VERDE"]}- A configuração foi salva!",end=COLORS["RESET"])
                else:
                    print(f"\n{COLORS["VERMELHO"]}- Deu erro!",end=COLORS["RESET"])

            elif (config == "0"):
                print(f"\n{COLORS["VERDE"]}- Saindo das configurações!",end=COLORS["RESET"])
                break

            elif (config == "l"):
                print(f"\n{COLORS["LCIANO"]}| Moldes disponíveis : \n",end=COLORS["RESET"])

                for pattern in dataOLD.dataConfigs["patterns"].keys():
                    print(f"{COLORS["LCIANO"]}| - {pattern} \n",end=COLORS["RESET"])

                language_value = input(f"\n{COLORS["MAGENTA"]}| - Informe o molde que deseja utilizar :{COLORS["RESET"]}")

                operation = dataOLD.changeLanguage(language_value)

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

    fileCreator.createScript(dataOLD.configs["language"],userNameAq,userDescAq,path)
    print(f"\n{COLORS["VERDE"]}- Arquivo {userNameAq.replace(" ","")}.{dataOLD.dataConfigs["patterns"][dataOLD.configs["language"]]["extension"]} criado!",end=COLORS["RESET"])
    sleep(cooldown)
    
    os.system('cls' if os.name == 'nt' else 'clear')