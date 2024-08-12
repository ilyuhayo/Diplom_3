from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    R2_D3_BUN = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8' and @href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    R2_D3_BUN_INGREDIENT_DETAILS_WINDOW_HEADER = (By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")
    CLOSE_WINDOW_DETAILS_INGREDIENT_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    MAKE_BURGER_HEADER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    DRAG_ORDER_CONSTRUCTOR = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    IDENTIFIER_ORDER_TEXT = (By.XPATH, "//p[@class='undefined text text_type_main-medium mb-15']")
