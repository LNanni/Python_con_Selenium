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

    """def SumaRestaMult(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")
        errorField = driver.find_element(By.ID, "errorMsgField")

        count = 0

        with open('DATOS_TEST.csv', 'r', encoding='utf-8') as csvFile:
            csvReader = csv.reader(csvFile)
            for row in csvReader:
                selectBuild.select_by_visible_text("2")
                number1.send_keys(row[1])
                number2.send_keys(row[2])
                selectOperation.select_by_visible_text(row[3])
                if(row[4] =='Si'):
                    onlyIntegers.click()
                calculateBtn.click()
                driver.implicitly_wait(1)
                try:
                    if(row[5].isdigit()):
                        resultadoObtenido = answerField.get_attribute('value')
                        self.assertIn(row[5], answerField.get_attribute('value'))
                    else:
                        resultadoObtenido = errorField.text
                        self.assertIn(row[5], errorField.text)
                except:
                    print("AssertionError: " + row[0]+" "+row[1]+" "+row[3]+" "+row[2])
                    print("\tIntegers Only: "+row[4]+" Resultado esperado: "+row[5])
                    count += 1
                number1.clear()
                number2.clear()

        print("Assertions = " + str(count))"""
        
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

        selectBuild.select_by_visible_text("2")
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
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text("2")
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
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text("2")
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
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text("2")
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
        answerField = driver.find_element(By.ID, "numberAnswerField")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text("2")
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
        answerField = driver.find_element(By.ID, "numberAnswerField")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text("2")
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
        answerField = driver.find_element(By.ID, "numberAnswerField")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text("2")
        number1.send_keys("25")
        number2.send_keys("0")
        selectOperation.select_by_visible_text("Divide")
        calculateBtn.click()

        self.assertIn("Divide by zero error!", errorField.text)

    def test_Divide_by_zero_only_integers(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")

        selectBuild = Select(driver.find_element(By.ID, "selectBuild"))
        number1 = driver.find_element(By.ID, "number1Field")
        number2 = driver.find_element(By.ID, "number2Field")
        onlyIntegers = driver.find_element(By.ID, "integerSelect")
        selectOperation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        calculateBtn = driver.find_element(By.ID, "calculateButton")
        answerField = driver.find_element(By.ID, "numberAnswerField")
        errorField = driver.find_element(By.ID, "errorMsgField")

        selectBuild.select_by_visible_text("2")
        number1.send_keys("25")
        number2.send_keys("0")
        selectOperation.select_by_visible_text("Divide")
        onlyIntegers.click()
        calculateBtn.click()
        number1.clear()
        number2.clear()

        driver.implicitly_wait(1)
        self.assertIn("Divide by zero error!", errorField.text)

        selectBuild.select_by_visible_text("2")
        number1.send_keys("25")
        number2.send_keys("25")
        selectOperation.select_by_visible_text("Divide")
        onlyIntegers.click()
        calculateBtn.click()

        self.assertIn("1", answerField.get_attribute('value'))
    
    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
