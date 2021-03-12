from BasePage import BasePage


class ShopMainPage(BasePage):
	discount_elems_locator 				= ('XPATH', './/*[@id="homefeatured"]//div[@class="right-block"]//span[@class="price-percent-reduction"]')
	add_to_chart_button_locator 		= ('XPATH', './/*[contains(@class, "hovered")]//div[@class="right-block"]//div[@class="button-container"]')
	item_price_locator					= ('XPATH', '(.//*[@id="homefeatured"]//div[@class="right-block"]//span[@class="price-percent-reduction"]/../span[@class="price product-price"])[%s]')
	continue_shopping_button_locator	= ('XPATH', './/*[contains(@title, "Continue shopping")]')
	process_to_checkout_button_locator	= ('XPATH', './/*[@class="btn btn-default button button-medium"]')

	def __init__(self, driver):
		self.driver = driver

	def get_items_with_discount(self):
		discount_elems = self.return_elements_list(self.discount_elems_locator)
		sum_of_prices = 0
		index = 1
		for element in discount_elems:
			# Get each item price with discount
			price = str(self.get_element_text(('XPATH',self.item_price_locator[1]%str(index))))
			print("%s item's price is: "%str(index) + price)
			sum_of_prices += float(price[1:])
			sum_of_prices = round(sum_of_prices, 2)
			index+=1

			# Add item to chart
			self.hover_element(element)
			self.do_click(self.add_to_chart_button_locator)
			self.driver.implicitly_wait(3)

			# if we still have items with discount continue adding to chart
			if element != discount_elems[-1]:
				self.do_click(self.continue_shopping_button_locator)
			else:
				self.do_click(self.process_to_checkout_button_locator)
		return sum_of_prices