from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads
url = 'http://selenium.dunossauro.live/aula_05.html'

firefox = Firefox()

firefox.get(url)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

sleep(3)

estrutura = {
    'nome':'Ricardo',
    'email':'ricardo.neves@eu',
    'senha':'qwoiuiqwe',
    'telefone':'987123678'
}

preenche_form(firefox, **estrutura)

url_parseada = urlparse(firefox.current_url)

sleep(2)

texto_resultado = firefox.find_element_by_id('result')
resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_result = loads(resultado_arrumado)

assert dic_result == estrutura


#    O QUE ACONTECE QUANDO CLICA NO BOTAO ENVIAr    ?
#    nome=Ricardo
#    &
#    email=ricardo.neves%40eu
#    &
#    senha=qwoiuiqwe
#    &
#    telefone=987123678
#    &
#    btn=Enviar!#
