import os
import time

import cv2
from PIL import Image
import io
import numpy as np
import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.touch_action import TouchAction

from appiumFramework.utilities.CustomLogger import customLogger
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.log = customLogger()

    """Constructor that initializes the class with the Appium driver and a custom logger"""

    def wait_for_element(self, locator_value, locator_type):
        """
        Waits for an element to become available in the UI using various types of locators.

        Args:
            locator_value (str): The value of the locator (e.g., ID, class name, XPath, etc.).
            locator_type (str): The type of locator (e.g., "id", "class", "des", "index", "text",
            "xpath").

        Returns:
            WebElement or None: The found WebElement object, or None if not found.
            :param locator_type:
            :param locator_value:
        """
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locator_type == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locator_value))
            return element
        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locator_value))
            return element
        elif locator_type == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % locator_value))
            return element
        elif locator_type == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locator_value)))
            return element
        elif locator_type == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locator_value))
            return element
        elif locator_type == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locator_value))
            return element
        else:
            self.log.info("Locator Value " + locator_value + " Not found")
        return element

    def get_element(self, locator_value, locator_type='id'):
        """
        Find and return a web element based on the provided locator value and locator type.

        Args:
            locator_value (str): The value of the locator (e.g., ID, class name, XPath, etc.).
            locator_type (str, optional): The type of locator (e.g., "id", "class", "des", "index",
             "text", "xpath").-----Defaults to 'id'------

        Returns:
            WebElement or None: The found WebElement object, or None if not found.
        """
        element = None
        try:
            locator_type = locator_type.lower()
            # Convert locator_type to lowercase for consistency

            element = self.wait_for_element(locator_value, locator_type)
            # Call the wait_for_element method to find the element

            self.log.info("Element found with locator_value " + locator_value +
                          " and with locator_type " + locator_type)
            # Log that the element was found using the provided locator value and locator type
        except Exception as e:
            self.log.error("Element not found with locator_value " + locator_value +
                           " and with locator_type " + locator_type)
            # If an exception occurs during the try block, log an error message
            # indicating that the element was not found with the provided locator value
            # and locator type

            self.log.exception(e)
            # Additionally, log the details of the exception using the log.exception method

        return element

    def click_element(self, locator_value, locator_type='id'):
        """
        Clicks on a web element using the specified locator value and type.

        Args:
            locator_value (str): The value of the locator (e.g., ID, class name, XPath, etc.).
            locator_type (str, optional): The type of locator (e.g., "id", "class", "xpath"). Defaults to 'id'.

        Returns:
            None

        Raises:
            AssertionError: If the element is not found or if an exception occurs.
        """
        element = None
        try:
            locator_type = locator_type.lower()
            # Convert locator_type to lowercase for consistency

            element = self.wait_for_element(locator_value, locator_type)
            # Find the element using the provided locator value and type

            element.click()
            # Click the found element

            self.log.info("Clicked the Element found with locator_value " + locator_value +
                          " and with locator_type " + locator_type)
        except Exception as exception:
            self.log.error("Unable to click Element not found with locator_value "
                           + locator_value + " and with locator_type " + locator_type)
            self.log.exception(exception)
            self.take_screenshot(locator_type)
            # Call the take_screenshot() when there is an error in passing the invalid locator type
            # then it will take a screenshot and add it in the allure report"""
            assert False


    def send_text(self, text, locator_value, locator_type='id'):
        """
        Enters text into a text input element using the specified locator value and type.

        Args:
            text (str): The text to be entered into the text input element.
            locator_value (str): The value of the locator (e.g., ID, class name, XPath, etc.).
            locator_type (str, optional): The type of locator (e.g., "id", "class", "xpath"). Defaults to 'id'.

        Returns:
            None

        Raises:
            AssertionError: If the element is not found or if an exception occurs.
        """
        element = None
        try:
            locator_type = locator_type.lower()
            # Convert locator_type to lowercase for consistency

            element = self.wait_for_element(locator_value, locator_type)
            # Find the element using the provided locator value and type

            element.send_keys(text)
            # Enters the provided text into the element

            self.log.info("Text sent to the Element found with locator_value "
                          + locator_value + " and with locator_type " + locator_type)
        except Exception as e:
            self.log.error("Unable to send text because Element not found with locator_value "
                           + locator_value + " and with locator_type " + locator_type)
            self.log.exception(e)
            self.take_screenshot(locator_type)
            assert False


    def is_displayed(self, locator_value, locator_type='id'):
        """
        Checks if an element is displayed on the page using the specified locator value and type.

        Args:
            locator_value (str): The value of the locator (e.g., ID, class name, XPath, etc.).
            locator_type (str, optional): The type of locator (e.g., "id", "class", "xpath"). Defaults to 'id'.

        Returns:
            bool: True if the element is displayed, False otherwise.
        """
        element = None
        try:
            locator_type = locator_type.lower()
            # Convert locator_type to lowercase for consistency

            element = self.wait_for_element(locator_value, locator_type)
            # Find the element using the provided locator value and type

            element.is_displayed()
            # Checks if the element is displayed on the page

            self.log.info(
                "Element found with locator_value " + locator_value + " and with locator_type "
                + locator_type + " is displayed")
            return True
        except Exception:
            self.log.info(
                "Unable to send text because Element not found with locator_value "
                + locator_value + " and with locator_type " + locator_type + " is not displayed")
            return False

    def screenshots(self, screenshot_name):
        """
        Captures a screenshot of the current state of the app and saves it with the provided name.

        Args:
            screenshot_name (str): A descriptive name for the screenshot.

        Returns:
            None
        """
        filename = screenshot_name + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        # Create a filename for the screenshot using the provided screenshot_name and current timestamp

        screenshot_directory = "../screenshots/"
        # Define the directory where the screenshots will be saved

        screenshot_path = screenshot_directory + filename
        # Create the complete path for the screenshot

        try:
            self.driver.save_screenshot(screenshot_path)
            # Save a screenshot of the current screen using the driver's save_screenshot method

            self.log.info("Screenshot saved: %s", screenshot_path)
            # Log a message indicating that the screenshot was successfully saved

        except Exception as e:
            self.log.error("Failed to save screenshot: %s", str(e))
            # If there's an exception (error) while saving the screenshot, log an error message


    def scroll_using_scrollable_by_text(self, scroll_text):
        """
        Scrolls the page to find an element with the specified scroll_text using UIAutomator.

        Args:
            scroll_text (str): The text to scroll to.

        Returns:
            None
        """
        try:
            # Construct a UIAutomator query to find an element with the specified scroll_text
            query = 'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                    '.scrollIntoView(new UiSelector().textContains("' + scroll_text + '"))'

            # Find the element using the constructed query
            ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, query)

            # Click the element after it's found (optional step)
            ele.click()

            # Log a message indicating that scrolling is started
            self.log.info("Scrolling is started")

        except Exception as e:
            # If an exception (error) occurs during scrolling, log an error message
            self.log.error("Error occurred while scrolling: %s", str(e))

    def tap(self, x_cordinate, y_ordinate):
        """
        Performs a tap gesture at the specified coordinates on the screen.

        Args:
            x_cordinate (int): The x-coordinate of the tap gesture.
            y_ordinate (int): The y-coordinate of the tap gesture.

        Returns:
            None
        """
        try:
            # Create a TouchAction object using the driver instance
            action = TouchAction(self.driver)

            # Perform the tap gesture at the specified coordinates (x, y)
            action.tap(x=x_cordinate, y=y_ordinate).perform()

            # Log a success message with the coordinates of the tap
            self.log.info("Tap gesture performed at coordinates: (%d, %d)", x_cordinate, y_ordinate)

        except Exception as e:
            # If an exception occurs, log an error message along with the exception details
            self.log.error("Error occurred while performing tap gesture: %s", str(e))


    def take_screenshot(self, text):
        """
        This method captures a screenshot of the current state of the app
        and attaches it to an Allure report.

        Parameters:
        - text: A descriptive name or label for the screenshot (to be used in the report).
        """
        allure.attach(
            self.driver.get_screenshot_as_png(),  # Captures the screenshot as a PNG image
            name=text,  # The name or label for the screenshot in the report
            attachment_type=AttachmentType.PNG  # Specifies that the attachment type is PNG
        )
    def scroll_using_scrollable_by_text(self, scroll_text):
        """
        Scrolls the page to find an element with the specified scroll_text using UIAutomator.

        Args:
            scroll_text (str): The text to scroll to.

        Returns:
            None
        """
        try:
            # Construct a UIAutomator query to find an element with the specified scroll_text
            query = 'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                    '.scrollIntoView(new UiSelector().textContains("' + scroll_text + '"))'

            # Find the element using the constructed query
            ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, query)

            # Click the element after it's found (optional step)
            ele.click()

            # Log a message indicating that scrolling is started
            self.log.info("Scrolling is started")

        except Exception as e:
            # If an exception (error) occurs during scrolling, log an error message
            self.log.error("Error occurred while scrolling: %s", str(e))


    def scroll_using_scrollable(self, scroll_locator, scroll_value):
        """
        Scrolls to an element using a scrollable container based on the specified scroll locator and value.

        Args:
            scroll_locator (str): The type of locator used in the query (e.g., 'text', 'description').
            scroll_value (str): The value to be used in the query for scrolling to the desired element.

        Returns:
            None
        """
        try:
            # Construct a UIAutomator query to find an element with the specified scroll_locator and scroll_value
            query = f'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                    f'.scrollIntoView(new UiSelector().{scroll_locator}("{scroll_value}"))'

            # Find the element using the constructed query
            ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, query)

            # Click the element after it's found (optional step)
            ele.click()

            # Log a message indicating that scrolling is started
            self.log.info("Scrolling is started")

        except Exception as e:
            # If an exception (error) occurs during scrolling, log an error message
            self.log.error("Error occurred while scrolling: %s", str(e))


    def capture_runtime_screenshot(self,filename):
        """Capture a screenshot of the current web page using a WebDriver instance
        and save it to a specified directory.

        Args:
            self: An instance of a class with a WebDriver object configured for web automation.
            filename (str): The name of the screenshot file, including the file extension.

        Returns:
            str: The path to the saved screenshot. """

        screenshot_dir = '../screenshots/Moto_Phone'
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, filename)

        self.driver.save_screenshot(screenshot_path)
        return screenshot_path

    def compare_images(self,reference_image_path, runtime_image_path, tolerance):
        """
        Compare two images and log the difference ratio as a percentage.

        Args:
            self: An instance of a class with logging capabilities.
            reference_image_path (str): The file path to the reference image.
            runtime_image_path (str): The file path to the runtime (captured) image for comparison.
            tolerance (float): The acceptable difference tolerance as a percentage (0.0 to 100.0).

        Note:
            This function uses OpenCV (cv2) to compare two images by calculating
            the absolute pixel-wise difference.
            It then computes the difference ratio as a percentage of the maximum possible difference.
            The difference ratio is logged to help assess image similarity."""

        reference_image = cv2.imread(reference_image_path)
        runtime_image = cv2.imread(runtime_image_path)

        # Ensure both images have the same dimensions
        if reference_image.shape != runtime_image.shape:
            self.log.info("Images have different dimensions. Cannot compare.")
            return

        # Calculate the absolute difference between pixel values
        diff_image = cv2.absdiff(reference_image, runtime_image)
        diff_sum = np.sum(diff_image)

        # Calculate the maximum possible difference (if all pixels differ)
        max_possible_diff = reference_image.shape[0] * reference_image.shape[1] * 255 * 3

        # Calculate a difference ratio as a percentage
        diff_ratio = (diff_sum / max_possible_diff) * 100

        # Log the difference ratio as a percentage
        self.log.info("Difference Ratio: %.2f" % diff_ratio)


        if diff_ratio <= tolerance:
            self.log.info("Images match!")
        else:
            self.log.info("Images do not match.")

    # try:
    #     # Capture the reference image
    #     reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\com_28_08_23_15_08_47.png'
    #     # reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\pages\\screenshot.png'
    #     # Capture the runtime screenshot
    #     time.sleep(10)
    #     runtime_image_path = capture_runtime_screenshot('runtime_screenshot.png')
    #     print("Runtime screenshot captured:", runtime_image_path)
    #
    #     # Set the tolerance level for comparison (adjust as needed)
    #     tolerance = 1  # Increase or decrease as needed
    #
    #     # Call the function to compare the images
    #     compare_images(reference_image_path, runtime_image_path, tolerance)
    # except Exception as e:
    #     print("An error occurred:", e)



    def swipe_to_element(self, element):
        start_x = element.location['x'] + int(element.size['width'] * 0.8)
        end_x = element.location['x'] + int(element.size['width'] * 0.2)
        y = element.location['y'] + int(element.size['height'] * 0.5)

        action = TouchAction(self.driver)
        action.press(x=start_x, y=y).move_to(x=end_x, y=y).release().perform()


    def swipe(self):
        try:
            devicesize = self.driver.get_window_size()
            screenwidth = devicesize['width']
            screenheight = devicesize['height']

            #right to left here y will half of the height
            startx = 40
            endx = 344
            starty = screenwidth/2
            endy = screenheight/2

            # startx1 = screenwidth/8
            # endx1 = screenheight*8/9
            # starty1 = screenwidth/2
            # endy1 = screenheight/2
            #

            action = TouchAction(self.driver)
            action.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
            self.log.info("swipe started")
        except Exception as e:
            self.log.error("Error occurred while swiping: %s", str(e))





    # def swipe_from_left_to_right(self,distance=200):
    #     # devicesize = self.driver.get_window_size()
    #     # screenwidth = devicesize['width']
    #     # screenheight = devicesize['height']
    #     #
    #     # startx = screenwidth/4
    #     # endx = startx * 3
    #     # starty = screenwidth/2
    #     # endy = screenheight/2
    #     #
    #     # actions = TouchAction(self.driver)
    #     # action = TouchAction(self.driver)
    #     # action.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
    #     # time.sleep(2)
    #     try:
    #         wait = WebDriverWait(self.driver, 25, poll_frequency=1,
    #                  ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
    #                                      NoSuchElementException])
    #         ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("Apple iPhone 14 (128 GB) - Blue"))'))
    #         #to perform tap action provide element x and y cordinate and count in Tap()
    #         startx = ele.location['x']
    #         starty = ele.location['y']
    #         endx = startx + distance  # Adjust the distance based on your swipe length
    #         endy = starty
    #
    #         actions = TouchAction(self.driver)
    #         actions.press(x=startx, y=starty).move_to(x=endx, y=endy).release().perform()
    #
    #         time.sleep(2)
    #     except Exception as e:
    #         self.log.error("Error occurred while scrolling: %s", str(e))
    #


    # def scroll_to_element(self, locator_strategy, locator_value):
    #     try:
    #         # Constructing the UIAutomator expression to scroll to the element with the specified locator
    #         scroll_command = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(' + locator_strategy + '("' + locator_value + '"))'
    #
    #         # Finding the element based on the constructed UIAutomator expression
    #         ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_command)
    #
    #         # Clicking the element
    #         ele.click()
    #     except NoSuchElementException:
    #         print("Element with locator '{}' and value '{}' not found.".format(locator_strategy, locator_value))

    # def tap_element_by_image(self, reference_image_path):
    #     try:
    #         # Capture the current screen
    #         screenshot = self.driver.get_screenshot_as_png()
    #         current_image = Image.open(io.BytesIO(screenshot))
    #
    #         # Load the reference image
    #         reference_image = Image.open(reference_image_path)
    #
    #         # Resize the reference image to match the current screen dimensions
    #         reference_image = reference_image.resize(current_image.size)
    #
    #         # Convert images to numpy arrays
    #         current_array = np.array(current_image)
    #         reference_array = np.array(reference_image)
    #
    #         # Perform basic image comparison
    #         diff = current_array - reference_array
    #         difference_score = np.mean(diff)
    #
    #         # Define a threshold for similarity
    #         similarity_threshold = 100
    #
    #         if difference_score < similarity_threshold:
    #             # Perform tap action if images are similar
    #             print("Button found! Performing action...")
    #             # Add code here to perform the tap action
    #         else:
    #             print("Button not found.")
    #     except Exception as e:
    #         print("An error occurred:", str(e))


    # def tap_element_by_image(self):
    #     try:
    #         # reference_image_path = 'C:/Users/vnaganur/PycharmProjects/appium/Amazon/screenshots/imagecompare_28_08_23_11_25_26.png'
    #
    #         # Capture the current screen
    #         screenshot = self.driver.get_screenshot_as_png()
    #         current_image = Image.open(io.BytesIO(screenshot))
    #
    #         # Load the reference image
    #         reference_image = Image.open('C:/Users/vnaganur/PycharmProjects/appium/Amazon/screenshots/imagecompare_28_08_23_11_25_26.png')
    #
    #         # Perform basic image comparison
    #         diff = np.array(current_image) - np.array(reference_image)
    #         difference_score = np.mean(diff)
    #
    #         # Define a threshold for similarity
    #         similarity_threshold = 100
    #
    #         if difference_score < similarity_threshold:
    #             # Perform tap action if images are similar
    #             print("Button found! Performing tap action...")
    #
    #             # Get the element's position on the screen
    #             element_x, element_y = self.find_element_coordinates(reference_image, current_image)
    #
    #             # Perform the tap action using TouchAction
    #             touch_action = TouchAction(self.driver)
    #             touch_action.tap(x=element_x, y=element_y).perform()
    #
    #             print("Tap action performed.")
    #         else:
    #             print("Button not found.")
    #     except Exception as e:
    #         print("An error occurred:", str(e))
    #
    # def find_element_coordinates(self, reference_image, current_image):
    #     # Perform image comparison and locate element's position
    #     # Implement your image comparison algorithm here
    #     # Return the element's X and Y coordinates
    #     element_x = 292  # Replace with the actual X coordinate
    #     element_y = 199  # Replace with the actual Y coordinate
    #     return element_x, element_y






