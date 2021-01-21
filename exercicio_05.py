from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl


url = 'https://selenium.dunossauro.live/exercicio_04.html'

firefox = Firefox()

firefox.get(url)

sleep(3)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

sleep(3)

form = {
    'nome':'Ricardo',
    'email':'ricardo.neves@eu',
    'senha':'qwoiuiqwe',
    'telefone':'987123678'
}

preenche_form(firefox, **form)


# -------------- parte 2
sleep(2)
dict_text_area = eval(firefox.find_element_by_tag_name('textarea').text)

dict_text_url = dict(parse_qsl(urlparse(firefox.current_url).query))

dict_text_url.pop('btn')


assert dict_text_area == dict_text_url
