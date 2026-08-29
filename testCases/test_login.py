import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username= "admin@yourstore.com"
    password= "admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL) 
        act_title= self.driver.title
        if act_title=="nopCommerce demo store. Login123":
            self.driver.close()
            assert True

        else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
                self.driver.close()
                assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        
        act_title= self.driver.title
        

        if act_title=="Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            

        else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
                self.driver.close()
                assert False


class Test_002_login:
      baseURL = "https://admin-demo.nopcommerce.com/admin/"
      username= "admin@yourstore.com22"
      password= "admin"

      def test_login2(self,setup):
           self.driver= setup
           self.driver.get(self.baseURL)
           self.lp=Login(self.driver)
           self.lp.setUserName(self.username)
           self.lp.setPassword(self.password)
           self.lp.clickLogin()

           act_title= self.driver.title

           if act_title=="Dashboard / nopCommerce administration":
                self.driver.close()
                assert True
                

           else:
                self.driver.save_screenshot(".\\Screenshots\\"+"invalid_user.png")
                self.driver.close()
                assert False
                
            
      
     
     
     
