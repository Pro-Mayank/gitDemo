import pytest

from dictData.DictDataSets import DictData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestForm(BaseClass):

    def test_form_submission(self, get_data):
        logs = self.getlogger()
        homepage = HomePage(self.driver)
        logs.info("candidate Name details "+ get_data["Name"])
        homepage.fill_name().send_keys(get_data["Name"])
        homepage.fill_email().send_keys(get_data["email"])
        logs.debug("email details: " + get_data["email"])

        homepage.checkbox().click()
        self.SelectOptionByText(homepage.get_gender(), get_data["gender"])
        homepage.get_submit().click()
        message = homepage.get_successMessage().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=DictData.get_excel_test_data("Test2"))
    def get_data(self, request):
        return request.param



