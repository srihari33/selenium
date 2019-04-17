from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
selenium_grid_url = "http://localhost:4444/wd/hub"
# Create a desired capabilities object as a starting point.
# capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
# capabilities = DesiredCapabilities.CHROME.copy()


capabilities['platform'] = "windows"
capabilities['ignoreProtectedModeSettings'] = True
#capabilities['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
#capabilities['INITIAL_BROWSER_URL'] = 'https://www.google.com/'
# capabilities['build'] = 12001

# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                          command_executor=selenium_grid_url)

# driver.implicitly_wait(10)
import time
driver.get("https://www.google.com/")
time.sleep(5)
elems = driver.find_elements_by_xpath("//input[contains(@name, 'q')]")
iframe = driver.find_elements_by_xpath("/iframe")
print('Iframe ===== {}'.format(iframe))
print("Elems  ===== {}".format(elems))
elems[0].send_keys("testing")
driver.find_element_by_xpath("//input[contains(@value, 'Google Search')]").click()
driver.save_screenshot("test.png")
handle = driver.window_handles.index(driver.current_window_handle)
print('Handle ==== {}'.format(handle))

driver.quit()


