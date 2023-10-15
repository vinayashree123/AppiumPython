import time
import unittest
import pytest
import Amazon.utilities.CustomLogger as cl
from Amazon.pages.Homepage import HomePage
from Amazon.pages.AddToCart import AddToCartPage


@pytest.mark.usefixtures("beforeclass")
class AddtocartpageTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classobject(self):
        self.cf = HomePage(self.driver)
        self.ap = AddToCartPage(self.driver)


    @pytest.mark.run(order=1)
    def test_LaunchHomePage(self):
        cl.allurelogs("App Launched")
        self.cf.clickEnglish()
        self.cf.tap_on_continue_english()

    @pytest.mark.run(order=2)
    def test_searchProduct(self):
        self.ap.clickonSearch()
        self.ap.searchAmazon()
        self.ap.clickiphone_14()

    @pytest.mark.run(order=3)
    def test_itemtoaddtocart(self):
        self.ap.clickOnItemToAddToCart()
        self.ap.scroll_until_add_to_cart_found()

    @pytest.mark.run(order=4)
    def test_verifyProductInCart(self):
        self.ap.click_on_cart_button()

    @pytest.mark.run(order=5)
    def test_screenshotOfProductInCart(self):
        self.ap.screenshot_of_product_add_to_cart()

    @pytest.mark.run(order=6)
    def test_removeProductFromCart(self):
        self.ap.remove_products_from_the_cart()










#
# log.info("Search product")
#
#
# log.info("add the product to cart")
# cf.clickOnItemToAddToCart()
# cf.scrollElement1()
#
# log.info("View the cart and verify added products ")
#
# # cf.Update_the_quantity_of_product()
#
#
#
# log.info("take screenshot of product added to cart")







































# cf.scroll_ele()
# cf.swipefromlefttoright()
# cf.scrollElement1()


# cf.continue_on_mi()
# cf.clickonSearch_on_mi()
# cf.searchAmazon_on_mi()
# cf.clickiphone_14_on_mi()
# cf.clickOnItemToAddToCart_on_mi()
# cf.scrollElement_on_mi()
# scroll_from_top_to_bottom()


"""cf.clickGetstart()
cf.sendMobNum()
cf.clickGetotp()"""

