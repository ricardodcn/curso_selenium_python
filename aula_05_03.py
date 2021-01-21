from selenium.webdriver import Firefox
from time import sleep
url = 'http://selenium.dunossauro.live/aula_05_c.html'

firefox = Firefox()

firefox.get(url)

def melhor_filme(browser, filme, email, telefone):
    """
    Preenche o formulário do melhor filme de 2020
    """
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()

melhor_filme(
firefox,
'Parasita',
'ricardo.neves@eu',
'(021)991110101'
)



"""
firefox.find_element_by_name('filme').send_keys('Parasita')
sleep(1)
email = firefox.find_element_by_name('email')

email.send_keys('ricardo@gmail.com')
sleep(1)
telefone = firefox.find_element_by_name('telefone')

telefone.send_keys('(021)99999-0101')

firefox.find_element_by_name ('enviar').click()
"""
sleep(3)
#firefox.quit()
