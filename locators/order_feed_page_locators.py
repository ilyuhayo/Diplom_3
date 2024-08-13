from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_HEADER_TEXT = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']")
    FIRST_ORDER_IN_ORDER_LIST = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6'][1]")
    ORDER_NUMBER_0105543 = (By.XPATH, "//p[text()='#0105517']")
    COMPOUND_ORDER_TEXT = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    ORDERS_DONE_BY_ALL_TIME_COUNTER = (By.XPATH, "//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDERS_DONE_BY_TODAY_COUNTER = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    ORDER_NUMBER_IN_THE_WORK_PANEL = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
