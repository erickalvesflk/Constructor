from src.data import Config
from time import strftime
from unicodedata import normalize

class Formater:
    
    @staticmethod
    def removeAccents(desc : str) -> str:
        desc_nomalized = normalize("NFD",desc)
        return desc_nomalized.encode("ascii","ignore").decode("utf-8")

    @staticmethod
    def format_desc(desc : str, comment: str):
            desc_without_accents = Formater.removeAccents(desc)
            desc_formated = """"""
            
            for i in range(len(desc_without_accents)):
                letter = desc_without_accents[i]
                desc_formated += letter           

                if i%Config.getValue("limitDescPerLine") == 0 and i != 0 :
                    if letter != " " and desc[i+1] != " ":
                        desc_formated  += "-"

                    desc_formated += f"\n{comment} "

            return desc_formated

class FileCrator:

    @staticmethod
    def createScript(archiveType:str, nameProject:str, desc:str,path) -> bool:
        """
        Cria o texto do arquivo, informe a linguagem, nome do projeto e a descrição.
        """
        
        PATTERN = Config.getProgamingLanguages(archiveType)
        RAW_TEXT = PATTERN["template"]
        
        FORMAT_COMMANDS = {
            "!n" : '"'+nameProject.replace(" ","")+'"',
            "!s" : Config.getValue("studentName"),
            "!t" : strftime('%d/%m/%Y'),
            "!d" : Formater.format_desc(desc, PATTERN["comment"]),
            "!f" : nameProject,
            "!T" : f'"=== {nameProject} ==="',
            "!v" : '" "',
            "!+" : "!"
        }
        
        script : str = ""
        extraCommandIndex = -1

        for i in range(len(RAW_TEXT)-1):

            if (i == extraCommandIndex):
                continue
            
            c = RAW_TEXT[i]

            if (c == "!") :
                script += FORMAT_COMMANDS["!"+RAW_TEXT[i+1]]
                
                extraCommandIndex = i + 1
                continue

            script += c

        with open(path+f"\\{nameProject.replace(" ","")}.{PATTERN["extension"]}", "w", encoding="utf-8") as arquive:
            arquive.write(script)
            arquive.close()
            
            return True