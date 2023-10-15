#command -  pytest --alluredir=C:\Users\vnaganur\PycharmProjects\appium\Amazon\reports\allurereports -v -s .\test_home_page.py
#report - allure serve path

from appium.webdriver.common.appiumby import AppiumBy
import Amazon.utilities.CustomLogger as cl
from Amazon.base.BasePage import BasePage
import time

class HomePage(BasePage):
    """This line defines a new class named HomePage that inherits from the BasePage class.
     This means that HomePage will inherit all the attributes
     and methods defined in the BasePage class"""
    def __init__(self, driver):

        """This line calls the constructor of the parent class BasePage using the super() function"""
        super().__init__(driver)

        """This line assigns the driver parameter to the instance variable self.driver of the HomePage class"""
        self.driver = driver

    _clickEnglish = 'Select English'
    _click_element = 'Continue in English'
    _Verify_Search_Bar_Presence = 'Search Amazon.in'
    _click_on_search_bar = 'Search Amazon.in'
    _search_product_on_Amazon = 'in.amazon.mShop.android.shopping:id/rs_search_src_text'
    _clickSearch = 'Search Amazon.in'
    _clickiphone14 = 'iphone 14'
    _click_on_search_with_photo = 'in.amazon.mShop.android.shopping:id/iss_btn_flk'
    _click_on_upload_photo = 'in.amazon.mShop.android.shopping:id/a9vs_upload_photo_button'
    _click_on_image_to_search_product='com.android.documentsui:id/icon_mime_lg'
    _scroll_element_until_find_product= "Avantika Fashion Women's Trendy Kanjivaram Soft Lichi Silk Saree With Blouse Piece"
    # _reference_image_path = 'C:/Users/vnaganur/PycharmProjects/appium/Amazon/screenshots/imagecompare_28_08_23_11_25_26.png'
    # _reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\imagecompare_28_08_23_11_25_26.png'
    # _runtime_image_path='C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\runtime_screenshot.png'

    # launch the home page and Verify_Search_Bar_Presence


    def clickEnglish(self):
        self.click_element(self._clickEnglish, 'des')
        cl.allurelogs("clicked on english lauaguage")

    def tap_on_continue_english(self):
        self.tap(518, 1428)
        cl.allurelogs("tap to continue on english button")

    # def image_compasion(self):
    #     self.tap_element_by_image()

    def continueButton(self):
        self.click_element(self._click_element, 'text')
        cl.allurelogs("clicked on continue to english button")

    def Verify_Search_Bar_Presence(self):
        self.is_displayed(self._Verify_Search_Bar_Presence, 'text')
        cl.allurelogs("verifyed search bar presence")

    # search the prdoduct using search log

    def click_on_search_bar(self):
        self.click_element(self._click_on_search_bar, 'text')
        cl.allurelogs("clicked on serach bar to search product")

    def search_product_on_Amazon(self):
        self.send_text('iphone', self._search_product_on_Amazon, 'id')
        cl.allurelogs("searched the product ie iphone")

    def clickiphone_14(self):
        self.click_element(self._clickiphone14, 'text')
        cl.allurelogs("clicked iphone14")

    def keycode_to_go_to_home_page(self):
        self.driver.press_keycode(3)

    #search the product with photo

    def click_on_search_with_photo(self):
        self.click_element(self._click_on_search_with_photo,'id')

    def click_on_upload_photo(self):
        self.click_element(self._click_on_upload_photo,'id')

    def click_on_image_to_search_product(self):
        self.click_element(self._click_on_image_to_search_product,'id')

    def scroll_element_until_find_product(self):
        self.scroll_using_scrollable(self._scroll_element_until_find_product)

    def screenshot_of_product_add_to_cart(self):
        self.screenshots("com")
        cl.allurelogs("take screenshot after the product added into the cart")


    def comapre_image_by_pixcel_to_pixcel(self):
        try:
            # Capture the reference image
            # reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\com_28_08_23_15_08_47.png'
            # reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\imagecompare_28_08_23_11_25_26.png'
            reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\screenshot.png'
            # reference_image_path = 'C:\\Users\\vnaganur\\PycharmProjects\\appium\\Amazon\\screenshots\\click_search_bar.png'

            # Capture the runtime screenshot using self
            runtime_image_path = self.capture_runtime_screenshot('runtime_screenshot.png')
            print("Runtime screenshot captured:", runtime_image_path)

            # Set the tolerance level for comparison (adjust as needed)
            tolerance = 4.0 # Increase or decrease as needed

            # Call the function to compare the images using self
            self.compare_images(reference_image_path, runtime_image_path, tolerance)
        except Exception as e:
            print("An error occurred:", e)


    def image_compare_1(self):
        self.tap_element_by_image()
