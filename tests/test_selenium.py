import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_routenplaner():
    # Erstellen Sie eine Instanz des WebDriver, z. B. für den Chrome-Browser
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    # Öffnen Sie die URL des Routenplaners
    driver.get("http://127.0.0.1:5000")

    # Interaktionen mit der Benutzeroberfläche durchführen
    checkbox = driver.find_element_by_name("Berlin")
    checkbox.click()

    checkbox = driver.find_element_by_name("Wiesbaden")
    checkbox.click()

    berechnen_button = driver.find_element_by_name("berechnen")
    berechnen_button.click()

    time.sleep(2)  # Warten, bis die Ergebnisse angezeigt werden (optional)

    # Überprüfen der erwarteten Ergebnisse --> Ist auch dann wahr, wenn nur eine checkbox angeklickt wird
    result_container = driver.find_element_by_class_name("result-container")
    assert result_container.is_displayed()

    # Weitere Überprüfungen und Interaktionen durchführen...

    # Beenden Sie den WebDriver
    driver.quit()


test_routenplaner()
