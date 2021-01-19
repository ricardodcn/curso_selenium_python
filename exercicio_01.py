#Crie um Programa com selenium que
#Gere um dicionário, onde a chave é H1
#O valor deve ser um novo dicionario
# Cada chave do valor deverá ser o valor de 'atributo'
# cada valor deve ser o texto contido no elemento


from selenium.webdriver import Firefox

from time import sleep

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

navegador = Firefox()

navegador.get(url)

sleep(1)

tag = navegador.find_element_by_tag_name('h1')

atributo = navegador.find_elements_by_tag_name('p')

navegador.quit()
