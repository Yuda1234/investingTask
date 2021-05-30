from selenium.webdriver.common.by import By


class InvestingPage:

    LOWER_PRICE_52_WK_RANGE = (By.XPATH, "//dd[@data-test='weekRange']/span[@class='key-info_dd-numeric__2cYjc'][1]")
    HIGHER_PRICE_52_WK_RANGE = (By.XPATH, "//dd[@data-test='weekRange']/span[@class='key-info_dd-numeric__2cYjc'][2]")
    LAST_PRICE = (By.XPATH, '//div[@class="instrument-price_instrument-price__3uw25 instrument-price_instrument-price-lg__3ES-Q"]'
                            '/span[@data-test="instrument-price-last"]')