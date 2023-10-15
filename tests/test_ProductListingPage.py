import unittest
import pytest
from Amazon.pages.Homepage import HomePage
import Amazon.utilities.CustomLogger as cl
from Amazon.pages.ProductListingPage import ProductListingPage

@pytest.mark.usefixtures("beforeclass")
class ProductListingPageTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classobject(self):
        self.pl = ProductListingPage(self.driver)
        self.cf = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_LaunchHomePage(self):
        cl.allurelogs("App Lauched")
        self.cf.clickEnglish()
        self.cf.tap_on_continue_english()

    @pytest.mark.run(order=2)
    def test_selectcategory(self):
        self.pl.click_on_fashion_product()
        self.pl.click_to_select_women_category()
        self.pl.select_Sarees_from_women_category()

    # @pytest.mark.run(order=3)
    # def test_Addproducttowishlist(self):
    #     self.pl.select_product_add_to_wish_list()
    #     self.pl.scroll_to_add_the_product_in_list()

    # @pytest.mark.run(order=4)
    # def scroll_to_addin_list(self):
    #     # self.pl.scroll_to_add_the_product_in_list()
    #     self.pl.click_on_color_sarees()
    #     self.pl.click_on_Reds_sarees()
    #     self.pl.click_on_material_to_select_filter_for_saree()
    #     self.pl.click_on_silk()
    #     # self.pl.click_on_show_Results()
    #     self.pl.clear_results_for_filters()

    @pytest.mark.run(order=3)
    def test_FilterProductsByAttribute(self):
        self.pl.click_on_filter_to_select_sarees()
        self.pl.click_on_color_sarees()
        self.pl.click_on_Reds_sarees()
        self.pl.click_on_material_to_select_filter_for_saree()
        self.pl.click_on_silk()
        # self.pl.click_on_show_Results()
        self.pl.clear_results_for_filters()






