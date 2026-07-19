from src.constants import Colors, TARGET_FOLDER_PATH, menu_response_type, config_response_type
from subprocess import run as runComandCMD
from typing import Literal, TypedDict, Any
from src.data import Config
from src.utils import RenderGraphics
import src.fileCreator as fileCreator

class FilePayload(TypedDict):
    name: str
    desc: str

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
                while True:
                    runComandCMD("cls",shell=True)
                    config_response = Menu.config_interface()
                    RenderGraphics.alert_config_change(config_response)

                    if config_response == "exit": break

            if menu_response[0] == "create-file": 
                op = fileCreator.createScript(Config.getValue("language"),menu_response[1]["name"],menu_response[1]["desc"],TARGET_FOLDER_PATH)
                if op : RenderGraphics.sucessFileCreation()

            runComandCMD("cls",shell=True)



    @staticmethod
    def config_interface() -> config_response_type:
        """
            Método que exibe a interface de configuração do programa, retornando a resposta do client.
        """
        FLAG = Config.getValue("flag")
        RenderGraphics.doPrint(f"{Colors.YELLOW}=== GERADOR DE ARQUIVOS (Configurações) === \n\n")

        RenderGraphics.drawBoxInstructions("Configurações :", Colors.CYAN,
            f" - Modelo ({Colors.MAGENTA}m{Colors.LIGHT_CYAN}) : {Config.getValue("language")}",
            f" - Nome do Usuário ({Colors.MAGENTA}u{Colors.LIGHT_CYAN}) : {Config.getValue("studentName")}",
            f" - Tamanho maximo de linha ({Colors.MAGENTA}t{Colors.LIGHT_CYAN}) : {Config.getValue("limitDescPerLine")}",
            f" - Cooldown ({Colors.MAGENTA}c{Colors.LIGHT_CYAN}) : {Config.getValue("cooldown")}",
            f' - flag ({Colors.MAGENTA}f{Colors.LIGHT_CYAN}) : "{FLAG}"'
        )
        
        print(f"{RenderGraphics.instruct(FLAG,"para retornar ao menu.",True)}")
        response = RenderGraphics.requestInput(f"Informe a configuração que deseja alterar")

        config_commands: dict[str, dict[Literal["key", "type"], Any]] = {
            "m": {"key": "language", "type": str},
            "u": {"key": "studentName", "type": str},
            "t": {"key": "limitDescPerLine", "type": int},
            "c": {"key": "cooldown", "type": float},
            "f": {"key": "flag", "type": str}
        }

        if (response == FLAG):
            return "exit"
        
        if (response == "m"):
            RenderGraphics.doPrint(f"\n{Colors.LIGHT_CYAN}| Moldes disponíveis : \n")

            for language in Config.getAllProgamingLanguages():
                RenderGraphics.doPrint(f"{Colors.LIGHT_CYAN}| - {language} \n")
        
        if (response in list(config_commands.keys())):
            newValue = RenderGraphics.requestConfigInput(response)

            Config.changeValue(config_commands[response]["key"], config_commands[response]["type"](newValue))

        
        operation = Config.changeValue(config_commands[response]["key"], config_commands[response]["type"](newValue))

        if operation: 
            return "sucess-apply"
        else: 
            return "fail-apply"



    @staticmethod
    def mainInterface() -> menu_response_type:
        """
            Método que exibe a interface principal do programa, retornando a resposta do client.
        """
        FLAG = Config.getValue("flag")

        RenderGraphics.doPrint(f"{Colors.YELLOW}=== GERADOR DE ARQUIVOS ({Config.getValue("language").capitalize()}) === \n\n")

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