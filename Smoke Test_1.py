from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    # Iniciar sesión
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

    element = driver.find_element(By.ID, 'user-name')
    element.send_keys('standard_user')

    element = driver.find_element(By.ID, 'password')
    element.send_keys('secret_sauce')
    time.sleep(5)
    element.submit()

    # Agregar al carrito
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()
    time.sleep(5)

    # Ir al carrito
    cart_button = driver.find_element(By.ID, "shopping_cart_container")
    time.sleep(5)
    cart_button.click()

    # Pagar el carrito
    Pay_cart_button = driver.find_element(By.ID, "checkout")
    time.sleep(5)
    Pay_cart_button.click()

    # Llenar el formulario
    Nombre = "Juan"
    Apellido = "Perez"
    CP = "0987"
    element = driver.find_element(By.ID, 'first-name')
    element.send_keys(Nombre)

    element = driver.find_element(By.ID, 'last-name')
    element.send_keys(Apellido)

    element = driver.find_element(By.ID, 'postal-code')
    element.send_keys(CP)
    time.sleep(5)

    # Pagar el carrito después del formulario
    Continuar_cart_button = driver.find_element(By.ID, "continue")
    Continuar_cart_button.click()

    # Terminar la compra
    Finish_cart_button = driver.find_element(By.ID, "finish")
    Finish_cart_button.click()

    # Regresar al menú principal (HOME)
    HOME_cart_button = driver.find_element(By.ID, "back-to-products")
    HOME_cart_button.click()
except Exception as e:
    print(f"Ocurrió un error: {e}")

time.sleep(20)
driver.close()
