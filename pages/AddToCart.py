from Amazon.base.BasePage import BasePage
import Amazon.utilities.CustomLogger as cl
class AddToCartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _clickEnglish = '//android.widget.ImageView[@content-desc="Select English"]'
    _click_element = 'Continue in English'
    _searchProduct = 'in.amazon.mShop.android.shopping:id/rs_search_src_text'
    _clickSearch = 'Search Amazon.in'
    _clickiphone14 = 'iphone 14'
    _scrollElement = 'Add to Cart'
    _clickOnItemToAddToCart = 'Apple iPhone 14 (128 GB) - Blue'
    _clickonAddToCartButton = 'add-to-cart-button'

    _click_on_cart_button = 'Cart'
    _Update_the_quantity_of_product = '+'
    _remove_products_from_the_cart = 'Delete'


    # # Launch Home Page
    # def clickEnglish(self):
    #     self.click_element(self._clickEnglish,'xpath')
    # def tap_on_continue_english(self):
    #     self.tap(518,1428)
    # def continueButton(self):
    #     self.click_element(self._click_element,'text')

    #Search product
    def clickonSearch(self):
        self.click_element(self._clickSearch,'text')
        cl.allurelogs("clicked on search log")

    def searchAmazon(self):
        self.send_text('iphone',self._searchProduct,'id')
        cl.allurelogs("search the product ie iphone")
    def clickiphone_14(self):
        self.click_element(self._clickiphone14,'text')
        cl.allurelogs("from that selecting the iphone14")

    #add the product to cart
    def clickOnItemToAddToCart(self):
        self.scroll_using_scrollable_by_text(self._clickOnItemToAddToCart)
        # self.click_element(self._clickOnItemToAddToCart,'text')
        cl.allurelogs("clicked on the item to add to cart")

    def scroll_until_add_to_cart_found(self):
        self.scroll_using_scrollable_by_text(self._scrollElement)
        cl.allurelogs("scroll the element until add to cart button visible and then click on that button")

    #View the cart and verify added products
    def click_on_cart_button(self):
        self.click_element(self._click_on_cart_button,'text')
        cl.allurelogs("clicked on cart button to verify the product added into cart")


    def Update_the_quantity_of_product(self):
        self.click_element(self._Update_the_quantity_of_product,'text')
        cl.allurelogs("increase the quantity of the product")

    def remove_products_from_the_cart(self):
        self.click_element(self._remove_products_from_the_cart,'text')
        cl.allurelogs("remove the product from the cart")

    # take screenshot of product added to cart
    def screenshot_of_product_add_to_cart(self):
        self.screenshots("addtocart")
        cl.allurelogs("take screenshot after the product added into the cart")


















































































    # _continue_on_mi= 'Continue'
    # _clickSearch_on_mi = 'in.amazon.mShop.android.shopping:id/chrome_search_hint_view'
    # _searchAmazon_on_mi = 'in.amazon.mShop.android.shopping:id/rs_search_src_text'
    # _clickiphone14_on_mi = 'iphone 14'
    # _clickOnItemToAddToCart_on_mi = 'Apple iPhone 14 (128 GB) - Blue'
    # _element_to_scroll = 'Add to Cart'
    #
    #
    #
    #
    #







































































    # def continue_on_mi(self):
    #     self.click_element(self._continue_on_mi,'text')
    # def clickonSearch_on_mi(self):
    #     self.click_element(self._clickSearch_on_mi,'id')
    # def searchAmazon_on_mi(self):
    #     self.sendText('iphone',self._searchAmazon_on_mi,'id')
    # def clickiphone_14_on_mi(self):
    #     self.click_element(self._clickiphone14_on_mi,'text')
    # def clickOnItemToAddToCart_on_mi(self):
    #     self.click_element(self._clickOnItemToAddToCart_on_mi,'text')
    # def scrollElement_on_mi(self):
    #     self.scroll_to_element_by_text(self._element_to_scroll,'text')




















    """_clickGetstart = 'in.swiggy.android:id/btn_get_started'
    _clickNoneoftheabove = 'NONE OF THE ABOVE'
    _sendMobNum = 'com.google.android.gms:id/default_credential_avatar_icon'
    _clickGetotp = 'Get OTP'

    def clickGetstart(self):
        self.click_element(self._clickGetstart,'id')

    def clickNoneoftheabove(self):
        self.click_element(self._clickNoneoftheabove,'text')\

    def sendMobNum(self):
        self.click_element('self._sendMobNum','id')

    def clickGetotp(self):
        self.click_element(self._clickGetotp,'text')"""
