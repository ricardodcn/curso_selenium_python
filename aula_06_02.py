from selenium.webdriver import Firefox
from time import sleep

b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

#usando a tag type [attr=valor]
#nome = b.find_element_by_css_selector('[type="text"]').send_keys ('Ricardo')
#senha = b.find_element_by_css_selector('[type="password"]').send_keys ('Ric123')
#btn = b.find_element_by_css_selector('[type="submit"]').click()

#usando o atributo name [attr=valor]
#nome = b.find_element_by_css_selector('[name="nome"]').send_keys ('Ricardo')
#senha = b.find_element_by_css_selector('[name="senha"]').send_keys ('Ric123')
#btn = b.find_element_by_css_selector('[name="l0c0"]').click()

# usando o atributo [att*=valor]
#nome = b.find_element_by_css_selector('[name*="ome"]').send_keys ('Ricardo')
#senha = b.find_element_by_css_selector('[name*="nha"]').send_keys ('Ric123')
#btn = b.find_element_by_css_selector('[name*="l0"]').click()

#usando o atributo | [att|=valor]
#nome = b.find_element_by_css_selector('[name|="nome"]').send_keys ('Ricardo')
#senha = b.find_element_by_css_selector('[name|="senha"]').send_keys ('Ric123')
#btn = b.find_element_by_css_selector('[name|="l0c0"]').click()

#usando o atributo ^ [att^=valor]
#nome = b.find_element_by_css_selector('[name^="n"]').send_keys ('Ricardo')
#senha = b.find_element_by_css_selector('[name^="s"]').send_keys ('Ric123')
#btn = b.find_element_by_css_selector('[name^="l"]').click()


"""
nome=Ricardo&senha=Ric123&l0c0=Enviar%21#
"""
