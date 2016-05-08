import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(sys.path[0], os.pardir)))
from Utilities.BaseTestCase import BaseTestCase
from Methods.HomeBeforeLoginMethods import HomeBeforeLoginMethods
from Methods.LoginMethods import LoginMethods
from Methods.SearchResultsMethods import SearchResultsMethods
from PageObjectModels.HomeBeforeLoginPage import HomeBeforeLoginPage
from Methods.TermsOfServiceMethods import TermsOfServiceMethods


class HomeBeforeLoginTests(BaseTestCase):

    #   Verify that all Page Elements are loaded correctly
    def test_01_all_elements_are_loaded_correctly(self):
        home_page = HomeBeforeLoginPage(self.driver)

        #   Verify that all Page Elements can be found
        home_page.validate_page_elements(home_page.page_elements_list)

    #   Verify that clicking the Login button will navigate the user to the Login Page.
    def test_02_click_login_button(self):
        home_page = HomeBeforeLoginPage(self.driver)

        #   Click Sign In button
        home_page.click_sign_in_button()

        #   Verify that the Login Page is loaded
        home_page.current_page_title_verification(self, "Sign in to GitHub · GitHub")

        #   Navigate back to the Home Page
        home_page.go_to_url(home_page.url)

    #  Verify that entering a text in the search box and pressing Enter will navigate the user to the
    #  Search Results Page.
    def test_search_box(self):

        #   Navigate to github.com
        self.driver.get("https://github.com")

        #   Search for "SneakyPythonGitHub" using the Home Page Search Box
        HomeBeforeLoginMethods.use_search_box(self, "SneakyPythonGitHub")

        #   Verify that Search Label is displayed on the Search Results page Which means the Search Page is displayed.
        SearchResultsMethods.search_label_text_is_displayed_correctly(self)

        #   Navigate back to the Home Page
        self.driver.get("https://github.com")

    #   Verify that clicking the Terms of Service link will navigate the user to the Terms of Service.
    def test_terms_of_service_link(self):
        #   Navigate to github.com
        self.driver.get("https://github.com/")

        #   Assert that the Terms of Service link is displayed
        self.assertTrue(HomeBeforeLoginMethods.terms_of_service_link_is_displayed(self))

        #   Click the Terms of Service link
        self.driver.find_element(*HomeBeforeLoginPage.terms_of_service_link).click()

        #   Switch to the new window that has just opened after clicking the Terms of Service Link
        #   At the same time, save the original window handle
        original_window_handle = TermsOfServiceMethods.switch_to_terms_of_service_browser_window(self)

        #   Verify that the Terms of Service Page is displayed in another window
        TermsOfServiceMethods.terms_of_service_page_is_displayed(self)

        #   Close the new Window of the Terms Of Service
        TermsOfServiceMethods.close_terms_of_service_browser_window(self, original_window_handle)


if __name__ == '__main__':
    unittest.main(verbosity=2)

