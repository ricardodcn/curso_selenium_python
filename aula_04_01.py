from selenium.webdriver import Firefox

navegador = Firefox()

navegador.get ('http://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = navegador.find_element_by_tag_name('ul')

lis = lista_n_ordenada.find_elements_by_tag_name ('li')

lis[0].find_element_by_tag_name('a').texto

"""

1. Buscamos 'UL'
2. BUscamos todos os 'li' 
3. no Primeiro 'li', buscamos 'a' e pegamos o seu texto

ul
    li
        a
            texto
    li
        a
            texto
"""
