# encoding:utf-8

from util.ObjectMap import *
from util.ParaseConfigurationFile import ParaseCofigFile


class HomePage:

    def __init__(self):
        self.driver = driver
        self.parasecf = ParaseCofigFile()

    def addressLink(self):
        try:
            locateType, locatorExpression = self.parasecf.getOptionsValue('126mail_homepage',
                                                                          'homePage.addressbook').split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
