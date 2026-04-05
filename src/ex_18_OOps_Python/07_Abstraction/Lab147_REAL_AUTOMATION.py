from abc import ABC, abstractmethod

class BrowserManager(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stop command, common")


class chromeBrowser(BrowserManager):
    def start(self):
        # t = ChromeDriver()
        print("We are starting the chrome")

tc = chromeBrowser()
tc.start()