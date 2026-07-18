from src.data import Config
from src.constants import Colors
from typing import Literal, TypedDict, Callable, Any
import re
from time import sleep
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
        COOLDOWN = Config.getValue("cooldown")

        pattern: dict[str, Callable[[], None]] = {
            "exit": lambda: RenderGraphics.doPrint(f"\n{Colors.RED}- Programa encerrado!\n"),
            "config": lambda: RenderGraphics.doPrint(f"\n{Colors.MAGENTA}- Abrindo configurações...\n"),
            "invalid-response": lambda: RenderGraphics.doPrint(f"\n{Colors.RED}- Input Inválido...\n"),
            "create-file": lambda: RenderGraphics.doPrint(f"\n{Colors.GREEN}- Criando arquivo...\n")
        }

        try:
            pattern[menu_response]()
        except TypeError:
            pattern[menu_response[0]]()

        sleep(COOLDOWN)

    @staticmethod
    def alert_config_change(config_response : config_response_type):
        """
            Exibe por um intervalo de [cooldown]s um alerta sobre a dinâmica de interfaces
        """
        COOLDOWN = Config.getValue("cooldown")

        pattern: dict[str, Callable[[], None]] = {
            "exit": lambda: RenderGraphics.doPrint(f"\n{Colors.RED}- Saindo das Configurações!\n\n"),
            "sucess-apply": lambda: RenderGraphics.doPrint(f"\n{Colors.GREEN}- Configuração aplicada com sucesso!\n\n"),
            "fail-apply": lambda: RenderGraphics.doPrint(f"\n{Colors.RED}- Falha ao configurar\n\n"),
        }

        pattern[config_response]()
        sleep(COOLDOWN)

    @staticmethod
    def sucessFileCreation():
        COOLDOWN = Config.getValue("cooldown")
        RenderGraphics.doPrint(f"{Colors.GREEN}- Arquivo Criado!\n")
        sleep(COOLDOWN)


    @staticmethod
    def instruct(key : str, desc : str, inverted = False) -> str:
        """
            Returna o texto estilizado: "- Infome ([key]) para [desc]"
        """
        color_1 = Colors.MAGENTA if inverted else Colors.LIGHT_CYAN
        color_2 = Colors.LIGHT_CYAN if inverted else Colors.MAGENTA

        return f"{color_1}- Informe ({color_2}{key}{color_1}) para {desc}"