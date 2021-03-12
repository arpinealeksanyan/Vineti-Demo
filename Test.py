import EnvSetup
from MainPage import ShopMainPage
from CheckoutPage import CheckoutPage

from selenium import webdriver

driver = webdriver.Chrome(EnvSetup.DRIVER_PATH)
shopPage = ShopMainPage(driver)
checkoutPage = CheckoutPage(driver)

driver.get(EnvSetup.BASE_URL)
driver.maximize_window()

# Get items price summarry
sum_price_in_shop = shopPage.get_items_with_discount()

# Get items price summary and total shipping in checkout page
sum_in_checkout = checkoutPage.get_total_ammount()
total_shipping = checkoutPage.get_total_shipping()

# Sum prices in shop and total shipping
sum_price_in_shop+=total_shipping
sum_price_in_shop = '$' + str(sum_price_in_shop)

print("Summary in checkout page: " + sum_in_checkout)
print("Summary of item's prices: " + sum_price_in_shop)
assert sum_price_in_shop == sum_in_checkout, "Summary of item prices should be the same as in checkout page."

checkoutPage.click_checkout_button()

driver.quit()