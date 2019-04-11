from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
selenium_grid_url = "http://localhost:4444/wd/hub"
# Create a desired capabilities object as a starting point.
# capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
# capabilities = DesiredCapabilities.CHROME.copy()


capabilities['platform'] = "windows"
capabilities['build'] = 12001

# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                          command_executor=selenium_grid_url)

driver.get("http://example.com")
driver.implicitly_wait(10)
import time
time.sleep(8)
driver.quit()
