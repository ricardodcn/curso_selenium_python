from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
"""
1. Pegar todos os links de aulas
    {'nome da aula' : 'link da aula'}
2. Navegar ate o exercício 3
    Achar a url do exercicio 3 e ir ate la

"""

browser = Firefox()

browser.get ('http://selenium.dunossauro.live/aula_04.html')

def get_links (browser, elemento):
    """
    pega todos os links dentro de um elemento

    - browser = a instancia do Navegador
    - element = webelement ['aside', main, body, ul, ol]

    """
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a') # o nome dos links ancorados em 'a'

    for ancora in ancoras:
        resultado [ancora.text] = ancora.get_attribute('href') #pega os links na tag href e armazena no dicionario 'resultado'

    return resultado
"""
parte 1
"""
sleep(3)

aulas = get_links(browser, 'aside')

pprint (aulas)

exercicios = get_links(browser, 'main')

pprint (exercicios)

#browser.get(exercicios['Exercício 3'])  # pega o exercício 3, pelo nome que está na TAG
#main = browser.find_element_by_tag_name('main')
