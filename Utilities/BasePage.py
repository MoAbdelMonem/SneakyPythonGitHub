import xlrd
from selenium.webdriver.common.by import By


class BasePage(object):
    #   Navigation Bar Locators
    view_profile_drop_down = (By.XPATH, "/html/body/div[2]/div/ul[2]/li[3]/a")
    sign_out_list_item = (By.XPATH, "/html/body/div[2]/div/ul[2]/li[3]/div/div/form/button")

    #   Properties

    #   Methods

    #   Initialization
    def __init__(self, driver):
        self.driver = driver

    #   Finding all Page Elements.
    def validate_page_elements(self, page_elements_list):
        try:
            for each_element in range(len(page_elements_list)):
                self.driver.find_element(*page_elements_list[each_element])

        except:
            raise InvalidPageException("The Page is not loaded. Current page title: " + self.driver.title)

    # Sign out from the current logged in user.
    def sign_out(self):
        self.driver.find_element(*self.view_profile_drop_down).click()
        self.driver.find_element(*self.sign_out_list_item).click()

    #   Verify current page title
    def current_page_title_verification(self, current_page, expected_page_title):
        current_page.assertRegex(self.driver.title, expected_page_title,
                                 "The Expected Page is not loaded. Current page title is: " + self.driver.title)

    #   Navigate to URL
    def go_to_url(self, url):
        self.driver.get(url)

    #   Switch to the new window that has just opened
    def switch_to_new_window(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])

    #   Close the new window (currently open) and switch to original window
    def close_and_switch_to_original_window(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    #

    #   read data from a certain sheet in the Test Data workbook "SneakyPythonGitHubTestData.xlsx"
    @staticmethod
    def get_data_from_excel(sheet_name):
        # create an empty ist to get data
        rows = []
        # open excel workbook and get excel sheet
        book = xlrd.open_workbook('..\Tests\SneakyPythonGitHubTestData.xlsx')
        sheet = book.sheet_by_name(sheet_name)
        for row_index in range(1, sheet.nrows):
            rows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
        return rows


class InvalidPageException(Exception):
    #   Throw this exception when you don't find the correct page
    pass