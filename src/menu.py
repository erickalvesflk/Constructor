from constants import Colors, TARGET_FOLDER_PATH
from subprocess import run as runComandCMD
from typing import Literal, TypedDict, Callable
from time import sleep
import data, format, re

class FilePayload(TypedDict):
    name: str
    desc: str

COOLDOWN = data.configs["cooldown"]
FLAG = data.configs["flag"]
STUDENTNAME = data.configs["studentName"]
type menu_response_type = tuple[Literal["exit"]] | tuple[Literal["invalid-response"]] | tuple[Literal["config"]] | tuple[Literal["create-file"], FilePayload]
type config_response_type = Literal["exit"] | Literal["fail-apply"] | Literal["sucess-apply"]

class RenderGraphics:
    """
        Classe que agrupa métodos que facilitam a criação de componentes estilizados para a interface.
    """
    @staticmethod
    def doPrint(arg):
        texto = str(arg)
        print(arg, end=f"{Colors.RESET}")


    @staticmethod
    def removeAnsi(text):
        ansi_pattern = re.compile(r'\033\[[0-9;]*m')
        return ansi_pattern.sub('', text)


    @staticmethod
    def drawBoxInstructions(title, color, *texts):
        """
        Desenha uma caixa feita com linhas de cor [color],
        apresentando o título e os textos.
        """

        cleanTexts = [RenderGraphics.removeAnsi(text) for text in texts]

        innerWidth = max(len(text) for text in cleanTexts)

        RenderGraphics.doPrint(f"{color}{title}\n")
        RenderGraphics.doPrint(f"{color}┌{'─' * (innerWidth + 2)}┐\n")

        for text, cleanText in zip(texts, cleanTexts):
            RenderGraphics.doPrint(
                f"{color}│ {text}{' ' * (innerWidth - len(cleanText))} {color}│\n"
            )

        RenderGraphics.doPrint(f"{color}└{'─' * (innerWidth + 2)}┘\n\n")


    @staticmethod
    def requestInput(text : str,color = Colors.CYAN):
        return input(fr"{color}- {text}: {Colors.RESET}")
    

    @staticmethod
    def requestConfigInput(name : str):
        return input(f"{Colors.MAGENTA}- Informe o novo valor para {Colors.LIGHT_CYAN} {name}{Colors.MAGENTA}: {Colors.RESET}")
    

    @staticmethod
    def alert_menu_change(menu_response : menu_response_type):
        """
            Exibe por um intervalo de [cooldown]s um alerta sobre a dinâmica de interfaces
        """
        pattern: dict[str, Callable[[], None]] = {
            "exit": lambda: RenderGraphics.doPrint(f"{Colors.RED}- Programa encerrado!\n"),
            "config": lambda: RenderGraphics.doPrint(f"{Colors.MAGENTA}- Abrindo configurações...\n"),
            "invalid-response": lambda: RenderGraphics.doPrint(f"{Colors.RED}- Input Inválido...\n"),
            "create-file": lambda: RenderGraphics.doPrint(f"{Colors.GREEN}- Criando arquivo...\n")
        }

        try:
            pattern[menu_response]()
        except TypeError:
            pattern[menu_response[0]]()

        sleep(COOLDOWN)

    def alert_config_change(config_response : config_response_type):
        """
            Exibe por um intervalo de [cooldown]s um alerta sobre a dinâmica de interfaces
        """
        pattern: dict[str, Callable[[], None]] = {
            "exit": lambda: RenderGraphics.doPrint(f"{Colors.RED}- Saindo das Configurações!\n"),
            "sucess-apply": lambda: RenderGraphics.doPrint(f"{Colors.GREEN}- Configuração aplicada com sucesso!\n"),
            "fail-apply": lambda: RenderGraphics.doPrint(f"{Colors.RED}- Falha ao configurar\n"),
        }

        pattern[config_response]()
        sleep(COOLDOWN)

    @staticmethod
    def instruct(key : str, desc : str, inverted = False) -> str:
        """
            Returna o texto estilizado: "- Infome ([key]) para [desc]"
        """
        color_1 = Colors.MAGENTA if inverted else Colors.LIGHT_CYAN
        color_2 = Colors.LIGHT_CYAN if inverted else Colors.MAGENTA

        return f"{color_1}- Informe ({color_2}{key}{color_1}) para {desc}"



