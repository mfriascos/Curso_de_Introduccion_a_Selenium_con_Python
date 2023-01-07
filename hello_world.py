import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    #*setUp ejecutará todo lo necesario antes de hacer una prueba
    #*Este decorador ayuda a que todas las pruebas se ejecuten en una sola ventana y no se cierren, también se cambia cls por self 
    @classmethod        
    def setUpClass(cls) -> None:        #*Se tiene test_fixtures, que están definidos como métodos 
        cls.driver = webdriver.Chrome(executable_path='./chromedriver') #*Se indica cual es el driver
        driver = cls.driver
        driver.implicitly_wait(10)  #*Se indica al driver que espere 10 segundos antes de realizar la acción.

    #*Este es un caso de prueba donde se realizará una serie de acciones para que el navegador automatice
    def test_hello_world(self):     #*Es importante escribir la palabra test, para que el interprete lo tenga en cuenta 
        driver = self.driver
        driver.get('https://www.platzi.com')
    
    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.com')

    #*Se realizan otras acciones para finalizar las pruebas
    @classmethod
    def tearDown(cls) -> None:     #* Dará la salida    
        cls.driver.quit()          #*Cerrará la ventana y todas sus pestañas
        

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))
