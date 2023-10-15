from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class Driver:
    def getDriverMethod(self):
        """
        Initializes and returns an Appium WebDriver instance with the specified desired capabilities.

        Returns:
            WebDriver: An instance of the Appium WebDriver.
        """
        # Desired capabilities for the Android device and app
        desired_caps = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'platformVersion': '10',
            'deviceName': 'ZF6224GFW3',
            'appPackage': 'in.amazon.mShop.android.shopping',
            'appActivity': 'com.amazon.mShop.android.home.PublicUrlActivity',
            'noRest': True  # This seems to be a typo, should be 'noReset'
        }

        # Create an Appium WebDriver instance using the specified desired capabilities
        driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)

        # Return the created driver instance
        return driver
