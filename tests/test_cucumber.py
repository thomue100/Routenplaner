import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_routenplaner():
    # Erstellen Sie eine Instanz des WebDriver, z. B. für den Chrome-Browser
    driver = webdriver.Chrome(executable_path="C:\\Users\\u608711\\PycharmProjects\\pythonProject4\\")

    # Öffnen Sie die URL des Routenplaners
    driver.get("http://localhost:5000")

    # Interaktionen mit der Benutzeroberfläche durchführen
    checkbox = driver.find_element_by_name("Berlin")
    checkbox.click()

    berechnen_button = driver.find_element_by_name("berechnen")
    berechnen_button.click()

    time.sleep(2)  # Warten, bis die Ergebnisse angezeigt werden (optional)

    # Überprüfen der erwarteten Ergebnisse
    result_container = driver.find_element_by_class_name("result-container")
    assert result_container.is_displayed()
    print('asd')

    # Weitere Überprüfungen und Interaktionen durchführen...

    # Beenden Sie den WebDriver
    driver.quit()

test_routenplaner()