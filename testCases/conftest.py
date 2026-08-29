from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver


#### Pytest HTML--- Report#######

def pytest_configure(config):
        if hasattr(config, '_metadata'):
                config._metadata['project Name']= 'e-commerce site automation'
                config._metadata['module Name']= 'customers'
                config._metadata['tester']='Anmol'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)