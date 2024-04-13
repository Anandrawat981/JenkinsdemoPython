import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import os

location = os.getcwd()
print(location)


def pytest_addoption(parser):  # this will get the value from CLI /hooks
    parser.addoption("--browser")

# this will retuen the browser value to browser_setup method
@pytest.fixture(scope='class', autouse=True)
def browser(request):
     return request.config.getoption("--browser")


@pytest.fixture(scope='class', autouse=True)
def setup(browser,request):
    if browser == 'chrome':
        print("**** Chrome browser started ****")
        prefernaces = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("prefs", prefernaces)
        ops.add_argument("--disable-notifications")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ops)

    elif browser == "firefox":
        print("**** Firefox browser started ****")
        preferences = {"download.default_directory": location}
        ops = webdriver.FirefoxOptions()
        ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # "application/msword"
        ops.set_preference("browser.download.manager.showWhenStarting", False)
        ops.set_preference("browser.download.folderList", 2)  # 0-desktop 1=download floder, 2 -desried location
        ops.set_preference("browser.download.dir", location)
        ops.set_preference("pdfjs.disabled", True)
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ops)
    else:
        print("**** Default Edge browser started ****")
        prefernaces = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
        ops = webdriver.EdgeOptions()
        ops.add_experimental_option("prefs", prefernaces)
        web_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=ops)
    request.cls.driver=web_driver
    yield
    web_driver.quit()
    #return driver




'''
@pytest.fixture()
def browsersetup():
    print("**** Chrome browser started ****")
    prefernaces = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", prefernaces)
    ops.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ops)
    return driver
@pytest.fixture()
def firefoxsetup():
    print("**** Firefox browser started ****")
    preferences = {"download.default_directory": location}
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # "application/msword"
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)  # 0-desktop 1=download floder, 2 -desried location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ops)
    return driver '''


############# pytest HTML report ###########
#It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    #config._metadata['Project Name'] = 'nop Commerce'
    #config._metadata['Module Name'] = 'Admin data'
    #config._metadata['Tester'] = 'Anand'
    config.metadata = {
       "Tester": "Anand",
      "Project Name": "Hybrid Framework Practice",
    }

#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



