# encoding:utf-8

from configparser import ConfigParser
from config.VarConfig import pageElemenetLocatorPath

class ParaseCofigFile:
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElemenetLocatorPath)

    def getItemSection(self, sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionsValue(self, sectionName, optionName):
        value = self.cf.get(sectionName, optionName)
        return value

if __name__ == '__main__':
    pc = ParaseCofigFile()
    print(pc.getItemSection('126main_login'))
    print(pc.getOptionsValue('126mail_login', 'loginpage.frame'))

