from BasePage import BasePage

class CheckoutPage(BasePage):
	total_ammount_locator 				= ('XPATH', './/*[@id="total_price"]')
	shipping_price_locator				= ('XPATH', './/*[@id="total_shipping"]')
	checkout_button_locator				= ('XPATH', './/*[@class="cart_navigation clearfix"]//a[@title="Proceed to checkout"]')
	page_heading_locator				= ('XPATH', './/*[@class="page-heading"]')

	def __init__(self, driver):
		self.driver = driver

	def get_total_ammount(self):
		return str(self.get_element_text(self.total_ammount_locator))

	def get_total_shipping(self):
		total_shipping = str(self.get_element_text(self.shipping_price_locator))
		return round(float(total_shipping[1:]), 2)

	def click_checkout_button(self):
		self.do_click(self.checkout_button_locator)
		checkout_page_heading = str(self.get_element_text(self.page_heading_locator))
		
		# Verify that user is in authentication page
		assert checkout_page_heading == 'AUTHENTICATION'