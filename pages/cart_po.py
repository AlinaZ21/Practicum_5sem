class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("[data-test=\"checkout\"]")

    def checkout_to_order(self) -> None:
        self.checkout_button.click()
