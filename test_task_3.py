from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
    
driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')

driver.find_element(By.CSS_SELECTOR, '#login-button').click()

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
driver.find_element(By.CSS_SELECTOR, '#checkout').click()

driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Данил')
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Стафейчук')
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('660074')

driver.find_element(By.CSS_SELECTOR, '#continue').click()

total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text

driver.quit()

def test_screen():
    assert total == 'Total: $58.29'