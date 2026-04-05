from abc import ABC, abstractmethod

class ExcelReder(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReder):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass
class TC1(Browser):
    def startBrowser(self):
        print("starting")


    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")


    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()

tc1 = TC1()
tc1.runTc()