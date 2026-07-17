import json
from typing import Literal
from src.constants import CONSTRUCTOR_PATH_FOLDER, Colors
from colorama import Fore, Style

type DataKey = Literal["cooldown"] | Literal["flag"] | Literal["studentName"] | Literal["language"] | Literal["limitDescPerLine"]

class ConfigJsonManipulator:

    def __init__(self):
        self.CONFIG_JSON_PATH = rf"{CONSTRUCTOR_PATH_FOLDER}\config.json"

        with open(self.CONFIG_JSON_PATH,"r",encoding="UTF-8") as dataJson:
            self.dataConfigs = json.load(dataJson)
            dataJson.close()  

    def saveJson(self):

        with open(self.CONFIG_JSON_PATH,"w",encoding="UTF-8") as dataJson:
            json.dump(self.dataConfigs, dataJson, ensure_ascii=False, indent=4)
            dataJson.close()

    def changeValue(self, dataKey : DataKey, newValue : any) -> bool:

        if not (dataKey in self.dataConfigs["config"]): raise KeyError("This key don't exist in the JSON!")
        if (type(self.dataConfigs["config"][dataKey]) != type(newValue)): raise TypeError("The types are diferents")

        if dataKey == "language":
            # Special
            if not(newValue in list(self.dataConfigs["patterns"].keys())): return False

        self.dataConfigs["config"][dataKey] = newValue
        self.saveJson()
        return True


DATA = ConfigJsonManipulator()
class Config:
    
    def __init__(self):
        ...

    @staticmethod
    def getValue(key : DataKey) -> any:
        if(key in DATA.dataConfigs["config"]):
            return DATA.dataConfigs["config"][key]
        else:
            raise KeyError("This key don't exist in the JSON!")
    
    @staticmethod
    def getAllProgamingLanguages() -> list[str]:
        return list(DATA.dataConfigs["patterns"].keys())
    
    @staticmethod
    def getProgamingLanguages(language) -> list[str]:
        if(language in Config.getAllProgamingLanguages()):
            return DATA.dataConfigs["patterns"][language]
    
    @staticmethod
    def changeValue(dataKey : DataKey, newValue : any) -> bool:
        return DATA.changeValue(dataKey, newValue)