class Menu:
    """
        Classe que armazena métodos para exbição e dinâmica de interfaces pro programa
    """

    @staticmethod
    def initCore():
        """
            Inicia o sistema de interfaces do menu
        """
        while (True):
            menu_response = Menu.mainInterface()

            RenderGraphics.alert_menu_change(menu_response)

            if menu_response == "restart": continue
            if menu_response == "exit": break

            if menu_response == "config":
                runComandCMD("cls",shell=True)
                while True:
                    config_response = Menu.config_interface()
                    RenderGraphics.alert_config_change(config_response)

                    if config_response == "exit": break

            if menu_response[0] == "create-file": 
                format.createScript(data.configs["language"],menu_response[1]["name"],menu_response[1]["desc"],TARGET_FOLDER_PATH)

            runComandCMD("cls",shell=True)



    @staticmethod
    def config_interface() -> config_response_type:
        """
            Método que exibe a interface de configuração do programa, retornando a resposta do client.
        """
        RenderGraphics.doPrint(f"{Colors.YELLOW}=== GERADOR DE ARQUIVOS (Configurações) === \n\n")

        RenderGraphics.drawBoxInstructions("Configurações :", Colors.CYAN,
            f" - Linguagem ({Colors.MAGENTA}l{Colors.LIGHT_CYAN}) : {data.configs["language"]}",
            f" - Nome do Usuário ({Colors.MAGENTA}u{Colors.LIGHT_CYAN}) : {data.configs["studentName"]}",
            f" - Tamanho maximo de linha ({Colors.MAGENTA}t{Colors.LIGHT_CYAN}) : {data.configs["limitDescPerLine"]}",
            f" - Cooldown ({Colors.MAGENTA}c{Colors.LIGHT_CYAN}) : {data.configs["cooldown"]}",
            f' - flag ({Colors.MAGENTA}f{Colors.LIGHT_CYAN}) : "{data.configs["flag"]}"'
        )
        
        print(f"{RenderGraphics.instruct(FLAG,"para retornar ao menu.",True)}")
        response = RenderGraphics.requestInput(f"Informe a configuração que deseja alterar")

        config_commands = {
            "l" : ["language"],
            "u" : ["studentName",str],
            "t" : ["limitDescPerLine",int],
            "c" : ["cooldown",float],
            "f" : ["flag",str],
        }

        if (response == FLAG):
            return "exit"
        
        if (response == "l"):
            RenderGraphics.doPrint(f"\n{Colors.LIGHT_CYAN}| Moldes disponíveis : \n")

            for pattern in data.dataConfigs["patterns"].keys():
                RenderGraphics.doPrint(f"{Colors.LIGHT_CYAN}| - {pattern} \n")

            language_value = RenderGraphics.requestInput("Informe o molde que deseja utilizar")

            operation = data.changeLanguage(language_value)

            if (operation):
                return "sucess-apply"
            else:
                return "fail-apply"
        
        if (response in list(config_commands.keys())):
            newValue = RenderGraphics.requestConfigInput(response)
            change_value_sucess = data.saveConfig(config_commands[response][0],config_commands[response][1](newValue))

            if change_value_sucess:
                return "sucess-apply"
            else:
                return "fail-apply"



    @staticmethod
    def mainInterface() -> menu_response_type:
        """
            Método que exibe a interface principal do programa, retornando a resposta do client.
        """
        RenderGraphics.doPrint(f"{Colors.YELLOW}=== GERADOR DE ARQUIVOS ({data.configs["language"].capitalize()}) === \n\n")

        RenderGraphics.drawBoxInstructions("Instruções : ", Colors.MAGENTA,
            RenderGraphics.instruct(FLAG, "para encerrar o programa."),
            RenderGraphics.instruct("c", "para acessar as configurações."),
        )

        response_first = RenderGraphics.requestInput("Informe o nome do projeto")

        if (not response_first):
            return ("invalid-response")

        if response_first == FLAG:
            return ("exit")
        
        if response_first == "c":
            return ("config")
        
        response_second = RenderGraphics.requestInput("Informe a descrição desse projeto")

        return ("create-file",{"name": response_first, "desc": response_second})

Menu.initCore()