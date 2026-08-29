import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.readProperties import ReadConfig2
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password= ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************ Test_001_LOGIN**************")
        self.logger.info("*************Verifying_Home_PAGE title ***********")

        self.driver = setup
        self.driver.get(self.baseURL) 
        act_title= self.driver.title
        if act_title=="nopCommerce demo store. Login123":
            self.driver.close()
            self.logger.info("*************home page title test is passed ***********")
                         

            assert True
                   

        else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
                self.driver.close()
                self.logger.info("*************home page title test is failed ***********")
                                  
                assert False
                           

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************verifying loging  ***********")
                     

        
        act_title= self.driver.title
        

        if act_title=="Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("*************login test has passed ***********")
                         
            assert True
                        
            

        else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
                self.driver.close()
                self.logger.info("*************login test has failed ***********")
                                             
                assert False
                

class Test_002_login:
      baseURL = ReadConfig.getApplicationURL()
      username= ReadConfig2.getUsername()
      password= ReadConfig2.getPassword()
      logger= LogGen.loggen()


      def test_login2(self,setup):
           self.driver= setup
           self.driver.get(self.baseURL)
           self.lp=Login(self.driver)
           self.lp.setUserName(self.username)
           self.lp.setPassword(self.password)
           self.lp.clickLogin()
           self.logger.info("*************verifying invalid username login test ***********")
                        

           act_title= self.driver.title

           if act_title=="Dashboard / nopCommerce administration":
                self.driver.close()
                self.driver.save_screenshot(".\\Screenshots\\"+"invalid_user.png") 
                assert False
                

           else:
               
                self.driver.close()
                assert True
                
            
      
     
     
     
