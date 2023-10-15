# from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy as AppiumBy
# from selenium.common.exceptions import NoSuchElementException
# import time
#
# def capture_element_screenshot(driver, element_locator, screenshot_path):
#     try:
#         element = driver.find_element(*element_locator)
#         element_location = element.location
#         element_size = element.size
#
#         screenshot = driver.get_screenshot_as_png()
#
#         left = element_location['x']
#         top = element_location['y']
#         right = left + element_size['width']
#         bottom = top + element_size['height']
#
#         element_screenshot = screenshot[top:bottom, left:right]
#
#         with open(screenshot_path, 'wb') as f:
#             f.write(element_screenshot)
#
#         print("Element screenshot captured successfully.")
#     except NoSuchElementException:
#         print("Element not found. Could not capture screenshot.")
#     except Exception as e:
#         print("An error occurred:", str(e))
#
# # Start Appium session
# desired_caps = {
#     'platformName': 'Android',
#     'automationName': 'UiAutomator2',
#     'platformVersion': '10',
#     'deviceName': 'ZF6224GFW3',
#     'appPackage': 'in.amazon.mShop.android.shopping',
#     'appActivity': 'com.amazon.mShop.android.home.PublicUrlActivity',
#     'noReset': True
# }
# driver = webdriver.Remote('http://localhost:4724/wd/hub', desired_caps)
#
# # Define the element locator (change as needed)
# element_locator = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Select English"]')
#
# # Define the path to save the screenshot
# screenshot_path = 'C:/Users/vnaganur/PycharmProjects/appium/Amazon/pages/screenshot.png'
#
# # Wait for the app to load (adjust the time as needed)
# time.sleep(5)
#
# # Capture the element screenshot using the function
# capture_element_screenshot(driver, element_locator, screenshot_path)
#
# # Quit Appium session
# driver.quit()




from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time
from PIL import Image
import io

def capture_element_screenshot(driver, element_locator, screenshot_path):
    try:
        element = driver.find_element(*element_locator)
        element_location = element.location
        element_size = element.size

        screenshot = driver.get_screenshot_as_png()

        # Convert the screenshot to an Image object
        screenshot_image = Image.open(io.BytesIO(screenshot))

        left = element_location['x']
        top = element_location['y']
        right = left + element_size['width']
        bottom = top + element_size['height']

        # Crop the screenshot to the element's bounding box
        element_screenshot = screenshot_image.crop((left, top, right, bottom))

        # Save the cropped screenshot to a file
        element_screenshot.save(screenshot_path)

        print("Element screenshot captured successfully.")
    except NoSuchElementException:
        print("Element not found. Could not capture screenshot.")
    except Exception as e:
        print("An error occurred:", str(e))

# Start Appium session
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '10',
    'deviceName': 'ZF6224GFW3',
    'appPackage': 'in.amazon.mShop.android.shopping',
    'appActivity': 'com.amazon.mShop.android.home.PublicUrlActivity'

}
# ... (your desired capabilities setup)
driver = webdriver.Remote('http://localhost:4724/wd/hub', desired_caps)

# Define the element locator (change as needed)
element_locator = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Select English"]')

# Define the path to save the screenshot
screenshot_path = 'C:/Users/vnaganur/PycharmProjects/appium/Amazon/pages/screenshot.png'

# Wait for the app to load (adjust the time as needed)
time.sleep(5)

# Capture the element screenshot using the function
capture_element_screenshot(driver, element_locator, screenshot_path)

# Quit Appium session
driver.quit()
