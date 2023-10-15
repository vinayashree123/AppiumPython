from appium.webdriver.common.appiumby import AppiumBy

from Amazon.base.BasePage import BasePage
import Amazon.utilities.CustomLogger as cl

class ProductListingPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _clickEnglish = '//android.widget.ImageView[@content-desc="Select English"]'
    _clickElement = 'Continue in English'
    _click_on_fashion_product = 'Fashion'
    _click_to_select_women_category = 'Women'
    _select_Sarees_from_women_category = 'Sarees'

    _click_on_filter_to_select_sarees = 'Filters (23)'
    _click_on_color_sarees = 'Colours'
    _click_on_Reds_sarees = 'Reds'
    _click_to_material_to_select_filter_for_saree = 'Material'
    _click_on_silk = 'Silk'
    _click_on_show_Results = '//android.view.View[@content-desc="Show 104 results"]'
    _clear_results_for_filters = '//android.view.View[@content-desc="Clear Filters"]'

    _element_id_to_scroll_until_product_visible = 'DEAL_OF_THE_DAY_B0BC46RJ9K-label'


    # #launch the home page
    #
    # def clickEnglish(self):
    #     self.clickElement(self._clickEnglish,'xpath')
    #
    # def tap_on_continue_english(self):
    #     self.tap(518,1428)
    #
    # def continueButton(self):
    #     self.clickElement(self._clickElement,'text')

    #productlist are like mobile,fashion

    def click_on_fashion_product(self):
        self.clickElement(self._click_on_fashion_product,'text')
        cl.allurelogs("selecting the fashion category")
    def click_to_select_women_category(self):
        self.clickElement(self._click_to_select_women_category,'text')
        cl.allurelogs("from fashion selecting the women category")
    def select_Sarees_from_women_category(self):
        self.clickElement(self._select_Sarees_from_women_category,'text')
        cl.allurelogs("from womenens category selecting the saree ")

    #Filter products by a specific attribute
    def click_on_filter_to_select_sarees(self):
        self.clickElement(self._click_on_filter_to_select_sarees,'text')
        cl.allurelogs("clicked on filter for sarees")
    def click_on_color_sarees(self):
        self.clickElement(self._click_on_color_sarees,'text')
        cl.allurelogs("clicked on colors to selecting the sraee color")
    def click_on_Reds_sarees(self):
        self.clickElement(self._click_on_Reds_sarees,'text')
        cl.allurelogs("selecting the red color sarees")
    def click_on_material_to_select_filter_for_saree(self):
        self.clickElement(self._click_to_material_to_select_filter_for_saree,'text')
        cl.allurelogs("clicked on selecting the material of saree")
    def click_on_silk(self):
        self.clickElement(self._click_on_silk,'text')
        cl.allurelogs("clicked on silk saree")

    def click_on_show_Results(self):
        self.clickElement(self._click_on_show_Results,'xpath')
        cl.allurelogs("clicked on show results button ")

    def clear_results_for_filters(self):
        self.clickElement(self._clear_results_for_filters,'xpath')



    def select_product_add_to_wish_list(self):
        self.scroll_using_scrollable("Womanista Women's Striped Satin Saree (TI2879_Mauve")
        # self.scroll_using_scrollable_id(self._element_id_to_scroll_until_product_visible,'id')
        # self.scroll_to_element(self._element_id_to_scroll_until_product_visible,'id')

    # def scroll_to_add_the_product_in_list(self):
    #     self.scroll_using_scrollable_id("in.amazon.mShop.android.shopping:id/contextual_actions_container")
    #






    _scrollElement = 'Add to Cart'
    _clickOnItemToAddToCart = 'Apple iPhone 14 (128 GB) - Blue'
    _clickonAddToCartButton = 'add-to-cart-button'






    def clickOnItemToAddToCart(self):
        self.clickElement(self._clickOnItemToAddToCart,'text')
    def scrollElement1(self):
        self.scroll_using_scrollable(self._scrollElement)
    def swipefromlefttoright(self):
        # Find the element you want to swipe to
        element_to_swipe_to = self.getElement('Apple iPhone 14 (128 GB) - Blue','text')
    def swipe_to_element(self):
        self.swipe()
    def clickonAddToCartButton(self):
        self.clickElement(self._clickonAddToCartButton,'id')





