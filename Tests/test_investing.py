from Tests.base_project_test_class import *


class TestInvesting(BaseProjectTestClass):

    def test_get_last_price_check_if_no_lower_from_range(self):
        last_price = self.driver.tools.get_text_from_element(InvestingPage.LAST_PRICE)
        lower_wk_range = self.driver.tools.get_text_from_element(InvestingPage.LOWER_PRICE_52_WK_RANGE)
        f_last_price = float(last_price)
        f_lower_wk52 = float(lower_wk_range)
        assert f_last_price >= f_lower_wk52

    def test_get_last_price_check_if_no_higher_from_range(self):
        last_price = self.driver.tools.get_text_from_element(InvestingPage.LAST_PRICE)
        higher_wk_range = self.driver.tools.get_text_from_element(InvestingPage.HIGHER_PRICE_52_WK_RANGE)
        f_last_price = float(last_price)
        f_higher_wk52 = float(higher_wk_range)
        assert f_last_price <= f_higher_wk52




