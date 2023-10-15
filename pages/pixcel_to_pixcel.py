"""import cv2
import numpy as np
from PIL import ImageGrab

def compare_real_time_with_base(base_image_path, tolerance=5):
    base_image = cv2.imread(base_image_path)
    real_time_image = np.array(ImageGrab.grab())

    # Compute the absolute difference between the images
    diff = cv2.absdiff(base_image, real_time_image)
    diff_sum = diff.sum()

    if diff_sum <= tolerance:
        print("Screenshots match!")
    else:
        print("Screenshots do not match.")

# Path to the base image you want to compare against
base_image_path = 'path_to_base_image.png'

# Set the tolerance level for comparison
tolerance = 5000

# Call the function to compare the real-time screenshot with the base image
compare_real_time_with_base(base_image_path, tolerance)
"""



from PIL import Image
import io
import pyautogui
import cv2
import numpy as np
import os
from appium import webdriver

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

def compare_images(image1_path, image2, tolerance=5):
    image1 = Image.open(image1_path)

    # Get the image dimensions
    width, height = image1.size

    # Load the runtime image
    image2 = Image.open(io.BytesIO(image2))

    # Compare each pixel of the images
    diff_pixels = 0
    for y in range(height):
        for x in range(width):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            # Calculate the absolute difference between pixel values
            diff = abs(pixel1[0] - pixel2[0]) + abs(pixel1[1] - pixel2[1]) + abs(pixel1[2] - pixel2[2])

            if diff > tolerance:
                diff_pixels += 1

    return diff_pixels

# Get path to the reference image
reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\com_28_08_23_15_08_47.png'

# Capture the runtime image using pyautogui (adjust as needed)
print("Capture the runtime image...")
pyautogui.alert("Capture the runtime image now.")
image2 = pyautogui.screenshot()

# Set the tolerance level for comparison (adjust as needed)
tolerance = 50

# Call the function to compare the images
diff_count = compare_images(reference_image_path, image2, tolerance)
if diff_count == 0:
    print("Images match!")
else:
    print(f"Images do not match. Total different pixels: {diff_count}")
