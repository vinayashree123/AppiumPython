import time
import unittest
import pytest
from Amazon.pages.Homepage import HomePage
import Amazon.utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeclass")
class HomePageTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classobject(self):
        self.cf = HomePage(self.driver)

    @pytest.mark.run(order=2)
    def test_VerifySearchbarisDiplayed(self):
        self.cf.Verify_Search_Bar_Presence()


    @pytest.mark.run(order=1)
    def test_launch_home_page(self):
        cl.allurelogs("App Launched")
        self.cf.clickEnglish()
        self.cf.tap_on_continue_english()
        self.cf.click_on_search_bar()
        self.cf.comapre_image_by_pixcel_to_pixcel()




    # @pytest.mark.run(order=3)
    # def test_search_prdoduct_using_photo(self):
    #     # self.cf.keycode_to_go_to_home_page()
    #     self.cf.click_on_search_bar()
    #     self.cf.click_on_search_with_photo()
    #     self.cf.click_on_upload_photo()
    #     self.cf.click_on_image_to_search_product()
    #     self.cf.scroll_element_until_find_product()


    # @pytest.mark.run(order=3)
    # def test_searchPrdoductUsingSearchLog(self):
    #     self.cf.click_on_search_bar()
    #     self.cf.search_product_on_Amazon()
    #     self.cf.clickiphone_14()


    # @pytest.mark.run(order=1)
    #     def test_to_check_image_comparision(self):
    #         cl.allurelogs("App Launched")
    #         self.cf.image_compasion()
    #         # self.cf.clickEnglish()
    #         self.cf.tap_on_continue_english()











