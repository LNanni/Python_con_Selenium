import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import csv

class FindElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.build = "2"

    def test_Add_integers(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("321")
        number2.send_keys("9")
        selectOperation.select_by_visible_text("Add")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("330", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()
        self.assertIn("330", answerField.get_attribute('value'))

    def test_Add_floats(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("400.3")
        number2.send_keys("9.2")
        selectOperation.select_by_visible_text("Add")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("409.5", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()
        self.assertIn("409", answerField.get_attribute('value'))

    def test_Add_symbols_number1(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("@Q")
        number2.send_keys("9.2")
        selectOperation.select_by_visible_text("Add")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("Number 1 is not a number", errorField.text)

        onlyIntegers.click()
        calculateBtn.click()
        self.assertIn("Number 1 is not a number", errorField.text)

    def test_Add_symbols_number2(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        selectOperation.select_by_visible_text("Add")
        number1.send_keys("3")
        number2.send_keys("$=")

        driver.implicitly_wait(1)
        calculateBtn.click()
        self.assertIn("Number 2 is not a number", errorField.text)

        onlyIntegers.click()
        calculateBtn.click()
        self.assertIn("Number 2 is not a number", errorField.text)

    def test_Subtract_integers(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("500")
        number2.send_keys("9")
        selectOperation.select_by_visible_text("Subtract")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("491", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("491", answerField.get_attribute('value'))

    def test_Subtract_floats(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("500.7")
        number2.send_keys("9.3")
        selectOperation.select_by_visible_text("Subtract")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("491.4", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("491", answerField.get_attribute('value'))

    def test_Subtract_Symbols_number1(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("34+21")
        number2.send_keys("9.3")
        selectOperation.select_by_visible_text("Subtract")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("Number 1 is not a number", errorField.text)

        onlyIntegers.click()
        calculateBtn.click()
        self.assertIn("Number 1 is not a number", errorField.text)

    def test_Subtract_Symbols_number2(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("31")
        number2.send_keys("9.3.4")
        selectOperation.select_by_visible_text("Subtract")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("Number 2 is not a number", errorField.text)

        onlyIntegers.click()
        calculateBtn.click()
        self.assertIn("Number 2 is not a number", errorField.text)

    def test_Multiply_integers(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("1024")
        number2.send_keys("2")
        selectOperation.select_by_visible_text("Multiply")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("2048", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()
        self.assertIn("2048", answerField.get_attribute('value'))

    def test_Multiply_floats(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("124.6")
        number2.send_keys("7.1")
        selectOperation.select_by_visible_text("Multiply")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("884.66", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()
        self.assertIn("884", answerField.get_attribute('value'))

    def test_Multiply_symbols_number1(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("(8)")
        number2.send_keys("9.2")
        selectOperation.select_by_visible_text("Multiply")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("Number 1 is not a number", errorField.text)

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("Number 1 is not a number", errorField.text)

    def test_Multiply_symbols_number2(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("6")
        number2.send_keys("98+2")
        selectOperation.select_by_visible_text("Multiply")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("Number 2 is not a number", errorField.text)

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("Number 2 is not a number", errorField.text)

    def test_Concatenate_numbers(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("321")
        number2.send_keys("9")
        selectOperation.select_by_visible_text("Concatenate")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("3219", answerField.get_attribute('value'))

    def test_Concatenate_symbols(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("** Test d")
        number2.send_keys("e Hola **")
        selectOperation.select_by_visible_text("Concatenate")
        calculateBtn.click()
        
        self.assertIn("** Test de Hola **", answerField.get_attribute('value'))
        
    def test_Divide_negative_integers(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("-999999999")
        number2.send_keys("-999999999")
        selectOperation.select_by_visible_text("Divide")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("1", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("1", answerField.get_attribute('value'))

    def test_Divide_positive_integers(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("9999999999")
        number2.send_keys("9999999999")
        selectOperation.select_by_visible_text("Divide")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("1", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("1", answerField.get_attribute('value'))

    def test_Divide_negatives(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("-9999999.9")
        number2.send_keys("-9999999.9")
        selectOperation.select_by_visible_text("Divide")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("1", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("1", answerField.get_attribute('value'))

    def test_Divide_positives(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("99999999.9")
        number2.send_keys("99999999.9")
        selectOperation.select_by_visible_text("Divide")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("1", answerField.get_attribute('value'))

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("1", answerField.get_attribute('value'))

    def test_Divide_symbols_Number1(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("##%$")
        number2.send_keys("15")
        selectOperation.select_by_visible_text("Divide")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("Number 1 is not a number", errorField.text)

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("Number 1 is not a number", errorField.text)

    def test_Divide_symbols_Number2(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("15")
        number2.send_keys("1fdes5")
        selectOperation.select_by_visible_text("Divide")
        calculateBtn.click()

        driver.implicitly_wait(1)
        self.assertIn("Number 2 is not a number", errorField.text)

        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("Number 2 is not a number", errorField.text)

    def test_Divide_by_zero(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("25")
        number2.send_keys("0")
        selectOperation.select_by_visible_text("Divide")
        calculateBtn.click()

        self.assertIn("Divide by zero error!", errorField.text)

        calculatingImg = driver.find_element(By.ID, "loadEquipment")
        self.assertTrue(not calculatingImg.is_displayed())

    def test_Divide_by_zero_only_integers(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text(self.build)
        number1.send_keys("25")
        number2.send_keys("0")
        selectOperation.select_by_visible_text("Divide")
        onlyIntegers.click()
        calculateBtn.click()
        number1.clear()
        number2.clear()

        driver.implicitly_wait(1)
        self.assertIn("Divide by zero error!", errorField.text)

        calculatingImg = driver.find_element(By.ID, "loadEquipment")
        self.assertTrue(not calculatingImg.is_displayed())
    
    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
