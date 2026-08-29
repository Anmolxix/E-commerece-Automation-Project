import configparser

config= configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url= config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
     username = config.get('common info','username')
     return username


    @staticmethod
    def getPassword():
     password = config.get('common info','password')
     return password

class ReadConfig2():
   
    @staticmethod
    def getUsername():
     username = config.get('invalid username','username')
     return username


    @staticmethod
    def getPassword():
     password = config.get('common info','password')
     return password
    