import time
import cv2
import numpy as np
import os
from appium import webdriver

# Appium configuration
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '10',
    'deviceName': 'ZF6224GFW3',
    'appPackage': 'in.amazon.mShop.android.shopping',
    'appActivity': 'com.amazon.mShop.android.home.PublicUrlActivity',
    'noRest': True  # This seems to be a typo, should be 'noReset'
}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)

def capture_runtime_screenshot(filename):
    screenshot_dir = '../screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, filename)

    driver.save_screenshot(screenshot_path)
    return screenshot_path

def compare_images(reference_image_path, runtime_image_path, tolerance=5):
    reference_image = cv2.imread(reference_image_path)
    runtime_image = cv2.imread(runtime_image_path)

    # Ensure both images have the same dimensions
    if reference_image.shape != runtime_image.shape:
        print("Images have different dimensions. Cannot compare.")
        return

    # Calculate the absolute difference between pixel values
    diff_image = cv2.absdiff(reference_image, runtime_image)
    diff_sum = np.sum(diff_image)
    print(diff_sum)

    # Calculate the maximum possible difference (if all pixels differ)
    max_possible_diff = reference_image.shape[0] * reference_image.shape[1] * 255 * 3
    print(max_possible_diff)
    # Calculate a difference ratio as a percentage
    diff_ratio = (diff_sum / max_possible_diff) * 100

    print("Difference Ratio:", diff_ratio)

    if diff_ratio <= tolerance:
        print("Images match!")
    else:
        print("Images do not match.")

try:
    # Capture the reference image
    reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\com_28_08_23_15_08_47.png'
    # reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\pages\\screenshot.png'
    # Capture the runtime screenshot
    time.sleep(10)
    runtime_image_path = capture_runtime_screenshot('runtime_screenshot.png')
    print("Runtime screenshot captured:", runtime_image_path)

    # Set the tolerance level for comparison (adjust as needed)
    tolerance = 10  # Increase or decrease as needed

    # Call the function to compare the images
    compare_images(reference_image_path, runtime_image_path, tolerance)
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the Appium session
    driver.quit()
