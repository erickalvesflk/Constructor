import json, os
from colorama import Fore, Style

dataConfigs = {
    "config": {
        "cooldown": 1.0,
        "flag": "0",
        "language": "visualg",
        "creates": 0
    },
    "patterns": {
       
    }
}

diretorio_script = os.path.dirname(os.path.abspath(__file__))

with open(rf"{diretorio_script}\config.json","r",encoding="UTF-8") as dataJson:
    dataConfigs = json.load(dataJson)
    dataJson.close()

configs = {
    "cooldown" : dataConfigs["config"]["cooldown"],
    "flag" : dataConfigs["config"]["flag"],
    "studentName" : dataConfigs["config"]["studentName"],
    "language" : dataConfigs["config"]["language"],
    "limitDescPerLine" : dataConfigs["config"]["limitDescPerLine"]
}

COLORS = {
    "VERDE" : Fore.GREEN,
    "RESET" : Style.RESET_ALL,
    "VERMELHO" : Fore.RED,
    "AMARELO": Fore.YELLOW,
    "CIANO": Fore.CYAN,
    "LCIANO": Fore.LIGHTCYAN_EX,
    "MAGENTA": Fore.LIGHTMAGENTA_EX
}

def saveJson():
    with open(rf"{diretorio_script}\config.json","w",encoding="UTF-8") as dataJson:
            json.dump(dataConfigs, dataJson, ensure_ascii=False, indent=4)
            dataJson.close()

def saveConfig(dataName : str, value):
    try:

        if not(type(dataConfigs["config"][dataName])) :
            print(f"\n[Erro] - {dataName} não existe em config.json .")
            return False
        
        if (type(dataConfigs["config"][dataName]) != type(value)):
            print(f"\n[Erro] - o valor informado ({type(value)} não é do mesmo tipo que {dataName} {type(dataConfigs["config"][dataName])}.")
            return False
        
        dataConfigs["config"][dataName] = value
        configs[dataName] = value

        saveJson()

        return True
    
    except:

        print("Erro inesperado!")
        return False
    
def changeLanguage(newLanguage : str):

    if not(newLanguage in dataConfigs["patterns"].keys()):
        return False
    
    configs["language"] = newLanguage
    dataConfigs["config"]["language"] = newLanguage

    saveJson()

    return True