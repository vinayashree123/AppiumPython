# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
#
#
# img1 = cv2.imread('C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\com_28_08_23_15_08_47.png', 0)  # queryImage
# img2 = cv2.imread('C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\pages\\screenshot.png', 0)  # trainImage
#
#
# # Initialize SIFT detector
# sift = cv2.SIFT_create()
#
# # Detect keypoints and compute descriptors
# kp1, des1 = sift.detectAndCompute(img1, None)
# kp2, des2 = sift.detectAndCompute(img2, None)
# import cv2
# from matplotlib import pyplot as plt
#
# # Load images
# img1 = cv2.imread('C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\com_28_08_23_15_08_47.png', 0)  # queryImage
# img2 = cv2.imread('C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\pages\\screenshot.png', 0)  # trainImage
#
# # Initialize SIFT detector
# sift = cv2.SIFT_create()
#
# # Detect keypoints and compute descriptors
# kp1, des1 = sift.detectAndCompute(img1, None)
# kp2, des2 = sift.detectAndCompute(img2, None)
#
# # BFMatcher with default params
# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1, des2, k=2)
#
# # Apply ratio test to select good matches
# good = []
# for m, n in matches:
#     if m.distance < 0.75 * n.distance:
#         good.append([m])
#
# # Draw matches using cv2.drawMatchesKnn
# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
#
# # Display the output image using matplotlib
# plt.imshow(img3)
# plt.show()
#
# # BFMatcher with default params
# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1,des2, k=2)
#
# # Apply ratio test
# good = []
# for m,n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append([m])
#
# # cv2.drawMatchesKnn expects list of lists as matches.
# img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,flags=2)
#
# plt.imshow(img3),plt.show()
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
    screenshot_dir = 'screenshots'
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

    if diff_sum <= tolerance:
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

    # Set the tolerance level for comparison
    tolerance = 20000

    # Call the function to compare the images
    compare_images(reference_image_path, runtime_image_path, tolerance)
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the Appium session
    driver.quit()
